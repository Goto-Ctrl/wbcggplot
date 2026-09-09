# B3 Case Study 2026 - Student Course Repository

This is the **student-visible course repository**. Course materials are released progressively as the semester advances. The repository intentionally does **not** contain future solution paths, reference implementations, hidden tests, or instructor notes.

## Start here — 9/25 Kickoff baseline

At kickoff, use only the materials currently visible in this repository:

1. `kickoff/B3_2026_0925_Kickoff_Student.pdf` — course orientation.
2. `kickoff/STUDENT_HANDOUT.md` — student-facing kickoff handout.
3. `docs/GIT_STUDENT_WORKFLOW.md` — Git workflow used throughout the semester.
4. `labs/tutorials/SMALL_PCAP_ANALYSIS_FIRST.md` — first PCAP self-study text.
5. `slides/small_pcap_analysis_first/main.pdf` — short companion slides used progressively in class.
6. `labs/lab0_pcap/README.md` — Lab 0 instructions.
7. `docs/B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md` — weekly purpose, current task, and exit condition.

The course repository grows over time. **Do not worry if a later Lab or later tutorial is not present yet.** It will be released when the class reaches the question that motivates it.

## First setup

```bash
git clone <COURSE_REPOSITORY_URL> b3-case-study-2026
cd b3-case-study-2026
git remote rename origin course
git remote add origin <YOUR_PRIVATE_REPOSITORY_URL>
git push -u origin main
python -m venv .venv
python -m pip install -r requirements-dev.txt
python -m labs.tools.kickoff_check
python -m labs.tools.inspect_pcap
python -m pytest -q tests_public
```

Use `origin` for your private work and `course` only to receive instructor releases.

```bash
git fetch course --tags
git log --oneline --decorate --all -n 15
```

Do not add the instructor-private repository as a remote.

## How the learning path works

We begin with **small PCAPs that are easy to inspect**. You will learn what a packet record means, what is observed directly, and what is derived by our code. Later, we deliberately increase the workload and ask whether the same convenient approach still works well.

The course follows this recurring cycle:

> **Read → Try → Observe → Explain → Improve → Re-test**

New techniques are introduced only after the problem they solve has become visible in your own measurements. The goal is not to memorize one tool, but to learn how to choose and justify a data-processing design for research.

## Weekly rhythm

- **Monday — Briefing:** weekly question, short concept material, exit condition.
- **Tuesday — Working Seminar:** code, PCAPs, intermediate results, debugging.
- **Friday — Evidence Seminar / Milestone:** evidence, interpretation, claim boundary, next question.

Before each meeting, check the current row in [`docs/B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md`](docs/B3_WEEKLY_TEACHING_PLAN_AND_SLIDE_MAP.md).

## Release workflow

When the instructor announces a new course release:

```bash
git fetch course --tags
git merge --no-edit <announced-release-tag>
```

Then continue your own work and push it to your private `origin`.
