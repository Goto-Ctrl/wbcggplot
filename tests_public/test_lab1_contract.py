from labs.lab1_flow_session import starter

def test_lab1_api_is_present():
    assert callable(starter.canonical_flow_key)
    assert callable(starter.build_flows)
    assert callable(starter.build_sessions)
