#!/usr/bin/env python3
"""Absurd micro-startup pitch entry for make.fun's 'Absurd Micro-Startup Pitch-Off'.

Writes one sentence to /output/entry.txt: a pitch for a micro-startup that
watches your ex-landlord's deposit for 30 days and files the small-claims
form on day 31, taking 20% only when the check clears. Deterministic: the
same text on every run. Stdlib only, no network.
"""

import os

LINE = "We watch your ex-landlord's $1,800 deposit for 30 days, file the small-claims form on day 31, and take 20% only when the check clears — you never call anyone."

# Entry gate, per the bounty rules: UTF-8 text, 1-200 characters,
# not whitespace-only, exactly one line plus a trailing newline.
# The entry is a fixed constant, so every run writes byte-identical output;
# validate() re-checks the written file so a truncated write is caught too.
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return text unchanged if it satisfies the entry gate, else raise."""
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") == 1 and text.endswith("\n"), (
        "entry must be exactly one line plus a trailing newline"
    )
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(LINE + "\n")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read and re-validate so a truncated write is caught, not silent.
    with open("/output/entry.txt", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
