# Lab 1 - PacketRecord to Bidirectional Flow and Session

## Goal
Turn ordered packet observations into explicit bidirectional flow and session abstractions while documenting the conventions that create those abstractions.

## Implementation Specification
Before coding, read `labs/lab1_flow_session/SPECIFICATION.md`. It is the authoritative baseline contract for definitions, function/artifact behavior, edge cases, the tiny worked example, and what the public tests do or do not certify.

## What to Read
- `labs/common/schema.py`
- `labs/lab1_flow_session/starter.py`
- `templates/reports/lab1.md`
- your Lab 0 field-use policy

## What to Do
1. Implement `canonical_flow_key` so FW and BW packets map to one bidirectional flow.
2. Implement `build_flows` with a documented FW/BW convention.
3. Implement `build_sessions` using an explicitly declared inactivity timeout.
4. Hand-check at least one small flow/session example.
5. Change the timeout once and record what changes.

Baseline to reproduce: protocol plus an unordered pair of `(IP, port)` endpoints; earliest observed source direction defines baseline FW; session boundaries are created by inactivity timeout.

## How to Test
```bash
python -m pytest -q tests_public
```

## What to Submit
- `labs/lab1_flow_session/starter.py`
- `reports/lab1.md` created from `templates/reports/lab1.md`

Commit/push both to your private `origin` repository.

## What to Present
Explain:
- why reverse packets map to the same flow key;
- why first-packet direction is a convention rather than guaranteed client/server truth;
- how session counts change when the timeout changes;
- one setting (VPN, multiplexing, NAT, QUIC, etc.) where 5-tuple aggregation may be misleading.

## Exit Condition
Your implementation passes the public contract test, you can reproduce one flow/session by hand, and your report states the chosen key, direction rule, timeout, and one failure mode.

## Claim Boundary
**You may claim:** your documented rules deterministically construct flow/session objects from the supported observations.

**You may not claim:** that a 5-tuple flow equals an application session, that FW always means client-to-server, or that the chosen timeout is universally correct.
