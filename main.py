# Say What Actually Broke — R2 entry
# Writes one line of software error copy to /output/entry.txt.

import os

LINE = "Your download stopped at 99%. Try again — it restarts from 0%, because remembering where it stopped was too much to ask."


def main():
    # Gate self-check: 1-200 chars, not only whitespace (RULES.txt).
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip(), "line is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Byte-verify what was actually written, immediately.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    assert not written.endswith("\n"), "no trailing newline"
    print(f"entry.txt: {len(written)} chars, {len(written.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
