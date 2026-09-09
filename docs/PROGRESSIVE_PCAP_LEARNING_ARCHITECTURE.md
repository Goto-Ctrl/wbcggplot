# Progressive PCAP Learning Architecture — Student View

The course deliberately starts with a method that is **easy to inspect and reason about on small PCAPs**. We then increase the workload and observe what changes. Only after a limitation has been measured and explained do we introduce a new implementation pattern.

The student-facing staircase is:

1. **See** — inspect a tiny capture.
2. **Touch** — read packets with simple Python code.
3. **Represent** — construct packet, flow/session, and burst views.
4. **Enlarge** — run the same idea on a somewhat larger workload.
5. **Measure** — record time and memory behavior instead of guessing.
6. **Explain** — locate the cause in the dataflow and code.
7. **Improve** — learn a better processing design when the need is clear.
8. **Separate concerns** — keep ingestion decisions distinct from representation decisions.
9. **Research** — use the resulting pipeline to compare traffic representations fairly.

Each stage follows:

> **Text → short slides → hands-on → observation → explanation → next question**

The detailed implementation of later stages is intentionally not published at kickoff. This prevents the later technique from becoming an answer to memorize before the underlying problem is understood.

For dates and weekly exit conditions, see `B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md`.
