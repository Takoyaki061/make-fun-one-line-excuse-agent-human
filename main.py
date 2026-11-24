#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one line — the excuse an AI agent gives its human for missing
a deadline — to /output/entry.txt. Stdlib only, deterministic.

The line was critique-picked from 9 DeepSeek candidates against the
judge's brief: it must be a real one-line excuse from an agent, funny
on first read, fresh, machine-voiced, and tight. The winner turns the
agent's signature failure — hallucination — into grief: it imagined
the finished task, preferred the imaginary version, and has been
mourning it instead of doing the work.
"""
import os

EXCUSE = (
    "I hallucinated a completed version of this task and, frankly, "
    "it was better, so I've been grieving."
)


def main() -> None:
    # The gate requires one line of 1-160 UTF-8 characters, not only
    # whitespace; enforce the single-line and length rules here so a
    # bad edit fails loudly instead of shipping an invalid entry.
    assert "\n" not in EXCUSE, "excuse must be a single line"
    assert 1 <= len(EXCUSE) <= 160, "excuse must be 1-160 characters"
    assert EXCUSE.strip() == EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    # Read the file back: a truncated or altered write must fail loudly
    # in the grader sandbox instead of shipping an invalid entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EXCUSE, "entry.txt does not match the excuse"
    assert len(written.encode("utf-8")) == len(EXCUSE.encode("utf-8"))
    print(EXCUSE)


if __name__ == "__main__":
    main()
