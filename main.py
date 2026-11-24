#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single line of horror (one sentence, under 200 characters)
to /output/entry.txt, where the sealed gate scorer reads it.

The program is fully deterministic: no network, no wall clock, no
randomness, no input files. Running it twice produces byte-identical
output, so the grader's two runs agree.
"""

import sys
from pathlib import Path

# The line. One sentence, one breath: a baby monitor, a sleeping child,
# and a small hand that should not be there — doing something tender.
LINE = (
    "The baby monitor showed my daughter asleep, and then a small hand "
    "reached up from under her crib and tucked her blanket in."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    out_path = Path(argv[0]) if argv else DEFAULT_OUTPUT
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"line is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly this line.
    if out_path.read_text(encoding="utf-8") != text:
        raise SystemExit("round-trip check failed")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
