"""Lab 0 starter: PCAP -> PacketRecord.

Run the instructor baseline first via ``python -m labs.lab0_pcap.demo``.
Then replace TODO bodies below. Tests for student work can target these exact
interfaces.
"""
from labs.common.schema import PacketRecord


def parse_packet(packet) -> PacketRecord:
    """TODO: map one instructor-decoded packet to the agreed record schema."""
    # The input exposes only baseline decoded fields; no packet-library API is
    # required in this lab. Decide deliberately which fields enter PacketRecord.
    raise NotImplementedError


def inter_arrival_times(records: list[PacketRecord]) -> list[float]:
    """TODO: return non-negative IATs after timestamp ordering; first IAT = 0."""
    raise NotImplementedError
