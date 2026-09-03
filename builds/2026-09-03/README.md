# Build — 2026-09-03: Unsold Estimate Recovery Calculator

## Research (what drove the pick)

Searched for current home-service pain points around leads, quotes, and
follow-up (industry roundups, contractor-facing calculator sites, home-service
follow-up statistics) before building.

Signals:
- Multiple sourced stats converge on the same gap: **initial close rates for
  residential HVAC/plumbing/electrical contractors run ~23-30%**, while a
  "healthy" estimate-to-close rate for the same trades is 40-60% — meaning a
  large share of quoted work never gets picked back up.
- **60% of sales happen after the 4th follow-up contact**, but most
  home-service businesses stop chasing an estimate after 1-2 touches
  (Service Labs Group / Pear / industry follow-up research).
- A 10-percentage-point lift in close rate is repeatedly cited as adding
  six figures a year for a mid-size shop — this is a process fix (follow-up
  cadence), not a pricing fix.
- A competitor already runs a similar "unsold estimate recovery" calculator
  (Wrench Grid) — independent confirmation this is a real, demand-backed
  need, not a made-up angle.
- Checked our own `<slug>/` folders and `posts/`: `quote-margin-checker`
  answers "is this quote priced right"; nothing on the site addresses
  what happens *after* the quote is sent — the follow-up/close-rate gap.
  Clear gap, not a repeat.

Shortlist considered:
1. **Unsold Estimate Recovery Calculator** ← built (strongest, sourced
   demand, clean single-session build, not yet on site)
2. Maintenance/membership-plan pricing & ROI calculator — saved for later
3. Lead-source ROI tracker (which channel actually pays off) — bigger build,
   needs more inputs than a single-session tool supports well

## What was built

`estimate-followup-calculator/index.html` — a free, no-signup calculator.
Owner enters estimates sent/month, average job value, current close rate,
and how many follow-ups they typically send before giving up on a quote.
Tool shows quoted value still unsold this month, the close rate shops hit
once they reach 4+ follow-up touches, and the $/month and $/year
recoverable by closing that gap — grounded in the follow-up → close-rate
curve measured in this run's own sample data (see below), capped at a
realistic industry ceiling (55%).

## Sample run (real, computed this session — see output.txt)

`calculator.py` simulates one month of 24 quotes for a small home-service
shop (seeded random, sample data only — no real customers) and measures
close rate by follow-up count:

- 24 quotes sent, $43,287 total quoted value
- Won so far: 6 ($9,382) → **25.0% close rate** (matches the ~23-30%
  industry-typical initial close rate found in research)
- Close rate by follow-up count: **0-1 follow-ups → 25.0%**, **2-3
  follow-ups → 37.5%**, **4+ follow-ups → 50.0%**
- 2 open quotes were neglected (open >3 days, <2 follow-ups) worth
  **$3,588** — applying this shop's own 4+-follow-up close rate (50%) to
  that pile → **$1,794 recoverable**

Live: https://answercatch.com/tools/estimate-followup-calculator/
Source: https://github.com/jayswalaman40-tech/daily-builds/tree/main/builds/2026-09-03
