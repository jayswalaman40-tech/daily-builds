# Build — 2026-09-13: Weather Day / Rain-Out Cost Calculator

## Research (what drove the pick)

Searched current home-service pain points for outdoor trades — weather
delays, rain-outs, storm response, and crew scheduling around weather
(roofing/HVAC/landscaping industry write-ups, contractor forums) — before
building.

Shortlist considered:
1. **Weather Day / Rain-Out Cost Calculator** ← built (strongest sourced
   numbers, clear "hidden margin leak" angle for outdoor trades, flagged
   as a future idea in an earlier build's README and never shipped)
2. Storm-lead response calculator (cost of slow response to storm-driven
   leads) — overlaps with `speed-to-lead-tracker`, too close to an
   existing tool
3. Inventory/parts stockout cost calculator — real pain point but thin,
   verifiable sourcing this session; saved for a future build

Signals for the pick:
- **Weather delays cost outdoor trades 15%-25% of potential working
  hours annually**, with high-rain regions (40+ rain days/year) seeing a
  **5%-7% annual revenue reduction** (contractor industry write-ups on
  roofing weather delays).
- **Rain delays cost roofing crews an average of $500-$800/day** in lost
  labor and equipment fees, and a **5-worker crew at ~$25/hr can lose
  $30,000-$50,000/year** to weather-delay idle labor alone (independent
  industry estimate).
- Weather-driven demand swings account for **22%-35% of annual revenue**
  for roofing, HVAC, and plumbing contractors, and 67% of contractors
  describe their weather response as "reactive" rather than planned.
- A 1-day storm can cascade into a multi-day delay: crews often wait
  2-3 extra days after heavy rain for ground/equipment access, turning
  one rained-out day into up to four lost days.
- Checked existing `<slug>/` folders and `posts/`: `drive-time-calculator`
  prices travel cost, `capacity-planner` prices being overbooked — nothing
  on the site prices the cost of a canceled/delayed *weather* day, even
  though it was explicitly noted as a gap in the 2026-09-08 build notes.

## What was built

`weather-day-calculator/index.html` — a free, no-signup calculator for
outdoor trades. Owner enters crew size, average hourly wage, weather days
lost per month, and revenue lost per canceled day. Tool shows the cost
per weather day, per month, and per year (idle labor cost + lost billed
revenue), with a benchmark flag against the 15%-25% industry range.

## Sample run (real, computed this session — see output.txt)

`calculator.py` runs three sample scenarios (sample crew/revenue data
only — no real employees or customers):

- **Small roofing crew (tool defaults): 5 workers, $28/hr, 4 weather
  days/month, $2,200 revenue lost/day** → **$3,320/weather day**,
  **$13,280/month**, **$159,360/year**
- **3-person landscaping crew, drier climate: $22/hr, 2 weather
  days/month, $1,400/day** → **$46,272/year**
- **Benchmark check: 5-worker crew, $25/hr, labor cost only (no revenue
  term), 3.33 weather days/month** → **$39,960/year** — matches the
  published **$30,000-$50,000/year** industry estimate for this exact
  crew profile, sanity-checking the model against outside data.
- Cutting scenario 1's weather days lost from 4/month to 2/month (faster
  reschedule / buffer-day planning) → **$79,680/year recoverable**.

## Sources
- Contractor-industry write-ups on the real cost of weather delays for
  roofing businesses (rain-day labor/equipment cost, cascading delay days)
- Industry estimate: 5-worker crew at $25/hr losing $30k-$50k/year to
  weather-delay idle labor
- Industry data on weather-driven revenue share (22%-35% of annual
  revenue) and reactive vs. planned weather response for roofing, HVAC,
  and plumbing contractors
