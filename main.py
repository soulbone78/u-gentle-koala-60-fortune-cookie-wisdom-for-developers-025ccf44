#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- entry program.

Writes a single original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Pure standard library, no dependencies.
"""

import os

FORTUNE = "Your estimate was never wrong; the future simply refused to be measured."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
