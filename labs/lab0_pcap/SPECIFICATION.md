# Lab 0 Specification -- PCAP to PacketRecord

## Purpose and scope
Lab 0 establishes the observation boundary. Students do **not** write a PCAP binary parser. The instructor-provided decoder exposes a small, stable decoded-packet object. Students map that object into `PacketRecord` and derive inter-arrival times (IATs).

Baseline input is classic PCAP containing Ethernet + IPv4 + TCP/UDP frames accepted by `labs/common/pcap.py`. IPv6, pcapng, IP reassembly, application parsing, inner VPN traffic, and QUIC stream semantics are outside the baseline.

## Canonical definitions
`PacketRecord` has exactly these fields in the baseline:

- `timestamp: float` -- capture time in seconds.
- `src_ip`, `dst_ip: str` -- IPv4 addresses rendered as strings.
- `src_port`, `dst_port: int | None` -- transport ports when available.
- `protocol: str` -- baseline values `"TCP"` or `"UDP"`.
- `packet_length: int` -- observed IP-packet length used by later representation labs.
- `payload_length: int` -- decoded transport payload length.
- `tcp_flags: int | None` -- TCP flags for TCP; `None` for UDP.

The canonical IAT sequence is computed **after sorting by timestamp ascending**. For ordered records `p_1,...,p_n`:

- `IAT_1 = 0.0`
- `IAT_i = max(0, timestamp_i - timestamp_{i-1})` for `i > 1`.

## Function contracts
### `parse_packet(packet) -> PacketRecord`
**Input:** one instructor-decoded packet object. It exposes the nine baseline fields listed above.

**Output:** one `PacketRecord` with the same semantic values. Do not invent, normalize, hash, anonymize, or drop fields inside this function.

**Required invariants:**
- integer lengths remain non-negative integers;
- UDP uses `tcp_flags=None`;
- the function does not infer FW/BW direction -- that begins in Lab 1;
- the function does not derive IAT -- that is a separate transformation.

### `inter_arrival_times(records) -> list[float]`
**Input:** zero or more `PacketRecord` objects, not necessarily pre-sorted.

**Output:** one float per input record, corresponding to timestamp-sorted order.

**Required behavior:**
- empty input -> `[]`;
- one record -> `[0.0]`;
- first IAT is exactly `0.0`;
- all returned IATs are non-negative;
- ties in timestamp produce zero IAT.

## Edge cases and failure modes
- A snaplen-truncated frame is rejected by instructor infrastructure rather than silently treated as a shorter packet.
- Fragmented IPv4 packets are excluded from the canonical decoder; students do not reassemble them in Lab 0.
- Unsupported frames may be skipped by the decoder. "PCAP contains N frames" and "baseline decoder returns N PacketRecords" are therefore different statements.
- Capture timestamp order must never be assumed from the Python input list; sort explicitly for IAT.

## Tiny worked example
Suppose the decoder gives three packets at times `1.050`, `1.000`, `1.020` seconds. After sorting, the order is `1.000, 1.020, 1.050`, so:

```text
IAT = [0.000, 0.020, 0.030]
```

For the provided `canonical_smoke.pcap`, the infrastructure smoke check should report 7 supported decoded packets: 5 TCP and 2 UDP. This count validates the provided decoder/fixture, not the student's research conclusion.

## Public-test alignment
The kickoff/public infrastructure test checks that the canonical PCAP is readable and that the decoded packet fields exist. It intentionally does **not** certify the student's full `parse_packet`/IAT implementation during the initial environment check.

Student correctness is additionally checked by the Lab 0 report, seminar evidence, and instructor/hidden tests. A passing kickoff test therefore means "environment and fixture are usable", not "Lab 0 is complete".

## Lecture-material boundary
The briefing/seminar explains why IP addresses, ports, payload-derived fields, protocol identifiers, timing, and packet length can create useful signal or shortcut leakage. The specification only defines the baseline data contract. Deciding which observed fields should become model input is a scientific design question recorded in `templates/reports/lab0_plan.md`.
