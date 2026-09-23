# Hiring Delay Cost Calculator

A tool for home-service businesses (HVAC, plumbing, electrical, roofing) that
quantifies what an open technician position actually costs while it sits
unfilled — the revenue that goes uncovered, plus the overtime spent patching
part of the gap.

## Research (why this, why today)

Searched trade-forum and industry-report signals on home-service pain points
for 2026 before picking a build:

- 2026 industry trend reports (Jobber, ServiceTitan, ACHR News) flag labor
  shortages as a top-3 pain point alongside weather/seasonality and margins —
  23% of contractors cite it directly, and AI is increasingly used to cover
  the resulting gaps in customer response and admin work.
- Skilled-trades roles average **56 days to fill** in 2026 (industry
  benchmark) — nearly two months of a seat sitting open.
- An unfilled technician position costs an estimated **$2,000–$7,800/day**
  in lost revenue (Mar-Hy Distributors analysis), with multiple open roles
  during a seasonal rush compounding into six figures.
- **62% of plumbing contractors** in shortage markets declined at least
  $50,000 in revenue in 2024 due to staffing constraints (HireAligned, 2026).
- **58% of HVAC contractors** in shortage markets ran overtime exceeding 15%
  of total labor hours in 2024 — confirming overtime, not just lost revenue,
  is a real cost of the gap.

Existing tools on the site already cover technician **turnover** (the cost
of someone *leaving*) via `turnover-cost-calculator`. Nothing yet modeled
the cost of a seat that's simply **vacant while hiring is in progress** —
a distinct, well-documented 2026 pain point for the trades. Ruled out
duplicating drive-time/fuel, quoting, and review-focused tools already on
the site (55+ tools, checked against `posts/` and top-level folders first).

## What it does

- Inputs: open technician positions, average days to fill a role, revenue
  that seat would generate per day, and the % of the resulting gap covered
  by existing staff working overtime.
- Model: `lost revenue (uncovered) = positions × days × daily revenue × (1 − covered%)`
  and `overtime cost (covered portion) = positions × days × daily revenue × covered% × 0.6`
  (the 0.6 multiplier approximates time-and-a-half premium pay buying back
  a fraction of the lost capacity — cheaper than losing the job outright,
  never free).
- Outputs: lost revenue, overtime cost, and total cost of the vacancy.

## Run

```bash
python3 hiring_delay_calculator.py sample_shops.csv
```

## Real run on the sample (`sample_shops.csv`, 3 shops)

```
Shop                          Open   Days   Rev/day  Covered      Lost rev     OT cost    Total cost
Mid-size HVAC & plumbing co      2     56      $520      25%       $43,680      $8,736       $52,416
Solo-to-2-truck electrician shop 1     62      $410      15%       $21,607      $2,288       $23,895
Regional roofing crew (peak)     3     48      $610      35%       $57,096     $18,446       $75,542

Combined cost of current hiring gaps: $151,853
```

Headline sample: a mid-size HVAC/plumbing shop with 2 open positions at the
56-day industry-average fill time, covering 25% of the gap with overtime,
loses **$52,416** to a hiring delay it's already living through.

Sample data only — no real customer or client data.

## Web version

`hiring-delay-calculator/index.html` — live sliders/inputs, same formula as
the script, built to the AnswerCatch site theme (cloned from
`missed-call-calculator/index.html`: same header/footer/style block, only
the middle `.wrap` content replaced).

Screenshot: `screenshot.png`
