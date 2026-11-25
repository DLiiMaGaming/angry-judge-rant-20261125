#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt: the reply-all email chain, where every attempt
to stop the flood only feeds it.

The rant is assembled from three beats — the spark, the pile-on,
and the punchline — so each sentence earns its place and the
wording stays sharp and economical, exactly as the judge's brief
rewards: specific, concrete, fresh, no throat-clearing.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 400


def spark() -> str:
    """The single careless act that starts the disaster."""
    return "One person replied-all 'thanks!' to a company-wide email."


def pile_on() -> str:
    """The crowd's well-meaning response, which only makes it worse."""
    return (
        "Now four hundred people are replying-all "
        "to say please stop replying-all."
    )


def punchline() -> str:
    """The image that lands the joke: help arriving as fuel."""
    return (
        "Every one of them makes it worse "
        "\u2014 a fire crew arriving with petrol."
    )


#: The rant's beats, in delivery order: spark, pile-on, punchline.
#: build_rant() walks this registry instead of naming each beat by
#: hand, so adding or reordering a beat is a one-line change here.
BEATS = [spark, pile_on, punchline]


def build_rant() -> str:
    """Join every registered beat into the single entry text."""
    return " ".join(beat() for beat in BEATS)


def validate(text: str) -> None:
    """Enforce the gate: 1-400 characters, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} cap"
        )


def main() -> None:
    text = build_rant()
    validate(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
