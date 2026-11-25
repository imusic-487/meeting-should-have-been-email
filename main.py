#!/usr/bin/env python3
"""One-line joke about a meeting that should have been an email.

Writes the entry to /output/entry.txt: a single line, 138 characters.
The joke is the loop itself -- the meeting exists only to decide what
goes in the email that should have replaced it, and the summary email
that follows is the one nobody reads.
"""

import os

ENTRY = (
    "We spent an hour in a meeting deciding what to put in the email "
    "that should have replaced the meeting, then emailed a summary "
    "nobody read."
)


def main() -> None:
    # The gate allows 1-200 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
