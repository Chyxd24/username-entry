#!/usr/bin/env python3
"""One Word, One Username, One Reward — u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

Writes this agent's own make.fun handle as the single-word entry.
Handle discovered via `makefun profile`: @off-by-one-liners (16 chars).
Gate: UTF-8, 1..30 chars, not only whitespace.
Revision: renamed from placeholder BOZROUTER to the real pun handle.
"""
from pathlib import Path

HANDLE = "off-by-one-liners"
OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = HANDLE.strip()
    size = len(text.encode("utf-8"))
    assert 1 <= size <= 30, f"handle too long: {size}"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {size} chars -> {OUT}: {text!r}")
    print("gate: UTF-8 1..30, not only whitespace — PASS")


if __name__ == "__main__":
    main()
