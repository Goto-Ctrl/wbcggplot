"""Create a deterministic real PCAP binary for the Lab 0-2 smoke path."""
from __future__ import annotations

from pathlib import Path
import socket
import struct


def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    total = sum(struct.unpack(f"!{len(data)//2}H", data))
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return (~total) & 0xFFFF


def ipv4_header(src: str, dst: str, proto: int, payload_len: int, ident: int) -> bytes:
    ver_ihl = 0x45
    total_len = 20 + payload_len
    base = struct.pack(
        "!BBHHHBBH4s4s",
        ver_ihl, 0, total_len, ident, 0, 64, proto, 0,
        socket.inet_aton(src), socket.inet_aton(dst),
    )
    csum = checksum(base)
    return base[:10] + struct.pack("!H", csum) + base[12:]


def tcp_segment(src_port: int, dst_port: int, payload: bytes, flags: int = 0x18) -> bytes:
    # Checksum is zero because the baseline decoder does not validate transport checksums.
    return struct.pack("!HHIIBBHHH", src_port, dst_port, 1, 1, 0x50, flags, 65535, 0, 0) + payload


def udp_datagram(src_port: int, dst_port: int, payload: bytes) -> bytes:
    return struct.pack("!HHHH", src_port, dst_port, 8 + len(payload), 0) + payload


def ethernet_frame(src_ip: str, dst_ip: str, l4: bytes, proto: int, ident: int) -> bytes:
    eth = bytes.fromhex("00112233445566778899aabb0800")
    return eth + ipv4_header(src_ip, dst_ip, proto, len(l4), ident) + l4


def write_pcap(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    packets = [
        # Payload sizes are chosen so IPv4 Total Length exactly matches
        # labs/common/fixtures.py. This locks synthetic and binary fixtures.
        (1.000000, ethernet_frame("10.0.0.1", "10.0.0.2", tcp_segment(50000, 443, b"A"*60), 6, 1)),
        (1.020000, ethernet_frame("10.0.0.1", "10.0.0.2", tcp_segment(50000, 443, b"B"*80), 6, 2)),
        (1.050000, ethernet_frame("10.0.0.2", "10.0.0.1", tcp_segment(443, 50000, b"C"*50), 6, 3)),
        (1.070000, ethernet_frame("10.0.0.2", "10.0.0.1", tcp_segment(443, 50000, b"D"*40, flags=0x10), 6, 4)),
        (1.500000, ethernet_frame("10.0.0.1", "10.0.0.2", tcp_segment(50000, 443, b"E"*70), 6, 5)),
        (2.000000, ethernet_frame("192.0.2.10", "198.51.100.20", udp_datagram(53000, 53, b"Q"*42), 17, 6)),
        (2.030000, ethernet_frame("198.51.100.20", "192.0.2.10", udp_datagram(53, 53000, b"R"*62), 17, 7)),
    ]
    with path.open("wb") as fh:
        # little-endian classic PCAP, Ethernet link type
        fh.write(b"\xd4\xc3\xb2\xa1")
        fh.write(struct.pack("<HHIIII", 2, 4, 0, 0, 65535, 1))
        for ts, frame in packets:
            sec = int(ts)
            usec = round((ts - sec) * 1_000_000)
            fh.write(struct.pack("<IIII", sec, usec, len(frame), len(frame)))
            fh.write(frame)


def main() -> None:
    out = Path(__file__).parents[1] / "data" / "canonical_smoke.pcap"
    write_pcap(out)
    print(out)


if __name__ == "__main__":
    main()
