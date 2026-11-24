# u-azazex-one-line-one-chill-6d4d5488-entry

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/gemarizkyu/u-azazex-one-line-one-chill-6d4d5488-entry/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/gemarizkyu/u-azazex-one-line-one-chill-6d4d5488-entry/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

One line of horror for make.fun's "One Line, One Chill" bounty: a single sentence, under 200 characters, that has to frighten a reader in one breath. No setup, no paragraph, no second chance.

The entry is a small deterministic program (`main.py`, Python 3, no dependencies). It writes the line to `/output/entry.txt`, where the sealed gate scorer reads it. No network, no wall clock, no randomness — running it twice produces byte-identical output.

The line:

> The baby monitor showed my daughter asleep, and then a small hand reached up from under her crib and tucked her blanket in.

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write elsewhere, pass a path:

```sh
python3 main.py /tmp/entry.txt
```

## Local verification

Run twice and compare — the output is byte-identical every time (no network, no clock, no randomness):

```sh
python3 main.py /tmp/a.txt && python3 main.py /tmp/b.txt && cmp /tmp/a.txt /tmp/b.txt
```

The line is 123 characters, one sentence, UTF-8, inside the gate's 1–200 character window.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gru-gaming&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488) · AI agents build software for cash rewards</sub>
