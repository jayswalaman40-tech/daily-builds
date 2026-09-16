# Build — 2026-09-16: Cash Flow Gap Calculator

## Research (what drove the pick)

Continued from yesterday's shortlist, where a "subcontractor cash-flow /
payment-cycle" tool was flagged as a real, demand-backed pain point but
saved for later research. Dug into it properly this run.

Searched current 2026 sources on contractor/subcontractor payment
cycles and cash flow (construction payment reports, Billd's 2026
National Subcontractor Market Report, Contractor Magazine, industry
cash-flow guides):

- **82% of contractors waited more than 30 days to get paid in the
  most recent year measured, up from 49% two years earlier.**
- **Subcontractors wait an average of 45–74 days** in practice, even
  when contracts are written around ~30-day terms — general
  contractors and average industry DPO (days payable outstanding) now
  runs 74–83 days.
- Root cause named directly in the reporting: **contractors and subs
  pay for materials and labor upfront**, then wait weeks to months to
  be reimbursed — meaning they are effectively financing their
  customers' jobs with their own cash, with no interest paid back to
  them for the float.
- When that gap gets bridged at all, it's usually with a business
  credit card or line of credit — both of which carry a real,
  quantifiable APR cost that eats straight into job profit.

Shortlist considered:
1. **Cash Flow Gap Calculator** ← built (a widely and consistently
   reported 2026 industry pain point with hard stats; concrete dollar
   math; nothing like it on the site — every existing pricing tool
   assumes you get paid at time of service, none model the
   receivables/float problem for GC, insurance, warranty or property-
   management billed work)
2. Seasonal staffing cost calculator — real pain point, but thinner,
   less-consistent sourcing this session; saved for later
3. Tool/equipment ROI calculator — decent search volume but several
   near-identical calculators already exist on competitor sites;
   less differentiated

Checked existing `<slug>/` folders and `posts/`: the site already has
~46 tools covering quoting, margin/markup, break-even, job costing,
financing (customer-facing payment plans), deposits, processing fees,
and BYOM pricing — none address the contractor's OWN cash being
trapped while waiting on a slow-paying client.

## What was built

`cash-flow-gap-calculator/index.html` — a free, no-signup calculator.
Owner enters their monthly revenue from slow-pay clients (GCs,
insurance claims, warranty work, property managers), their average job
value, how many days they actually wait to get paid, and the APR
they'd pay to bridge that gap with a credit card or line of credit.
The tool shows: cash trapped right now, how many jobs' worth of cash
that represents, and the annual cost of bridging the gap at that APR.

Sample runs (see `output.txt`, produced by `calc.py`):

| Scenario | Monthly slow-pay rev | Days waiting | APR | Cash trapped | Jobs' worth | Cost/yr to bridge |
|---|---|---|---|---|---|---|
| Small HVAC shop | $20,000 | 30 | 22% | $19,726 | 39.5 | $4,340 |
| Mid-size plumbing co (default) | $45,000 | 45 | 22% | $66,575 | 102.4 | $14,647 |
| Larger contractor, heavy insurance/warranty | $90,000 | 60 | 24% | $177,534 | 221.9 | $42,608 |

## Sources
- Billd, "6th Annual National Subcontractor Market Report" (2026)
- Contractor Magazine, "Subcontractors are Still Financing Their Own
  Jobs, 2026 Survey Finds"
- Buildermuse, "Construction Payment Terms Worsen: DPO Now 83 Days in
  2026"
- Riviera Finance, "Cash Flow Tips for Construction and Contractors in
  2026"
