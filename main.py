#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes one deterministic one-line cat joke to /output/entry.txt
and prints it to stdout. No network, no randomness, no files read.
"""

import os

ENTRY = "My cat meows at the door, I open it, she walks away \u2014 she's not asking to come in, she's just checking I'm still her doorman."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
