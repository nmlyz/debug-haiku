#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

The haiku is fixed text: three lines in the 5-7-5 syllable shape,
73 characters including the trailing newline. Standard library only,
no network access, deterministic output.
"""

import os

HAIKU = (
    "the code was not wrong\n"
    "i rewrote it all three times\n"
    "the test was the bug\n"
)


def main():
    lines = HAIKU.splitlines()
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert len(HAIKU) <= 200, "haiku must fit within 200 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
