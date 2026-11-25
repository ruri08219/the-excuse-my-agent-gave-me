#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt (stdlib only)."""

import os

ENTRY = "Sorry \u2014 I checked my calendar three times and it kept saying tomorrow, so I believed it. It was my calendar. I wrote it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
