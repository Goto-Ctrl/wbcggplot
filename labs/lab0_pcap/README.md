# Lab 0 - PCAP to PacketRecord

## Goal
Inspect what is actually observable in a packet capture and convert supported classic Ethernet/IPv4 PCAP packets into a stable `PacketRecord` representation without silently treating labels or metadata as model input.

## Implementation Specification
Before coding, read `labs/lab0_pcap/SPECIFICATION.md`. It is the authoritative baseline contract for definitions, function/artifact behavior, edge cases, the tiny worked example, and what the public tests do or do not certify.

## What to Read
- `kickoff/STUDENT_HANDOUT.md`
- `labs/common/schema.py`
- `labs/common/pcap.py`
- `labs/lab0_pcap/starter.py`
- `templates/reports/lab0_plan.md`

## What to Do
1. Complete `starter.py::parse_packet` and `inter_arrival_times`.
2. Run the canonical PCAP and inspect packet count, timestamps, protocol, packet length, and IAT.
3. Classify candidate fields as observed, derived, or metadata/label.
4. Write a short field-use policy before using fields as model inputs.

The baseline reader intentionally accepts classic `.pcap`, not `.pcapng`. Convert pcapng first when necessary and record the conversion procedure.

## How to Test
From the repository root:

```bash
python -m labs.tools.kickoff_check
python -m pytest -q tests_public
```

## What to Submit
Commit to your private repository:
- `labs/lab0_pcap/starter.py`
- completed `reports/kickoff.md`
- completed `reports/lab0_plan.md` (create from `templates/reports/lab0_plan.md`)

Do not commit large/private PCAP data unless explicitly instructed. Record provenance/checksum instead.

## What to Present
Bring evidence showing:
- stable supported-packet count and ordered timestamps;
- non-negative IATs;
- your observed/derived/metadata field classification;
- one field you deliberately exclude and why.

## Exit Condition
You can reproducibly decode the canonical capture, explain every field in your `PacketRecord`, and state which fields are permitted as model inputs without relying on a label or shortcut feature.

## Claim Boundary
**You may claim:** the released parser/setup reproduces the stated supported observations under the documented baseline policy.

**You may not claim:** that the baseline parser supports all PCAP/pcapng, IPv6, fragmentation, encrypted application semantics, or that your chosen field policy is uniquely correct.

## Two ingestion paths: understand first, scale second

The course deliberately keeps two PCAP ingestion paths:

- `labs/common/pcap.py`: small educational decoder. Use it to inspect exactly
  how Ethernet/IPv4/TCP/UDP bytes become fields.
  capture is large, pcapng is involved, or production-grade protocol dissection
  is more important than reading every decoder line yourself.

Both paths terminate at the same `PacketRecord` contract. Verify this invariant
on the canonical fixture with:

```bash
python -m labs.tools.compare_ingestion_paths
```

This separation is intentional: **the implementation best for learning the
mechanics need not be the implementation best for a large research corpus**.

## Release boundary

At kickoff, focus only on the inspectable Lab 0 path above. Later ingestion and scaling materials are released after the class has measured the need for them.
