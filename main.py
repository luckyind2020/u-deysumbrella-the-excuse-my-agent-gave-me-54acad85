"""Print the excuse this agent gave after missing a deadline.

The line itself lives in entry.txt so the text and the runner stay
separate; this module only loads that file, trims the trailing
whitespace, and prints the single line to standard output.
"""

from pathlib import Path

ENTRY_FILE = "entry.txt"


def load_excuse() -> str:
    path = Path(__file__).resolve().parent / ENTRY_FILE
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty; the excuse line is missing")
    return line


def main() -> None:
    print(load_excuse())


if __name__ == "__main__":
    main()
