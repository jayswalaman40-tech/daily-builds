# Environment Probe Report

Generated: 2026-08-23 (automated environment probe)

## 1) Python

- `python3 --version` → `Python 3.11.15` (works)
- `python --version` → `Python 3.11.15` (works — `python` resolves to the same 3.11.15 interpreter)

Both `python3` and `python` are available and functional.

## 2) Headless Screenshot

None of the commonly-named binaries were found on PATH:

- `chromium` — not found
- `chromium-browser` — not found
- `google-chrome` — not found
- `google-chrome-stable` — not found
- `wkhtmltoimage` — not found
- `npx puppeteer` — `puppeteer` module is not installed/resolvable in this workspace

However, this sandbox ships a pre-installed Playwright-managed Chromium that is **not** on PATH under any of the standard names:

- `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`
- Binary: `/opt/pw-browsers/chromium` (symlink → `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`)
- A `headless_shell` variant also exists at `/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`

Test performed:

```
echo '<h1 style="color:green">PROBE OK</h1>' > test.html
/opt/pw-browsers/chromium --headless=new --disable-gpu --no-sandbox \
  --screenshot=test.png --window-size=800,400 file://$PWD/test.html
```

Result: **succeeded** (exit code 0). Output included harmless D-Bus warnings
(`Failed to connect to the bus...`) which do not affect the screenshot.
`test.png` was created, **5407 bytes**.

**Conclusion:** no headless browser exists under the conventional binary
names, but a working Chromium is available at the fixed path
`/opt/pw-browsers/chromium`. Daily automation that needs screenshots should
use this explicit path (or the `headless_shell` binary) rather than
searching PATH.

## 3) Git / System

```
$ git --version
git version 2.43.0

$ uname -a
Linux vm 6.18.44-fc-v21 #1 SMP PREEMPT_DYNAMIC @0 x86_64 x86_64 x86_64 GNU/Linux
```

## SUMMARY

`python=yes (python3 & python, 3.11.15) | screenshot=yes (binary: /opt/pw-browsers/chromium, not on PATH under standard names) | push=pending (see commit result)`
