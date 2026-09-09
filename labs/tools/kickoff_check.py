"""Small, dependency-light kickoff environment check for the B3 case study.

This is not a scientific validation.  It only verifies that the student can
execute the distributed repository and read the canonical PCAP fixture.
"""
from __future__ import annotations

import hashlib
import platform
import subprocess
import sys
from pathlib import Path

from labs.common.pcap import load_packet_records

ROOT = Path(__file__).resolve().parents[2]
PCAP = ROOT / "labs" / "data" / "canonical_smoke.pcap"


def main() -> int:
    failures: list[str] = []
    print("B3 KICKOFF CHECK")
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")

    if sys.version_info < (3, 11):
        failures.append("Python 3.11 or newer is recommended for the course baseline")

    try:
        git_version = subprocess.check_output(
            ["git", "--version"], text=True, stderr=subprocess.STDOUT
        ).strip()
        print(git_version)
    except (OSError, subprocess.CalledProcessError):
        failures.append("Git command is not available")

    if not PCAP.exists():
        failures.append(f"Canonical PCAP is missing: {PCAP}")
    else:
        digest = hashlib.sha256(PCAP.read_bytes()).hexdigest()
        records = load_packet_records(PCAP)
        tcp = sum(r.protocol == "TCP" for r in records)
        udp = sum(r.protocol == "UDP" for r in records)
        print(f"Canonical PCAP SHA256: {digest}")
        print(f"Supported packets: {len(records)} (TCP={tcp}, UDP={udp})")
        if (len(records), tcp, udp) != (7, 5, 2):
            failures.append("Canonical PCAP counts differ from the frozen baseline")

    if failures:
        print("\nSTATUS: CHECK / ASK")
        for item in failures:
            print(f"- {item}")
        return 1

    print("\nSTATUS: PASS")
    print("This PASS verifies setup only; it does not validate a research claim.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
