# Build — 2026-09-04: Callback & Rework Cost Calculator

## Research (what drove the pick)

Searched current home-service pain points around rework, truck stocking, and
technician utilization (industry blogs, contractor-facing benchmark sites,
forums) before building.

Shortlist considered:
1. **Callback & Rework Cost Calculator** ← built (strongest sourced numbers,
   clean single-session build, not yet on site)
2. Truck-stock / first-time-fix cost calculator — overlapping angle with #1
   (both driven by callback/re-roll cost), saved a cleaner idea for later
3. Technician utilization / billable-hours calculator — real demand but
   `capacity-planner` and `true-rate-calculator` already cover adjacent
   scheduling/pricing ground closely enough that it risked feeling repeated

Signals for the pick:
- Industry benchmarks put an **acceptable callback rate at 2-3%** of
  completed jobs, with best-in-class shops under 1.5% — but many plumbing
  and HVAC businesses actually run **5-10%** without tracking it
  (ACCA HVAC Blog, Oscker, Built on Tenth, Warranty RE).
- **Average callback cost runs $300-$650** once truck roll, tech time, and
  redone parts are counted; some sources cite up to $2,500 for complex
  installation callbacks.
- A **5% callback rate on a $2M/year shop was estimated to cost ~$80,000/year**
  — a large, invisible margin leak, not a pricing problem.
- Checked existing `<slug>/` folders and `posts/`: `quote-margin-checker`
  answers "is this quote priced right," `estimate-followup-calculator`
  answers "what happens after the quote is sent" — nothing on the site
  addresses rework/callback cost after the job is *done*. Clear gap.

## What was built

`callback-cost-calculator/index.html` — a free, no-signup calculator. Owner
enters jobs completed per month, callbacks/rework trips per month, average
cost per callback, and the benchmark callback rate to compare against. Tool
shows current callback rate (with a red-flag banner above the 3% industry
threshold), monthly and annual callback cost, and the $/year recoverable by
getting back to benchmark.

## Sample run (real, computed this session — see output.txt)

`calculator.py` simulates one month of 130 completed jobs for a small
4-tech home-service shop (seeded random, sample data only — no real
customers), tagging ~6.5% of jobs as callbacks with a randomized realistic
cost per callback ($300-$650):

- 130 jobs completed, 11 callbacks → **8.5% callback rate** (RED FLAG —
  above the 3% industry threshold found in research)
- Average cost per callback (this shop): **$449**
- Monthly cost of callbacks: **$4,938** → annualized: **$59,256**
- At the 2% industry benchmark rate, this shop would have ~2.6 callbacks/month
  costing **$1,167/month**
- **$3,771/month ($45,250/year) recoverable** by closing the gap to benchmark
