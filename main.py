#!/usr/bin/env python3
"""Fortune cookie wisdom, developer edition.

The program assembles one fortune-cookie line and drops it into
/output/entry.txt. It only uses the standard library, writes a single
line with no trailing newline, and behaves the same on every run.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output") / "entry.txt"

# The two halves of the fortune, kept apart so the sentence is built
# from its clauses rather than pasted as one long literal.
FIRST_HALF = "Your estimate was never wrong"
SECOND_HALF = "the future simply refused to be measured"


def build_fortune():
    """Join the clauses into the final one-line fortune."""
    return FIRST_HALF + "; " + SECOND_HALF + "."


def write_entry(text):
    """Create the output folder if needed and store the line as-is."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


def main():
    write_entry(build_fortune())


if __name__ == "__main__":
    main()
