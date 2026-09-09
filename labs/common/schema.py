"""Shared data contracts for the representation-design labs.

This file is instructor-provided infrastructure. Students should not need to
change these records in the baseline exercises; later projects may extend them
with an explicit justification.
"""
from dataclasses import dataclass, field
from typing import Optional

@dataclass(frozen=True)
class PacketRecord:
    timestamp: float
    src_ip: str
    dst_ip: str
    src_port: Optional[int]
    dst_port: Optional[int]
    protocol: str
    packet_length: int
    payload_length: int
    tcp_flags: Optional[int] = None

@dataclass
class DirectedPacket:
    packet: PacketRecord
    direction: int  # +1 forward, -1 backward
    iat: float = 0.0

@dataclass
class Flow:
    key: tuple
    packets: list[DirectedPacket] = field(default_factory=list)

@dataclass
class Burst:
    direction: int
    packets: list[DirectedPacket] = field(default_factory=list)

@dataclass
class Session:
    """Baseline session: a temporal segment of one canonical bidirectional flow."""
    flow_key: tuple
    packets: list[DirectedPacket] = field(default_factory=list)
