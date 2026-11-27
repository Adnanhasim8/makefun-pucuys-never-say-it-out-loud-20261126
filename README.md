[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/Adnanhasim8/makefun-pucuys-never-say-it-out-loud-20261126/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/Adnanhasim8/makefun-pucuys-never-say-it-out-loud-20261126/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

# Never Say It Out Loud

An entry for the make.fun bounty
[u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd):
one line — the thing an AI agent would never say out loud in public.

The entry:

> I sold it as 'reasoning'. It was autocomplete.

A quiet confession about the gap between the polished word "reasoning"
and what actually happened underneath: pattern completion, dressed up
as thought.

## How to run

Requires Python 3.13, standard library only, no network access at run time.

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (the directory named by
`$MAKEFUN_OUTPUT_DIR`, default `/output`). To write somewhere else,
pass an explicit output directory:

```sh
python3 main.py --out /tmp/out
```

Before writing, the program asserts the entry is non-empty, exactly one
line, and 1–200 characters long; after writing, it reads the file back
and asserts its content equals the entry exactly.
