# debug-haiku

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/nmlyz/debug-haiku/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/nmlyz/debug-haiku/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A tiny Python program that writes a single haiku about debugging to a text file. The poem is three lines in the traditional 5-7-5 syllable shape, and the program checks its own output before finishing.

## The haiku

```
the code was not wrong
i rewrote it all three times
the test was the bug
```

## Usage

```sh
python3 main.py
```

This creates `entry.txt` in the output directory — `/output` by default, or the directory named by the `OUTPUT_DIR` environment variable. The output is deterministic: every run writes exactly the same 73 bytes.

## How it works

`main.py` keeps the poem as a list of three lines, joins them with newlines, and validates the result before writing: exactly three non-blank lines, at most 200 characters, ending with a newline. After writing, it reads the file back and confirms the contents match. Only the Python standard library is used, and the program makes no network access.

## License

MIT — see [LICENSE](LICENSE).
