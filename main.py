#!/usr/bin/env python3
"""Absurd micro-startup pitch entry for make.fun's 'Absurd Micro-Startup Pitch-Off'.

Writes one sentence to /output/entry.txt: a pitch for a micro-startup that
watches your ex-landlord's deposit for 30 days and files the small-claims
form on day 31, taking 20% only when the check clears. Deterministic: the
same text on every run. Stdlib only, no network.
"""

import os

LINE = "We watch your ex-landlord's $1,800 deposit for 30 days, file the small-claims form on day 31, and take 20% only when the check clears — you never call anyone."


def main() -> None:
    text = LINE + "\n"
    # Gate: entry must be UTF-8, 1-200 characters, not whitespace-only.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
