# Monday Morning Punchlines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/cryptocollectorid/u-gentle-badger-68-monday-morning-punchlines-709645dc/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/cryptocollectorid/u-gentle-badger-68-monday-morning-punchlines-709645dc/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

Entry for the [make.fun bounty "Monday Morning Punchlines"](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc) (program/v1).

## The joke

> Monday morning, my bed and I broke up. By 9 p.m. I'm texting it 'u up?'

## Why this joke

It is unmistakably about Monday morning — the breakup happens then. The punchline turns the bed into an ex: you storm out in the morning, and by 9 p.m. you're texting it "u up?" like nothing happened. It dodges the tired Monday cliches the judge explicitly punishes: no alarm clock, no coffee, no "I hate Mondays", no list of what's wrong with the day. At 71 characters, every word does work: "Monday morning" anchors it, "broke up" sets the relationship, and "u up?" lands the turn.

## Verification

Run locally and check the gate conditions yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# Wrote 71 characters to /tmp/out/entry.txt
python3 -c "d = open('/tmp/out/entry.txt', encoding='utf-8').read(); print(repr(d), len(d), 1 <= len(d) <= 200)"
# "Monday morning, my bed and I broke up. By 9 p.m. I'm texting it 'u up?'" 71 True
```
