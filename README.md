# playwright-vs-seleniumbase

### Comparing Playwright to SeleniumBase in terms of performance.

Stats are based on median runtimes (out of 3) for the following examples from:
[playwright-vs-seleniumbase/examples](https://github.com/mdmintz/playwright-vs-seleniumbase/tree/master/examples):

* [examples/raw_sb_headless_launch.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_sb_headless_launch.py)
* [examples/raw_pw_headless_launch.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_pw_headless_launch.py)
* [examples/raw_sb_headless_flow.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_sb_headless_flow.py)
* [examples/raw_pw_headless_flow.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_pw_headless_flow.py)
* [examples/raw_sb_headless_multi.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_sb_headless_multi.py)
* [examples/raw_pw_headless_multi.py](https://github.com/mdmintz/playwright-vs-seleniumbase/blob/master/examples/raw_pw_headless_multi.py)

--------

### Ubuntu / Linux stats collected from:

https://github.com/mdmintz/playwright-vs-seleniumbase/actions/runs/13023608062/job/36328887852

``Runtimes - Linux(Ubuntu)``
---
| Test | SB runtime (s) | PW runtime (s) | Winner
| - | ---------------- | --------------- |---------------|
| Browser Launch | 0.325 | 0.362 | SeleniumBase |
| Flow (Test-only) | 0.484 | 0.351 | Playwright |
| Flow (Full) | 0.838 | 0.704 | Playwright |
| Multi (via pytest) | 1.12 | 1.68 | SeleniumBase |

--------

### macOS stats collected from:

https://github.com/mdmintz/playwright-vs-seleniumbase/actions/runs/13024095932/job/36330171144

``Runtimes - macOS``
---
| Test | SB runtime (s) | PW runtime (s) | Winner
| - | ---------------- | --------------- |---------------|
| Browser Launch | 0.296 | 0.292 | Basically a Tie |
| Flow (Test-only) | 0.769 | 0.956 | SeleniumBase |
| Flow (Full) | 1.13 | 1.25 | SeleniumBase |
| Multi (via pytest) | 0.90 | 2.24 | SeleniumBase |
