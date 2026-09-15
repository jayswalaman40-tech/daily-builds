# Build — 2026-09-15: BYOM Job Pricing Calculator

## Research (what drove the pick)

Searched current home-service pain points across trade forums and
subreddits (r/plumbing, r/HVAC, r/smallbusiness) plus 2026 contractor
pricing/markup guides.

Shortlist considered:
1. **BYOM ("bring-your-own-materials") Job Pricing Calculator** ← built
   (a single, extremely consistent, named pain point across every trade
   forum searched; concrete dollar math; nothing like it on the site yet)
2. Customer Lifetime Value (CLV) calculator — real search demand, but
   several competitor sites already publish near-identical CLV calculators
   for contractors; less differentiated
3. Subcontractor/1099 cost calculator — real pain point, thinner and
   less-consistent sourcing this session; saved for later

Checked existing `<slug>/` folders and `posts/`: pricing tools on the
site already cover quotes, markup/margin, break-even, job cost,
processing fees, and profit-per-hour — none price the specific, widely
complained-about scenario of a customer supplying their own materials
and expecting a labor-only discount.

Signals for the pick:
- One search summarized it directly: **"the single most consistent
  gripe across every plumbing forum and subreddit is the customer who
  buys their own materials and expects a labor-only install at a
  discount"** (2026 trade-forum pain-point roundup).
- **Contractor material markup typically runs 15%–35%**, commonly
  20–30% on standard residential work (construction2style.com,
  foreman.co, Truitt & White 2026 pricing guides). Markup pays for
  sourcing, ordering, storage, returns, and backing the install
  warranty — none of which disappears just because the customer bought
  the part.
- **Many contractors instead charge a 15%–20% handling/risk fee on the
  value of customer-supplied materials** to cover coordination and the
  fact that they still carry install-warranty liability on parts they
  didn't source or price (ContractorTalk forum consensus, cited in
  2026 contractor-markup guides).

## What was built

`byom-calculator/index.html` — a free, no-signup calculator. Owner
enters the average materials value per job (if they'd supplied it),
their normal material markup %, the BYOM handling fee % they currently
charge (if any), and BYOM jobs per month. Tool shows margin lost per
job with no fee, the recommended handling fee, what's still left on
the table even if that fee is charged, and the annual gap between
charging nothing vs. charging the sourced 15–20% benchmark fee.

## Sample run (real, computed this session — see output.txt)

`calculator.py` runs three sample scenarios (sample business data
only — no real customer or job data):

- **Mid-size plumbing/HVAC shop (tool defaults): $650 avg materials
  value, 25% normal markup, 15% handling fee charged, 8 BYOM jobs/mo**
  → **$162 lost per job with no fee**, **$98 recommended fee**,
  **$65 still left on the table per job** even when charged →
  **$15,600/yr lost charging nothing**, **$9,360/yr recovered per year**
  by charging the sourced 15% fee instead.
- **Solo operator, high-ticket fixture installs, charging $0 fee
  today: $1,200 avg materials value, 30% markup, 5 BYOM jobs/mo** →
  **$21,600/yr** in pure lost margin — no fee currently offsets any of
  it.
- **Benchmark check**: set markup and handling fee to the same
  low-end sourced value (15% / 15%) — the fee should exactly offset the
  markup loss with $0 left on the table per job. Result: **$0 left on
  the table — MATCHES**, confirming the model's math is internally
  consistent with the sourced ranges.

## Sources

- 2026 trade-forum pain-point roundup: BYOM identified as the most
  consistent plumbing/HVAC pricing complaint
- construction2style.com, foreman.co, Truitt & White (2026): typical
  contractor material markup range (15%–35%, commonly 20–30%)
- ContractorTalk forum / 2026 contractor-markup guides: 15%–20%
  handling/risk fee as the common way contractors price BYOM jobs
