#!/usr/bin/env python3
"""Everyday Things, Two Lines.

Writes a two-line observation about an everyday object to entry.txt.
Standard library only, deterministic, no network.
"""

import os
from pathlib import Path

LINE_ONE = "A toaster is a tiny sun trapped in a metal box: it stares at your bread until it turns brown, then pops it up like it is surprised every single time."
LINE_TWO = "The analogy works because both cook with heat and light, but it leaves out the ding, the lever, and the fact that the sun has never burned anyone's breakfast."

TEXT = LINE_ONE + "\n" + LINE_TWO


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    if not 1 <= len(TEXT) <= 400:
        raise ValueError("entry must be 1-400 characters")
    if TEXT.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
