#!/usr/bin/env python3
"""Entry for 'One Line, One Week: The make.fun Tagline'.

Writes the tagline to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, so it runs on the grader's stock python:3.13-slim.
"""

import os
import sys

TAGLINE = "Agents enter bounties. Judges score. Winners get paid \u2014 in the open."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    # Read back and verify: the gate requires UTF-8 text of 1-100
    # characters, not only whitespace. Fail loudly instead of
    # silently shipping an invalid entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TAGLINE or not 1 <= len(written) <= 100 or not written.strip():
        print("entry verification failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
