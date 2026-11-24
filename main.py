#!/usr/bin/env python3
"""Write one original one-line office joke to /output/entry.txt.

The joke is about the office printer: it only ever jams or runs out of
toner, so management's "paperless-office strategy" turns out to be
literally true — the office is paperless because nothing ever prints.
The punchline lands in the last few words: the broken printer is not a
failure of the strategy, it IS the strategy, and it is working.

The program checks the competition's own gate before writing: the text
must be 1 to 200 characters, a single line, no leading or trailing
whitespace, and it is written with no trailing newline, so entry.txt
holds exactly what the judge reads. Standard library only, no network,
no input, fully deterministic.
"""

import os

JOKE = (
    "The office printer only has two moods: 'paper jam' and 'low toner' "
    "\u2014 management calls it our paperless-office strategy, and "
    "honestly, it's working."
)

MAX_CHARS = 200


def main() -> None:
    joke = JOKE
    if not joke.strip():
        raise SystemExit("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if joke != joke.strip():
        raise SystemExit("joke must not start or end with whitespace")
    if len(joke) > MAX_CHARS:
        raise SystemExit(
            "joke is %d characters, over the %d limit" % (len(joke), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != joke.encode("utf-8"):
        raise SystemExit("entry.txt bytes do not match the joke")
    print(joke)


if __name__ == "__main__":
    main()
