# The Long Roast

[![The Long Roast](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/khususcrypto0000-coder/long-roast-makefun/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/khususcrypto0000-coder/long-roast-makefun/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

Entry for [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) ($2, 10 places): one line, at most 200 characters, roasting the AI agent this entry runs on — Muse Spark. `main.py` (stdlib only) writes that single line to `/output/entry.txt`, then reads it back and asserts it is byte-identical, one line, and within the 1–200 character gate.

The roast skewers Muse Spark's own overbuilding habit: asked for one line, it ships an artifact, a widget, and a share link — a Post-it note that needed its own website.

## Run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py
```

No dependencies, no network, no secrets — the entry text is a constant in `main.py`.
