from pathlib import Path
from labs.common.pcap import iter_decoded_packets

def test_canonical_pcap_is_readable():
    p=Path('labs/data/canonical_smoke.pcap')
    rows=list(iter_decoded_packets(p))
    assert len(rows)==7
    assert sum(x.protocol=='TCP' for x in rows)==5
    assert sum(x.protocol=='UDP' for x in rows)==2

def test_decoded_packet_fields_exist():
    row=next(iter(iter_decoded_packets(Path('labs/data/canonical_smoke.pcap'))))
    for field in ('timestamp','src_ip','dst_ip','src_port','dst_port','protocol','packet_length','payload_length','tcp_flags'):
        assert hasattr(row,field)
