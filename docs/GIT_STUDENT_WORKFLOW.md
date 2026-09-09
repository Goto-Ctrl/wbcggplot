# Student Git workflow

## Remotes

- `origin`: your own private student repository; read/write.
- `course`: instructor-maintained student-safe course repository; read-only.
- There is no remote pointing to the instructor-private repository.

## Normal work

```bash
git switch main
git pull --ff-only origin main
# work, test, commit
git add <files>
git commit -m "Describe the evidence or implementation change"
git push origin main
```

## Receiving a course release

The instructor announces a release tag such as `lab1-release`.

```bash
git fetch course --tags
git merge --no-edit lab1-release
git push origin main
```

Course releases are designed to be append-only: new lab files are added without overwriting previously student-owned implementations. If a corrective patch must touch an existing file, the instructor will announce it explicitly.

## Data policy

Do not commit large/raw captures unless explicitly approved. Put provenance, license/collection conditions, checksum, and preprocessing notes in `data/README.md`.
