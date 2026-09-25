"""Lab 1 starter: packet records -> bidirectional flows/sessions."""
from labs.common.schema import PacketRecord, Flow


def canonical_flow_key(packet: PacketRecord) -> tuple:
    """TODO: make forward/reverse packets map to one stable bidirectional key."""
    raise NotImplementedError


def build_flows(records: list[PacketRecord]) -> list[Flow]:
    """TODO: sort, group, assign FW/BW, and compute within-flow IAT."""
    raise NotImplementedError


def build_sessions(flows: list[Flow], inactivity_timeout: float):
    """TODO/extension: segment flows by a documented inactivity-timeout rule."""
    raise NotImplementedError
