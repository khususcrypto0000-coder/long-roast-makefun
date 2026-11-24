"""The Long Roast — one-line roast of my own agent, Muse Spark.

Writes the entry text to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only.

The joke: asked for a single line, this agent overbuilds — it turns a
Post-it note into a whole website. That is the roast, and the entry
itself is the evidence.
"""

import os
import sys

ENTRY = "Muse Spark heard 'one line' and shipped an artifact, a widget, and a share link \u2014 a Post-it note that needed its own website."


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    assert not text.endswith("\n"), "entry must have no trailing newline"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == text, "read-back mismatch: file is not byte-identical"
    assert len(back.encode("utf-8")) == len(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
