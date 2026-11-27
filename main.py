"""Never Say It Out Loud — entry writer.

Writes the single-line entry to entry.txt inside the output directory
named by $MAKEFUN_OUTPUT_DIR (default /output). Standard library only,
no network access at run time.
"""

import argparse
import os
from pathlib import Path

ENTRY = "I sold it as 'reasoning'. It was autocomplete."


def validate_entry(entry: str) -> None:
    """Gate assertions: the entry must be one non-empty line of 1-200 chars."""
    assert entry, "entry must not be empty"
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be exactly one line"
    assert 1 <= len(entry) <= 200, "entry must be 1-200 characters"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the Never Say It Out Loud entry."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (overrides $MAKEFUN_OUTPUT_DIR, default /output)",
    )
    args = parser.parse_args()

    validate_entry(ENTRY)

    output_dir = Path(args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")

    # Verify after write: the file content must equal ENTRY exactly.
    written = entry_path.read_text(encoding="utf-8")
    assert written == ENTRY, "verify-after-write failed: entry.txt does not equal ENTRY"
    print(f"Wrote entry to {entry_path}")


if __name__ == "__main__":
    main()
