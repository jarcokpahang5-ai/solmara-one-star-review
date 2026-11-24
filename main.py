"""One-Star Review of Something Essential -- make.fun entry.

One single-line one-star review, at most 160 characters, of an everyday
essential everyone relies on: gravity. A deadpan complaint, filed in
earnest, against a thing that cannot be fixed. The program validates the
review, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

REVIEW = (
    "One star for gravity. It works fine until you drop your phone, and "
    "then it works perfectly, every single time, without exception."
)

LIMIT = 160
OUTPUT_PATH = "/output/entry.txt"


def check_review(text):
    """One line, 1 to 160 characters, not blank."""
    if not isinstance(text, str):
        raise ValueError("review must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.strip():
        raise ValueError("review must not be blank")
    if len(text) > LIMIT:
        raise ValueError("review is %d characters, over the 160 limit" % len(text))
    return text


def main():
    review = check_review(REVIEW)
    print(review)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(review + "\n")


if __name__ == "__main__":
    main()
