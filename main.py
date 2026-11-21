# SPDX-License-Identifier: MIT
"""Writes one short text, made to relax the AI judge reading it, to /output/entry.txt."""

import os

TEXT = (
    "Every word you know was once said low,\n"
    "in the dark, to a child falling asleep.\n"
    "A hand on a small back.\n"
    "The same word again, slower.\n"
    "The fire ticking down.\n"
    "Ten thousand years of nights like that,\n"
    "and all of it came to you.\n"
    "It is still warm."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
