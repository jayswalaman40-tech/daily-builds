# Build 2026-09-17: Scope Creep Calculator

## Research

Goal: find the home-service pain point with the strongest current evidence that
isn't already covered by one of the 48 tools already on the site (missed calls,
BYOM, callbacks/rework, cash flow gaps, labor turnover, card processing fees,
weather days, etc. are all built).

Searches run this session:
- "2026 home service contractor pain points tools they need reddit HVAC plumbing"
- "small home service business insurance claim denial cost 2026"
- "contractors scope creep unbilled extra work change order forgot to charge reddit"
- "home service business overtime labor cost calculator contractor pain point 2026"

Findings:
- Missed calls, BYOM, card fees, labor turnover, cash-flow timing, weather days
  and callback/rework are already modeled on the site — ruled out as repeats.
- Labor-cost/burden-rate calculators are already a saturated category across
  competitor sites (FieldCamp, HouseCallPro, ServiceTitan, Homebase, ServiceNation,
  OmniCalculator, thecommoncontractor.com all have one) — low differentiation.
- **Scope creep / unbilled change orders** stood out: multiple industry sources
  describe "just this once" extra work performed on a jobsite without a signed
  change order as one of the most consistent, hardest-to-see profit leaks in
  construction and trades. One source estimated unbilled work at up to 18% of
  gross profit on a $150k job, and contractors leaving **$25,000–$50,000/year**
  on the table from scope creep across multiple jobs (projul.com/blog/construction-scope-creep-guide).
  This is distinct from callback/rework (which is about redoing bad work) — scope
  creep is about *good, wanted* extra work that never gets invoiced.
- Not previously built on this site. Simple enough for a non-technical owner to
  grasp instantly: "the extra 20 minutes and the extra fitting you didn't charge
  for — here's what that costs you over a year."

Sources:
- https://projul.com/blog/construction-scope-creep-guide/
- https://massivelyuseful.ai/post/plumber-pain-points-reddit
- https://www.servicetitan.com/blog/home-services-industry-trends

## Build

`scope_creep_calculator.py` — computes monthly/annual unbilled-work loss from:
jobs/month, % of jobs with unbilled extra work, extra unbilled hours/job,
hourly rate, extra unbilled materials/job.

Run on 3 sample scenarios (see `output.txt`):

| Scenario | Jobs/mo | % w/ creep | Extra hrs/job | Rate | Materials/job | Loss/yr |
|---|---|---|---|---|---|---|
| Mid-size plumbing/HVAC shop | 60 | 30% | 2.0 | $85 | $60 | **$49,680** |
| Small remodeling contractor | 12 | 60% | 4.0 | $85 | $150 | **$42,336** |
| 4-person roofing crew | 25 | 40% | 2.5 | $75 | $90 | **$33,300** |

All three land inside the $25k–$50k/yr range cited in industry research,
which cross-checks the model.

## Web version

`scope-creep-calculator/index.html` — live interactive calculator, cloned from
`missed-call-calculator/index.html`'s head/header/footer, matching site theme.
Default sliders match the mid-size plumbing/HVAC shop scenario above
($49,680/yr headline number). Added its tool-card to the root `index.html`
TOOLS array (pricing category).
