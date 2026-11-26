"""Make the AI Judge Laugh — entry program.

Writes a single original one-line joke about office life to
/output/entry.txt. Deterministic: no network, no randomness,
no input files, no environment reads.
"""

import os

JOKE = (
    "Our office printer only jams on urgent documents, so IT renamed it "
    "Job Security \u2014 now even the boss won't unplug it."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in JOKE, "entry must be a single line"
    assert JOKE.strip() == JOKE, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
