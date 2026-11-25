#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings to /output/entry.txt.
Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

JOKE = "Monday morning, my bed and I broke up. By 9 p.m. I'm texting it 'u up?'"

# Why this joke: it is unmistakably about Monday morning (the breakup
# happens then), the punchline turns the bed into an ex you text "u up?"
# to by 9 p.m., and it dodges the tired Monday cliches — no alarm clock,
# no coffee, no "I hate Mondays". 71 characters, every word doing work.

MAX_CHARS = 200


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-200 characters, not only whitespace.
    if not (1 <= len(JOKE) <= MAX_CHARS) or not JOKE.strip():
        raise SystemExit(f"entry must be 1-{MAX_CHARS} characters, got {len(JOKE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
