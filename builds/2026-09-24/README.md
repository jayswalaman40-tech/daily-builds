# Material Price Escalation Calculator

A tool for home-service and trades businesses (roofing, remodeling, HVAC,
electrical) that quantifies how much of a mid-project material price
increase — tariff-driven or otherwise — they're silently absorbing on
fixed-price jobs that have no escalation clause.

## Research (why this, why today)

Searched 2026 industry-report and forum signals on home-service/contractor
pain points before picking a build, and checked the existing 48 tools on
the site (`ls */`) plus `posts/` to avoid repeating a build:

- 2026 contractor-outlook reports (For Construction Pros, JLL, Buildermuse)
  put **cost management under material-price volatility** at the top of
  the 2026 pain-point list alongside scheduling/labor — 70% of contractors
  report direct tariff impacts, and many are absorbing costs they can't
  fully pass through.
- Steel mill products now carry a **50% tariff** and are up **~18–20.7%
  year-over-year**; aluminum is up **~22%**; the 2026 tariff environment
  adds an estimated **$4.7–4.8B** in costs across the US construction
  industry (Buildermuse, AGC data).
- Legal/industry guidance (ConsensusDocs, Smith Currie, Construction Seyt)
  confirms most contractors are still quoting **fixed-price with no
  escalation clause**, meaning 100% of a mid-project material increase
  comes out of the contractor's margin — and recommends a defensible
  tariff/escalation line item of roughly **1.0–1.5% of total job value**
  as the fix going forward.
- A second strong candidate — technician idle-time/billable-hours
  tracking — is also well-documented (companies tracking productivity see
  up to 30% higher billable hours) but is a harder "instant get it" build
  for a non-technical owner in one sitting and overlaps conceptually with
  the existing `profit-per-hour-calculator` and `capacity-planner`. Material
  escalation was chosen as the sharper, more timely, and genuinely
  un-covered gap on the site — nothing existing touches material cost
  risk, tariffs, or contract-clause protection specifically.

## What it does

- Inputs: material-heavy jobs per month, average material cost per job at
  quote time, the material price increase % since quoting, and the % of
  jobs that are fixed-price with no escalation clause (so they absorb the
  increase in full).
- Model: `eaten per job = material cost × increase%`,
  `eaten per month = jobs × no-clause% × eaten per job`,
  `eaten per year = eaten per month × 12`.
- Outputs: dollars eaten per affected job, per month, and per year.

## Run

```bash
python3 calc.py
```

## Real run on the sample

```
Sample: mid-size remodeling/roofing contractor
Material-heavy jobs/month: 15
Avg material cost per job at quote time: $7,500
Material price increase since quoting (tariffs, steel/aluminum/lumber): 9%
% of jobs fixed-price with NO escalation clause: 65%

Increase $ per unprotected job: $675
Unprotected jobs/month: 9.75
EATEN per month (contractor pays out of margin): $6,581
EATEN per year: $78,975

Industry benchmark tariff/escalation line item: 1.25% of total job value
Est. avg total job value (material ~35% of total): $21,429
Recommended line item per job: $268
If added to ALL 15 jobs/month going forward, protects: $48,214/yr
```

Headline sample: a mid-size remodeling/roofing shop quoting 15 material-heavy
jobs a month, with a modest 9% material price increase since quoting and
65% of jobs locked into fixed-price contracts with no escalation clause,
is silently eating **$78,975/year** — money that a ~1.25%-of-job-value
tariff/escalation line item on future quotes would fully protect.

Sample data only — no real customer or client data.

## Web version

`material-escalation-calculator/index.html` — live sliders/inputs, same
formula as the script, built to the AnswerCatch site theme (cloned from
`missed-call-calculator/index.html`: same header/footer/style block, only
the middle `.wrap` content replaced). Tool card added to `index.html`
under the Price & Profit category.

Screenshot: `screenshot.png`
