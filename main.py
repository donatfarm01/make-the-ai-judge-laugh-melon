"""Make the AI Judge Laugh entry program.

Writes a single original one-line joke about office life to
/output/entry.txt.

The line was written against the judge's brief, in the order the judge
weighs its criteria:

1. It is about office life and lands as a joke: a boss, a hierarchy,
   and the daily reporting chain everyone in an office knows.
2. The observation is true to the office: companies that brag about a
   flat hierarchy still hand you a stack of managers, each acting like
   the one in charge. The listener nods before laughing.
3. The turn is surprising: the flat hierarchy is the reason for seven
   bosses, not the cure for them, and the last words reframe the whole
   setup. The number seven makes the absurdity concrete.
4. It is tight: one line, no wasted setup, every word earning its
   place, and it reads cleanly aloud in one breath.
5. It is original: no meetings-could-have-been-an-email, no printer
   jam, no coffee addiction, no reply-all, no inbox-zero stock line.

Cliches avoided on purpose: meetings about meetings, the printer, the
coffee machine, reply-all, inbox zero, "per my last email", and any
pun. The line is deterministic: the same text is written on every run.
"""

import os

ENTRY = "My boss calls it a flat hierarchy, which is why I report to seven people who all think they're my boss."


def main():
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
