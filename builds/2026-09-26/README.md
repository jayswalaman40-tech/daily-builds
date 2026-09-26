# Build — 2026-09-26: Tax Set-Aside Calculator

## Research (what home-service owners actually need right now)

Searched for current (2026) pain points across home-service owner forums, trade
press, and small-business tax guidance before picking a build:

1. **Speed-to-lead / margin pressure / labor shortage** — already the subject of
   12+ existing tools in this repo (missed-call-calculator, overtime-cost-calculator,
   hiring-delay-calculator, cost-per-lead-calculator, etc). Ruled out — would repeat.
2. **Cash trapped in slow-paying receivables (30-90 day AR)** — real and cited by
   multiple sources, but `cash-flow-gap-calculator` (built 2026-09-16) already
   owns this exact angle ("How much cash is trapped waiting to get paid?").
3. **Callbacks / low first-time-fix rate** — real (best-in-class shops hit 88%
   first-time-fix vs 63% for underperformers, per ServiceTitan's contractor
   playbook), but `callback-cost-calculator` already covers this precisely.
4. **Quarterly/self-employment tax set-aside** — a near-universal pain point for
   the sole-prop and single-member-LLC owners this whole site targets, and *not*
   covered by any of the 50 existing tools. Self-employed workers are commonly
   advised to set aside "25-35% of net income" (1800Accountant, SmartAsset,
   Jackson Hewitt) because nobody withholds SE tax (15.3% — both halves of
   Social Security + Medicare) for them, and estimated payments are due
   quarterly ($1,000+ owed triggers the requirement). This was the clearest,
   most concrete gap — chosen as today's build.

Sources consulted: Housecall Pro 2026 field-service trends, Jobber 2026 growth-barrier
research, m3thods Substack trades-pain-point analysis, 1800Accountant/SmartAsset/
Jackson Hewitt self-employment tax guidance, ServiceTitan contractor playbook on
callbacks, and the IRS 2026 inflation-adjustment release (via search snippets —
direct irs.gov/taxfoundation.org fetch was blocked by network egress policy, so
figures were cross-verified across three independent secondary sources that all
agreed to the dollar).

## What was built

**Tax Set-Aside Calculator** (`tax-set-aside-calculator/`) — a self-employment
tax estimator built specifically for solo/small home-service business owners
(sole prop, single-member LLC, 1099). Enter expected net profit, filing status
(single / married filing jointly), and an optional state tax rate + average job
revenue. It returns:

- The % of every dollar to set aside (a real number, not a flat "20%" guess)
- Self-employment tax, estimated federal tax, and estimated state tax, broken out
- Total estimated tax owed for the year
- The $ amount to move to savings per job
- The four 2026 quarterly estimated-tax due dates with the payment amount for each

## Data used (real 2026 figures, verified this run)

- Federal brackets (single & MFJ, all 7 rates) — 2026 IRS inflation adjustments
- Standard deduction: $16,100 single / $32,200 MFJ (2026)
- Social Security wage base: $184,500 (2026)
- Self-employment tax: 15.3% (12.4% SS up to wage base + 2.9% Medicare) +
  0.9% Additional Medicare Tax above $200k (single) / $250k (MFJ)
- Deduction for half of SE tax, applied before the standard deduction (matches
  how Form 1040 Schedule SE actually works)

## Ran on sample data (`calc.py` / `output.txt`)

| Profile | Net profit | Filing | State rate | Set-aside % | Tax owed | Per job |
|---|---|---|---|---|---|---|
| Solo plumber | $95,000 | Single | 0% | 25.3% | $24,017 | $114 (on $450 job) |
| 3-tech HVAC shop owner | $180,000 | Single | 5% | 35.2% | $63,315 | $229 (on $650 job) |
| Married electrician | $130,000 | MFJ | 4.5% | 26.4% | $34,356 | $132 (on $500 job) |

These land squarely inside the widely-cited "25-35% of net income" rule of
thumb — confirming the bracket math is sound — while showing that the real
number moves a lot with income and state, which is exactly why a flat rule of
thumb under- or over-shoots for any given owner.

The tool's in-page JavaScript was cross-checked against `calc.py` line-for-line
(same formulas run in Node) for all three sample profiles — outputs matched to
the cent.

## Honesty notes

- Not tax advice; the tool says so in its footer and the posts don't claim otherwise.
- No client or customer data used anywhere — all three profiles are invented samples.
- State tax is a flat-rate estimate (real state tax codes vary in structure); this
  is disclosed as an estimate, not a filing-ready number.
