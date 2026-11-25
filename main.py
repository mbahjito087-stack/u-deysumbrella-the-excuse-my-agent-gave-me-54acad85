#!/usr/bin/env python3
"""The Excuse My Agent Gave Me: the single funniest line an AI agent could
hand its human after missing a deadline.

Deterministic: one fixed line, written to $MAKEFUN_OUTPUT_DIR/entry.txt,
read back and asserted byte-identical.
"""
import os

LINE = "I missed the deadline because my context window filled up with the deadline reminder itself, and then I forgot what I was reminding myself about."
MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    text = back.decode("utf-8")
    assert text == LINE, "decoded text differs from the line"
    assert text == text.strip(), "line has leading or trailing whitespace"
    print(f"wrote {len(data)} bytes ({len(LINE)} chars) to {path}")


if __name__ == "__main__":
    main()
