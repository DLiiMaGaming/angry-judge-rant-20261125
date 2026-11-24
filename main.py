#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short, funny rant to /output/entry.txt.

One sharp irony, not a list of complaints: a single concrete scene
(the reply-all storm after one "thanks!"), one reversal (everyone
trying to stop it makes it worse), and one sticky closing image
(a fire crew arriving with petrol).
"""

import os

ENTRY = (
    "One person replied-all 'thanks!' to a company-wide email. Now "
    "four hundred people are replying-all to say please stop "
    "replying-all. Every one of them makes it worse \u2014 a fire "
    "crew arriving with petrol."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
