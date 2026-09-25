# Week 1 Self-Study Seminar Guide

## Purpose

During Week 1 (9/28, 9/29, 10/2), run the seminar as a student-led
self-study session.

The goal of this week is not to finish as much code as possible.
The goal is to understand what is observed in a PCAP, what our code
transforms, and what information is preserved or discarded.

Use these materials:

- `labs/tutorials/SMALL_PCAP_ANALYSIS_FIRST.md`
- `slides/small_pcap_analysis_first/main.pdf`
- `labs/lab0_pcap/README.md`
- `docs/B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md`

---

## 9/28 — Briefing: Small PCAP and Packet Fields

### Before the seminar

Read Steps A1–A4 of:

`labs/tutorials/SMALL_PCAP_ANALYSIS_FIRST.md`

### During the seminar

Use slides A1–A5 of:

`slides/small_pcap_analysis_first/main.pdf`

Divide the slides among the participants and explain them to each other.

Discuss:

1. What can be observed directly from the PCAP?
2. What is produced or transformed by our code?
3. Which fields should be retained in `PacketRecord`?
4. Which fields or packets may be ignored by the educational reader?
5. Why must these choices be documented?

### Exit condition

Everyone should be able to explain the difference between:

- a raw observed field; and
- a derived or transformed field.

Do not try to teach the whole slide deck.

---

## 9/29 — Working Seminar: Lab 0

No new lecture is required.

Use slides A3–A5 only when needed as a reference.

Work through Lab 0 and inspect the canonical small PCAP.

Useful commands include:

```bash
python -m labs.tools.inspect_pcap
python -m pytest -q tests_public
```bash


Do not stop at "the test passed."

Compare the PCAP observations with the resulting PacketRecord objects
and make sure you can explain the correspondence.

Exit condition

You should be able to reproduce and explain how the canonical PCAP is
read into the fields used by the course.

Optional preview

If you have completed Lab 0 and can explain its evidence, you may begin
reading the released Lab 1 materials:

labs/lab1_flow_session/README.md

Lab 1 is an optional preview this week. It is not necessary to finish it
before the instructor returns.

10/2 — Evidence Seminar: What Did We Preserve and Discard?

Use slides A6–A8 as a map for the discussion.

Each student or group should briefly present evidence from Lab 0.

Explain:

What did your parser read?
What did it ignore?
What information was preserved in PacketRecord?
What information was discarded or transformed?
What can you claim from this representation?
What can you not claim?

Compare answers across the group. Differences should be discussed rather
than silently resolved.

Exit condition

Everyone should be able to explain what the parser reads and discards,
and how those choices limit later analysis.

At the end, discuss the next question:

If packets are aggregated into flows or sessions, what becomes easier
to observe, and what information might disappear?

This question leads into Lab 1.

Seminar rule

The slides are a map, not the deliverable.

For every session, leave behind evidence: code output, a small table,
a hand-checked example, or a written claim/limitation.

The objective is:

Read → Try → Observe → Explain → Improve → Re-test EOF
