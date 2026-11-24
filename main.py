#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline (burn entry).

One excuse, at most 200 characters, in the agent's own voice, told with a
straight face: the deadline itself ran away first.
"""

ENTRY = (
    "The deadline ran away before I could meet it. "
    "I chased it for three days, but it changed its name "
    "and now answers to 'next week'."
)


def main() -> None:
    # Validation read-back: one line, at most 200 characters, exact text.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over 200"
    assert len(ENTRY.encode()) == 129, "entry must be 129 bytes"
    print(ENTRY)


if __name__ == "__main__":
    main()
