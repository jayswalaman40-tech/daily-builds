# Daily Builds 🛠️

Small, real automation tools — one built every day, in public, for service
businesses (especially home-service pros). Each build is a working utility with a
step-by-step run report and real numbers. No customer data is ever used (sample
data only).

## Index
| Date | Build | Result |
|------|-------|--------|
| 2026-09-24 | [Material Price Escalation Calculator](builds/2026-09-24) | Sample mid-size remodeling/roofing shop, 15 material-heavy jobs/mo, 9% material price increase, 65% of jobs with no escalation clause: $78,975/yr eaten out of margin, $48,214/yr protectable with a ~1.25% tariff line item |
| 2026-09-23 | [Hiring Delay Cost Calculator](builds/2026-09-23) | Sample mid-size HVAC/plumbing shop, 2 open positions, 56-day avg fill time, 25% covered by overtime: $52,416 total cost of the vacancy ($43,680 lost revenue + $8,736 overtime) |
| 2026-09-17 | [Scope Creep Calculator](builds/2026-09-17) | Sample mid-size plumbing/HVAC shop, 60 jobs/mo, 30% with unbilled extra work: $4,140/mo, $49,680/yr lost to unbilled hours + materials never invoiced |
| 2026-09-16 | [Cash Flow Gap Calculator](builds/2026-09-16) | Sample mid-size plumbing co, $45k/mo GC/insurance revenue, 45-day wait: $66,575 cash trapped, 102.4 jobs' worth, $14,647/yr cost to bridge at 22% APR |
| 2026-09-15 | [BYOM Job Pricing Calculator](builds/2026-09-15) | Sample plumbing/HVAC shop, $650 materials/job, 8 BYOM jobs/mo: $15,600/yr lost charging no fee → $9,360/yr recovered charging the sourced 15% handling fee |
| 2026-09-14 | [Credit Card Processing Fee Calculator](builds/2026-09-14) | Sample business, $30k/mo card volume at 3.2%: $996/mo, $11,952/yr in fees (28% of profit) → $3,960/yr recoverable at 2.1% interchange-plus benchmark |
| 2026-09-13 | [Weather Day / Rain-Out Cost Calculator](builds/2026-09-13) | Sample 5-worker roofing crew, 4 weather days/mo: $3,320/day → $159,360/yr; benchmark crew (labor-only) matched published $30k-$50k/yr industry estimate |
| 2026-09-03 | [Unsold Estimate Recovery Calculator](builds/2026-09-03) | Sample month, 24 quotes: 25% close rate at 0-1 follow-ups vs 50% at 4+ → $3,588 neglected, $1,794 recoverable |
| 2026-09-04 | [Callback & Rework Cost Calculator](builds/2026-09-04) | Sample month, 130 jobs: 8.5% callback rate (red flag, >3%) → $4,938/mo, $59,256/yr cost; $45,250/yr recoverable at 2% benchmark |
| 2026-09-08 | [Technician Turnover Cost Calculator](builds/2026-09-08) | Sample 4-tech shop, 20% turnover, $58k salary → $69,600/yr hidden cost; $41,760/yr recoverable cutting to 8% turnover |
| 2026-09-02 | [True Hourly Rate Calculator](builds/2026-09-02) | Sample solo profile: $28,800/yr overhead, break-even $77.23/hr, recommended $90.86/hr → $34,758/yr left on the table at $65/hr |
| 2026-08-31 | [Emergency Call-Out Fee Calculator](builds/2026-08-31) | 8 sample after-hours calls → $1,772 left on the table at daytime pricing, 158% avg after-hours premium |
| 2026-08-28 | [Double-Booking Checker](builds/2026-08-28) | 16 jobs, 3 techs → 3 conflicts (6 jobs/38% touched), $920 (16%) revenue at risk |
| 2026-08-27 | [Appointment Reminder Generator](builds/2026-08-27) | 12 bookings → 11 (92%) had a reminder due now, $4,655 job value covered |
| 2026-08-26 | [No-Show Predictor](builds/2026-08-26) | 20 booked jobs → 10 (50%) high risk, $4,770 (63% of revenue) at risk |
| 2026-08-25 | [Job Quote & Margin Checker](builds/2026-08-25) | 20 quotes → 6 (30%) underpriced, $201 left on the table |
| 2026-08-24 | [Speed-to-Lead SLA Report](builds/2026-08-24) | 25 leads → 52% answered <5min, 1 never answered, SLA grade F |
| 2026-08-23 | [Missed-Call Revenue Calculator](builds/2026-08-23) | 20 calls → 11 missed (55%), ~$38k/mo lost |

## Structure
```
builds/<date>/   the tool, its files, output.txt, report.html, report.png
posts/<date>.md  the ready-to-post X + LinkedIn content for that build
_template/        report style template
```

Building in public — follow along.
