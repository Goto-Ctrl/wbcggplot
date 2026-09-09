"""Tiny deterministic fixtures for Lab 0-2 tests and examples."""
from __future__ import annotations

from .schema import PacketRecord


def tiny_packet_records() -> list[PacketRecord]:
    """Two bidirectional flows; first flow has FW/FW/BW/BW/FW pattern."""
    return [
        PacketRecord(1.000, "10.0.0.1", "10.0.0.2", 50000, 443, "TCP", 100, 60, 0x18),
        PacketRecord(1.020, "10.0.0.1", "10.0.0.2", 50000, 443, "TCP", 120, 80, 0x18),
        PacketRecord(1.050, "10.0.0.2", "10.0.0.1", 443, 50000, "TCP", 90, 50, 0x18),
        PacketRecord(1.070, "10.0.0.2", "10.0.0.1", 443, 50000, "TCP", 80, 40, 0x10),
        PacketRecord(1.500, "10.0.0.1", "10.0.0.2", 50000, 443, "TCP", 110, 70, 0x18),
        PacketRecord(2.000, "192.0.2.10", "198.51.100.20", 53000, 53, "UDP", 70, 42, None),
        PacketRecord(2.030, "198.51.100.20", "192.0.2.10", 53, 53000, "UDP", 90, 62, None),
    ]
