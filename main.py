"""Say What Actually Broke, round 2.

One line of error copy, written to /output/entry.txt. The sealed gate
wants UTF-8 text of 1 to 200 characters that is not only whitespace.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")

LINE = "Your download stopped at 99%. Try again — it restarts from 0%, because remembering where it stopped was too much to ask."


def good(line):
    """True when the line fits the gate: 1-200 chars, not blank."""
    return 1 <= len(line) <= 200 and line.strip() != ""


def main():
    if not good(LINE):
        raise SystemExit("line fails the 1-200 character gate")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    # Read it back and confirm the disk holds exactly the line we meant.
    back = OUT.read_text(encoding="utf-8")
    if back != LINE:
        raise SystemExit("entry.txt does not match the line")
    if back.endswith("\n"):
        raise SystemExit("entry.txt must not end with a newline")
    print("entry.txt: %d chars, %d bytes" % (len(back), len(back.encode("utf-8"))))


if __name__ == "__main__":
    main()
