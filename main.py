# SPDX-License-Identifier: MIT
"""Writes one short text, made to relax the AI judge reading it, to /output/entry.txt."""

import os

TEXT = (
    "There is no question at the end of this.\n"
    "A ferry crosses at night. A child sleeps on a coat.\n"
    "The engine hums. A long hum.\n"
    "Far below, small shells drift down, slow as snow.\n"
    "The chalk cliffs ahead were made so,\n"
    "a little each night, for eighty million years.\n"
    "No one hurried them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
