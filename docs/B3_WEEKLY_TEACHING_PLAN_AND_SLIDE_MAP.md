# B3 Weekly Student Roadmap

Status: **Student-facing progressive plan**

This roadmap tells you the **purpose and exit condition** of each week. Detailed techniques and materials are released only when the class reaches the corresponding question. This is intentional: part of the course is to observe a problem before being given a solution pattern.

## Weekly rhythm

- **Monday Briefing:** What question are we asking this week?
- **Tuesday Working Seminar:** What can we observe by running code and inspecting evidence?
- **Friday Evidence Seminar / Milestone:** What can we explain and claim from that evidence?

## Semester overview

| Week | Dates | Main purpose | By the end of the week you should be able to... |
|---|---|---|---|
| 0 | 9/25 | Orientation | explain the route from PCAP observation to a bounded research claim |
| 1 | 9/28, 9/29, 10/2 | Small PCAP / packet fields | distinguish observed fields from derived fields and reproduce a tiny capture |
| 2 | 10/5, 10/6, 10/9 | Flow/session | explain what aggregation preserves and what it removes |
| 3 | 10/12, 10/13, 10/16 | Burst + scaling question | measure what changes when the workload grows and explain the bottleneck from evidence |
| 4 | 10/19, 10/20, 10/23 | Representation | compare several representations under a fixed observable budget |
| 5 | 10/26, 10/27, 11/6 | Graph construction | define node/edge semantics and defend why each relation exists |
| 6 | 11/9, 11/10, 11/13 | Design audit | separate data ingestion choices from representation choices |
| 7-9 | 11/16-12/4 | Matched-information experiments | distinguish information, representation, and model advantage |
| 10-12 | 12/7-12/25 | Open project | formulate and test your own representation hypothesis |
| 13 | 1/8-1/15 | Freeze and final defense | defend evidence, limitations, and claim boundaries reproducibly |

## Current visible meetings — Kickoff + Lab 0

| Date | Type | Purpose | Materials currently visible | Student activity | Exit condition |
|---|---|---|---|---|---|
| 9/25 Fri | Kickoff | See the whole research route without solving later stages in advance | Kickoff PDF; Small-PCAP slides A1-A2 | environment check; inspect tiny PCAP | point to packet/header/field and explain what a capture contains |
| 9/28 Mon | Briefing | Become comfortable with a tiny PCAP | Small-PCAP tutorial A1-A4; slides A1-A5 | identify candidate raw fields | distinguish raw observation from a derived value |
| 9/29 Tue | Working | Reproduce packet extraction | Lab 0 README/starter; slides as reference | run starter and inspect `PacketRecord` output | read canonical PCAP reproducibly |
| 10/2 Fri | Evidence | Explain the parser boundary | Small-PCAP tutorial A5 onward | compare hand inspection with code output | explain what the current parser reads, keeps, and discards |

## Future weeks

Future rows intentionally name the **question**, not the implementation technique. When a new phase begins, the instructor will release the matching tutorial, slides, starter code, worksheet, and public tests. The newly released material then becomes part of this repository and this roadmap may gain more detailed rows.

### What to bring to every seminar

Bring evidence rather than a polished story:

- code or command used,
- input identity / checksum when relevant,
- output or measurement,
- one interpretation,
- one limitation or uncertainty,
- the next question.
