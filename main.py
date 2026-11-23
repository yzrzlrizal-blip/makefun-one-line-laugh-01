#!/usr/bin/env python3
"""One-Line Laugh entry.

Writes one original, funny line about everyday life to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output). The line is a
single sentence of at most 200 characters, as the bounty requires.
"""

import os
import sys

LINE = (
    "The Wi-Fi died for ten minutes and my family had to introduce "
    "themselves to each other again."
)
MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.replace(tmp_path, path)

    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != line + "\n":
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"{line} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
