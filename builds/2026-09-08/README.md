# Build — 2026-09-08: Technician Turnover Cost Calculator

## Research (what drove the pick)

Searched current home-service pain points — labor cost, turnover, retention,
and Reddit/forum threads on pricing pressure (r/HVAC, r/plumbing, mikeholt.com
pricing threads) — before building.

Shortlist considered:
1. **Technician Turnover Cost Calculator** ← built (strongest sourced numbers,
   clear "hidden margin leak" angle, not yet on site)
2. Employee overtime/burden-rate calculator — overlaps with `true-rate-calculator`
   (already covers the loaded hourly cost of labor) — too close to existing tool
3. Weather-day / cancellation impact calculator for outdoor trades (roofing,
   landscaping) — real pain point but thinner sourcing this session; saved for
   a future build

Signals for the pick:
- **Trade turnover rates run 12%-21%** depending on trade — electrical
  highest at 21%, garage door lowest at 12% (ServiceTitan "State of the
  Trades" technician tenure/turnover data).
- **Replacing a service tech costs 0.5x-2x their annual salary** once lost
  productivity, team disruption, recruiting and training-to-full-productivity
  are counted (Wrenchway, Applause HQ industry data).
- A tech earning **$55,000/year can cost $55,000-$110,000 to replace**; a
  20-tech shop at a 17.5% blended turnover rate was estimated at
  **over $275,000/year** in turnover cost (Applause HQ / Wrenchway).
- An HVAC contractor at 30% turnover was estimated to carry a **hidden
  $45,000-$75,000/year "tax"** that never appears as a line item on the P&L
  (industry benchmark write-ups, 2026).
- Checked existing `<slug>/` folders and `posts/`: `true-rate-calculator`
  answers "what should I charge per hour," `capacity-planner` answers
  "am I overbooked today" — nothing on the site prices the cost of *losing*
  a technician. Clear gap, and a natural sibling to `callback-cost-calculator`
  (both are "hidden margin leak" tools).

## What was built

`turnover-cost-calculator/index.html` — a free, no-signup calculator. Owner
enters technicians on staff, annual turnover rate, average annual salary per
tech, and a replacement-cost slider (50%-200% of salary, default 150% —
mid-range of the 0.5x-2x industry benchmark). Tool shows technicians lost per
year, monthly cost, and annual cost, with a red-flag banner when turnover is
at/above the 12%-21% industry range.

## Sample run (real, computed this session — see output.txt)

`calculator.py` runs three sample scenarios (sample data only — no real
employees or customers):

- **Small 4-tech shop, 20% turnover, $58k avg salary, 1.5x replacement cost**
  → 0.8 techs lost/year → **$69,600/year** hidden turnover cost
- Same shop at a strong-retention **8% turnover** → **$27,840/year**
  → **$41,760/year recoverable** by cutting turnover from 20% to 8%
- **20-tech shop at the industry-benchmark 17.5% turnover**, $55k avg salary,
  1.0x replacement cost → 3.5 techs lost/year → **$192,500/year** (directionally
  matches the ~$275k/year figure reported for a 20-tech shop at a similar rate
  with a higher replacement multiplier — sanity-checks the model against
  published industry data)

## Sources
- ServiceTitan, "State of the Trades" — technician tenure & turnover by trade
- Wrenchway, "The Cost of Technician Turnover and How to Prevent It"
- Applause HQ, "Retaining Technicians Saves Thousands vs. Hiring" / "How to
  Cut Technician Turnover by up to 25% or More"
