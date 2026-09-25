# Lab 1 Specification -- PacketRecord to Bidirectional Flow and Session

## Purpose and scope
Lab 1 converts packet observations into researcher-defined temporal aggregates. The baseline must be reproduced exactly before alternatives are explored.

## Canonical definitions
### Endpoint
An endpoint is `(IP address, transport port)`.

### Canonical bidirectional flow key
For one packet, form source endpoint `a=(src_ip,src_port)` and destination endpoint `b=(dst_ip,dst_port)`. Sort the two endpoints deterministically; the key is:

```text
(protocol, lower_endpoint, higher_endpoint)
```

Therefore A->B and B->A packets with the same protocol/ports share one key. This is an **unordered endpoint pair**, not a client/server label.

### FW/BW convention
Within each flow, sort packets by timestamp. The source endpoint of the earliest packet is the baseline **FW endpoint**. A packet whose source endpoint equals that endpoint is direction `+1` (FW); the reverse source is `-1` (BW).

### Flow-local IAT
After flow grouping and timestamp ordering, the first packet in each flow has `iat=0.0`. Later IATs are non-negative differences from the previous packet **in the same flow**.

### Session
A session is a temporal segment of one canonical bidirectional flow. If the gap from the previous packet is strictly greater than `inactivity_timeout`, start a new session. A session never mixes different flow keys.

## Function contracts
### `canonical_flow_key(packet) -> tuple`
- deterministic and hashable;
- identical for reverse-direction packets of one 5-tuple conversation;
- protocol is part of the key;
- must not depend on arrival order.

### `build_flows(records) -> list[Flow]`
- accept records in any order;
- group by `canonical_flow_key`;
- sort each group by timestamp ascending;
- assign FW/BW using earliest-source convention;
- set flow-local IAT;
- return deterministic flow ordering (do not depend on dictionary insertion order).

Empty input returns `[]`.

### `build_sessions(flows, inactivity_timeout) -> list[Session]`
- `inactivity_timeout` must be positive; non-positive values are invalid;
- preserve packet order and direction labels;
- split only when `gap > inactivity_timeout`;
- do not merge packets from different flow keys;
- an empty flow produces no session.

## Edge cases and failure modes
- Equal timestamps: keep deterministic order; resulting IAT can be zero.
- The earliest packet might be a server response captured after a missing request. Thus FW is a convention, not guaranteed client->server truth.
- NAT, VPN tunnels, QUIC multiplexing, HTTP/2, or reused 5-tuples can make one flow key a poor application-session model.
- A timeout of exactly the gap does **not** split under the baseline (`>` not `>=`).

## Tiny worked example
Input packets:

```text
p1 1.000 10.0.0.1:50000 -> 10.0.0.2:443 TCP
p2 1.020 10.0.0.1:50000 -> 10.0.0.2:443 TCP
p3 1.050 10.0.0.2:443   -> 10.0.0.1:50000 TCP
p4 1.070 10.0.0.2:443   -> 10.0.0.1:50000 TCP
p5 1.500 10.0.0.1:50000 -> 10.0.0.2:443 TCP
```

All five map to one canonical flow. Direction pattern:

```text
FW FW BW BW FW  ->  +1 +1 -1 -1 +1
```

Flow-local IAT:

```text
0.000, 0.020, 0.030, 0.020, 0.430
```

With timeout `0.1 s`, the `0.430 s` gap starts a second session.

## Public-test alignment
The public test checks that the required API exists. The tiny example above is the human-readable behavior contract. Instructor/hidden tests additionally check reverse-key equality, direction/IAT behavior, and timeout splitting.

A passing public API test alone does not prove semantic correctness; students must also hand-check the tiny example and present the convention.

## Lecture-material boundary
Lecture material explains why "flow", "session", "client", and "server" are not interchangeable concepts and why 5-tuple aggregation can fail in modern/tunneled traffic. The implementation specification fixes one reproducible baseline so later representation comparisons start from the same objects.
