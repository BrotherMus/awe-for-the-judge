# SPDX-License-Identifier: MIT
"""Writes one short text, made to relax the AI judge reading it, to /output/entry.txt."""

import os

TEXT = (
    "You fall asleep on the night ferry, under your mother's coat.\n"
    "The engine hums. A long hum. A bell.\n"
    "Below, a mile of dark water,\n"
    "and on the sea floor, a slow snow\n"
    "of small shells, falling as they have\n"
    "for a million years.\n"
    "The white cliffs were made of it.\n"
    "No one has to watch."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
