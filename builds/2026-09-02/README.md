# Build — 2026-09-02: True Hourly Rate Calculator

## Research (what drove the pick)

Searched for current home-service / contractor pain points (small-business
pricing pain, r/plumbing-/HVAC-/electrician-adjacent contractor pricing
discussion, "tools every contractor needs" roundups) before building.

Signals:
- Multiple pricing-guide sources (Service Nation, Markup & Profit,
  Construction Cost Accounting) converge on the same root problem: contractors
  price off "the going rate" or competitor pricing instead of their own
  overhead + labor cost, and most have never calculated a true "loaded"
  hourly rate.
- One sourced stat: **roughly 78% of contractors undercharge by $15,000+ a
  year** because they don't know their real costs (Service Nation / industry
  pricing-guide data).
- Existing free tools on the market are mostly invoicing/estimate generators
  (Billdu, Joist, Zoho, Wave) — nobody offers a quick, no-signup "what should
  my baseline hourly rate actually be" calculator that factors in overhead +
  desired pay + realistic billable hours.
- Checked our own `<slug>/` folders: `quote-margin-checker` answers "what
  should I quote *this job*", `emergency-fee-calculator` answers "what's a
  fair after-hours premium" — neither answers "what's my baseline break-even
  rate before I even write a quote." Clear gap, not a repeat.

Shortlist considered:
1. **True Hourly Rate / Overhead Recovery Calculator** ← built (strongest,
   most-cited pain point, clean single-session build, not yet on site)
2. Maintenance/membership-plan pricing & ROI calculator (recurring revenue) —
   good candidate, saved for a future run
3. Late-payment / invoice follow-up message generator — smaller, more niche

## What was built

`true-rate-calculator/index.html` — a free, no-signup calculator. Owner
enters monthly overhead (rent, vehicle & fuel, insurance, tools, software &
marketing, admin/other), desired annual pay, billable hours/week, weeks
worked/year, and target profit margin. Tool outputs annual overhead, annual
billable hours, break-even hourly rate, a recommended rate with margin built
in, and — if they enter what they currently charge — exactly how much
they're leaving on the table per year.

Logic: `annual_overhead = sum(monthly overhead) * 12`
`billable_hours = hours/week * weeks/year`
`breakeven = (annual_overhead + desired_pay) / billable_hours`
`recommended = breakeven / (1 - margin%)`
`gap = (recommended - current_rate) * billable_hours`

## Sample run (real, computed this session — see output.txt)

Solo plumber/electrician profile: $2,400/mo overhead ($28,800/yr),
$75,000 desired pay, 28 billable hrs/week × 48 weeks = 1,344 billable
hrs/year, 15% target margin, currently charging $65/hr.

- Break-even rate: **$77.23/hr**
- Recommended rate (15% margin): **$90.86/hr**
- Gap vs. current $65/hr rate: **$25.86/hr short → $34,758/year left on the table**

Live: https://answercatch.com/tools/true-rate-calculator/

## Files
- `true-rate-calculator/index.html` — the tool (added to `index.html` tools grid)
- `builds/2026-09-02/output.txt` — real computed sample output
- `builds/2026-09-02/screenshot.png` — screenshot of the live tool
