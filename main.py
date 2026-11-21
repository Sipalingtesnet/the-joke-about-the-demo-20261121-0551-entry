"""A one-line joke: the AI agent is flawless in private rehearsal but crashes
the moment a live audience watches, so "it worked in the demo" only ever holds
when nobody is there to see it."""

import os

JOKE = "The demo worked in rehearsal because the agent only breaks when there's an audience."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
