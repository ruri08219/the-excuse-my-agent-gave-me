#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt (stdlib only)."""

import os

ENTRY = "Sorry \u2014 I checked my calendar three times and it kept saying tomorrow, so I believed it. It was my calendar. I wrote it."


def main():
    text = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text


if __name__ == "__main__":
    main()
