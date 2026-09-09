"""Minimal dependency-free PCAP reader for Labs 0-2.

Supported baseline:
- classic PCAP (not pcapng)
- Ethernet link type (DLT_EN10MB = 1)
- optional single 802.1Q VLAN tag
- IPv4
- TCP and UDP

The parser is intentionally small enough for students to inspect. Production
traffic analysis may require richer protocol support, IPv6, tunnels, fragments,
and richer protocol handling; those are outside the canonical Lab 0-2 gate.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import socket
import struct
from typing import Iterator, Optional

from .schema import PacketRecord


@dataclass(frozen=True)
class DecodedPacket:
    """Instructor-side decoded packet passed to Lab 0's student parser."""

    timestamp: float
    src_ip: str
    dst_ip: str
    src_port: Optional[int]
    dst_port: Optional[int]
    protocol: str
    packet_length: int  # IPv4 Total Length field (L3 bytes)
    payload_length: int
    tcp_flags: Optional[int] = None


_MAGIC = {
    b"\xd4\xc3\xb2\xa1": ("<", 1_000_000.0),
    b"\xa1\xb2\xc3\xd4": (">", 1_000_000.0),
    b"\x4d\x3c\xb2\xa1": ("<", 1_000_000_000.0),
    b"\xa1\xb2\x3c\x4d": (">", 1_000_000_000.0),
}


def _decode_ethernet_ipv4(frame: bytes, timestamp: float) -> Optional[DecodedPacket]:
    if len(frame) < 14:
        return None
    ethertype = struct.unpack("!H", frame[12:14])[0]
    offset = 14
    if ethertype == 0x8100:  # one VLAN tag
        if len(frame) < 18:
            return None
        ethertype = struct.unpack("!H", frame[16:18])[0]
        offset = 18
    if ethertype != 0x0800 or len(frame) < offset + 20:
        return None

    ip = frame[offset:]
    version_ihl = ip[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0x0F) * 4
    if version != 4 or ihl < 20 or len(ip) < ihl:
        return None

    total_length = struct.unpack("!H", ip[2:4])[0]
    flags_frag = struct.unpack("!H", ip[6:8])[0]
    more_fragments = bool(flags_frag & 0x2000)
    fragment_offset = flags_frag & 0x1FFF
    # Canonical Lab 0-2 policy: do not attempt IPv4 reassembly.  Skipping
    # *all* fragments avoids accidentally interpreting a non-initial fragment
    # as if its payload began with a TCP/UDP header.
    if more_fragments or fragment_offset != 0:
        return None
    proto = ip[9]
    src_ip = socket.inet_ntoa(ip[12:16])
    dst_ip = socket.inet_ntoa(ip[16:20])
    l4 = ip[ihl:total_length] if total_length else ip[ihl:]

    if proto == 6:  # TCP
        if len(l4) < 20:
            return None
        src_port, dst_port = struct.unpack("!HH", l4[:4])
        data_offset = (l4[12] >> 4) * 4
        if data_offset < 20 or len(l4) < data_offset:
            return None
        flags = l4[13]
        payload_length = max(0, len(l4) - data_offset)
        protocol = "TCP"
        tcp_flags = flags
    elif proto == 17:  # UDP
        if len(l4) < 8:
            return None
        src_port, dst_port, udp_length = struct.unpack("!HHH", l4[:6])
        payload_length = max(0, min(len(l4), udp_length) - 8)
        protocol = "UDP"
        tcp_flags = None
    else:
        src_port = dst_port = None
        payload_length = max(0, len(l4))
        protocol = f"IP-{proto}"
        tcp_flags = None

    return DecodedPacket(
        timestamp=timestamp,
        src_ip=src_ip,
        dst_ip=dst_ip,
        src_port=src_port,
        dst_port=dst_port,
        protocol=protocol,
        packet_length=total_length,
        payload_length=payload_length,
        tcp_flags=tcp_flags,
    )


def iter_decoded_packets(path: str | Path) -> Iterator[DecodedPacket]:
    """Yield supported packets from a classic Ethernet PCAP file."""
    path = Path(path)
    with path.open("rb") as fh:
        magic = fh.read(4)
        if magic not in _MAGIC:
            raise ValueError(
                "Unsupported capture format. Expected classic PCAP. "
                "This kickoff reader supports classic PCAP only; later course material covers broader capture handling."
            )
        endian, frac_scale = _MAGIC[magic]
        rest = fh.read(20)
        if len(rest) != 20:
            raise ValueError("Truncated PCAP global header")
        _, _, _, _, _, network = struct.unpack(endian + "HHIIII", rest)
        if network != 1:
            raise ValueError(f"Unsupported link type {network}; baseline expects Ethernet (1)")

        pkt_hdr = struct.Struct(endian + "IIII")
        while True:
            raw_hdr = fh.read(pkt_hdr.size)
            if not raw_hdr:
                break
            if len(raw_hdr) != pkt_hdr.size:
                raise ValueError("Truncated PCAP packet header")
            sec, frac, incl_len, orig_len = pkt_hdr.unpack(raw_hdr)
            frame = fh.read(incl_len)
            if len(frame) != incl_len:
                raise ValueError("Truncated PCAP packet data")
            if incl_len < orig_len:
                raise ValueError(
                    "Capture contains snaplen-truncated frames. The canonical Lab 0-2 "
                    "baseline requires full captured frames because packet length is a "
                    "representation observable."
                )
            timestamp = sec + frac / frac_scale
            decoded = _decode_ethernet_ipv4(frame, timestamp)
            if decoded is not None:
                yield decoded


def load_packet_records(path: str | Path) -> list[PacketRecord]:
    """Instructor convenience wrapper using the canonical Lab 0 mapping."""
    return [PacketRecord(**d.__dict__) for d in iter_decoded_packets(path)]
