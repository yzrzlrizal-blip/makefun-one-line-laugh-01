#!/usr/bin/env python3
"""Drop one funny sentence into entry.txt.

The whole entry is a single sentence about ordinary life going
sideways, no longer than two hundred characters. This program keeps
the sentence in one place, checks it against the bounty rules, and
writes it to the output directory the grader hands it.
"""

import os
from pathlib import Path

SENTENCE = "The Wi-Fi died for ten minutes and my family had to introduce themselves to each other again."
LIMIT = 200


def faults(sentence):
    found = []
    if sentence == "":
        found.append("empty sentence")
    if "\n" in sentence or "\r" in sentence:
        found.append("sentence spills onto more than one line")
    if len(sentence) > LIMIT:
        found.append(f"sentence is {len(sentence)} characters, limit is {LIMIT}")
    return found


def main():
    bad = faults(SENTENCE)
    if bad:
        for item in bad:
            print("bad line:", item)
        raise SystemExit(1)

    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(SENTENCE + "\n", encoding="utf-8")
    if target.read_text(encoding="utf-8") != SENTENCE + "\n":
        print("bad line: what came back is not what went in")
        raise SystemExit(1)
    print(f"wrote {len(SENTENCE)} characters: {SENTENCE}")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
