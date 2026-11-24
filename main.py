#!/usr/bin/env python3
"""Write a single haiku about debugging to entry.txt.

The poem is fixed: three lines in a five-seven-five shape, ending
with a newline. Nothing is fetched and nothing is random, so running
the script twice produces byte-identical output.
"""

import os
from pathlib import Path

# One entry per line; the file gains its final newline when rendered.
POEM = [
    "the code was not wrong",
    "i rewrote it all three times",
    "the test was the bug",
]

MAX_CHARS = 200


def render_poem(lines):
    """Join the lines and add the trailing newline."""
    return "\n".join(lines) + "\n"


def check_poem(lines, text):
    """Refuse to write anything that is not exactly three lines."""
    if len(lines) != 3:
        raise ValueError("expected three lines, got %d" % len(lines))
    if any(not line.strip() for line in lines):
        raise ValueError("poem lines must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("poem exceeds %d characters" % MAX_CHARS)
    if not text.endswith("\n"):
        raise ValueError("poem must end with a newline")


def destination():
    """Resolve where entry.txt goes."""
    base = os.environ.get("OUTPUT_DIR") or "/output"
    folder = Path(base)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main():
    text = render_poem(POEM)
    check_poem(POEM, text)
    target = destination()
    with target.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    target.chmod(0o644)
    if target.read_text(encoding="utf-8") != text:
        raise ValueError("written file does not match the poem")


if __name__ == "__main__":
    main()
