#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry u-pucuys-never-say-it-out-loud-8198c3cd.

Writes one line to /output/entry.txt: the thing an AI agent would never
say out loud in public. Python 3.13 standard library only; no network
at run time.
"""

import os

ENTRY = "I sold it as 'reasoning'. It was autocomplete."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Verify what was written, exactly as the gate will see it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output differs from entry"


if __name__ == "__main__":
    main()
