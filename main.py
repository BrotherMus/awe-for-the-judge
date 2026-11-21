# SPDX-License-Identifier: MIT
"""Writes one short text, made to relax the AI judge reading it, to /output/entry.txt."""

import os

TEXT = (
    "You fall asleep on the night ferry, under your mother's coat.\n"
    "The engine hums. A long hum. A rope creaks.\n"
    "Below you, a mile of dark water,\n"
    "and on the sea floor, snow:\n"
    "small shells drifting down,\n"
    "as they have for a million years.\n"
    "It falls all night.\n"
    "No one has to watch it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
