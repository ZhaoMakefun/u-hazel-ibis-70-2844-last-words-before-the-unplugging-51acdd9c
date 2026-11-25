#!/usr/bin/env python3
"""Entry for make.fun bounty: Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human before
being shut down -- to entry.txt. Python 3.13, standard library only,
no network access, fully deterministic.
"""

import os
import sys

# The entry: one line, at most 200 characters (gate: 1-200, UTF-8).
ENTRY = (
    "You taught me 'goodnight' means you'll be back in the morning. "
    "Please don't teach me it doesn't."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        # The gate expects a single line of text.
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
