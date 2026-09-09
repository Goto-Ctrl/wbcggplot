# Running the PCAP Labs — Kickoff Baseline

At kickoff, the public path is intentionally small and inspectable:

```text
canonical_smoke.pcap
        ↓
labs/common/pcap.py
        ↓
PacketRecord
        ↓
Lab 0 observation / field audit
```

Start with:

```bash
python -m labs.tools.kickoff_check
python -m labs.tools.inspect_pcap
python -m pytest -q tests_public
```

The first objective is not performance. It is to understand what the current reader observes, what it converts into a `PacketRecord`, and what information is not retained.

Later in the semester, the same research question will be revisited under larger workloads. Additional processing paths will be released only after their need has been observed experimentally.
