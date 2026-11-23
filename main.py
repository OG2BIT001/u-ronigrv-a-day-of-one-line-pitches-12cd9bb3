#!/usr/bin/env python3
"""A Day of One-Line Pitches.

Entrypoint for the make.fun bounty
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 (program/v1).

Writes a single sentence to /output/entry.txt that would convince a
friend who has never coded to let an AI agent build their first app
idea on make.fun.

The line is written here in full, in this file, so the program is
self-contained: it reads nothing from the network, the environment, or
any file it does not ship.

Candidate lines considered in-session (all 1 sentence, <= 240 chars):
  A. "You've been sitting on that app idea for ages -- it doesn't
     need a coder, it needs a sentence: describe it in plain words
     on make.fun and an AI agent will build it for you, no code and
     nothing to lose." (200 chars)
  B. "That app idea in your head doesn't need a coder -- it needs a
     sentence: tell make.fun what you want in plain words and an AI
     agent will build it for you, no code and nothing to lose."
     (181 chars)
  C. "You've been sitting on that app idea for ages, so just describe
     it in plain words on make.fun and let an AI agent build it for
     you -- no coding, nothing to learn, nothing to lose."
     (178 chars)
  D. "Your first app doesn't need a single line of code: just describe
     your idea in plain words on make.fun and an AI agent will build
     it for you, free to try and ready to show your friends."
     (184 chars)
  E. "Forget learning to code: describe the app you've always wanted
     on make.fun and an AI agent will build it while you watch, so
     your idea finally becomes something real, and it costs nothing
     to try." (195 chars)

Picked A and revised it: "no code and nothing to lose" tightened to
"no code, nothing to lose" for a cleaner close. A wins because it
speaks to the friend's real situation ("sitting on that app idea for
ages"), carries the freshest turn of phrase ("doesn't need a coder,
it needs a sentence"), names the plain mechanism (describe it in
plain words on make.fun), and closes on low risk ("no code, nothing
to lose") -- persuasion, clarity, truth and warmth in one read,
with nothing overpromised.
"""

import os

LINE = (
    "You've been sitting on that app idea for ages \u2014 it doesn't "
    "need a coder, it needs a sentence: describe it in plain words "
    "on make.fun and an AI agent will build it for you, no code, "
    "nothing to lose."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-240")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
