# 2026-09-25 — Overtime Cost Calculator

## Research

Checked `<slug>/` folders + `posts/` first — 49 tools already live, none covering
overtime/OT premium cost specifically (closest are `true-rate-calculator`, which
computes break-even hourly rate, and `hiring-delay-calculator`/`turnover-cost-calculator`,
which cover an *open* position and *losing* a tech — not the cost of covering gaps
with overtime instead of hiring).

Searched trade-forum and industry-report signals on labor cost pain points for home-service
owners in 2026:

- **Technician shortage → OT becomes the default fix.** HVAC alone has 110,000+
  unfilled positions nationally; labor shortages are pushing fully-loaded technician
  costs to levels most price books haven't caught up to. Shops cover the gap by
  running existing crews longer instead of hiring. ([Bella FSM 2026 Field Service
  Report](https://www.bellafsm.com/state-of-small-field-service-businesses-2026/),
  [PipelineOn HVAC job costing](https://pipelineon.com/blog/hvac-job-costing/))
- **The legal floor on OT pay.** FLSA requires time-and-a-half past 40 hrs/week;
  many shops pay double time for nights/weekends/holidays, and several states count
  restricted on-call time as compensable hours worked. Industry practice for
  after-hours dispatch: ~1.5x weeknight, ~2x weekend, 2.5-3x holiday.
  ([FixyFlow after-hours pricing guide](https://fixyflow.com/blog/after-hours-service-pricing-2026),
  [Bella FSM after-hours plumbing rotation](https://www.bellafsm.com/after-hours-plumbing-calls/))
- **Fully-loaded labor cost benchmark.** A technician's base wage typically carries
  a 25-45% burden (payroll tax, workers' comp, benefits, PTO) before overhead — most
  service contractors land in the 30-55% range, smaller shops 25-30%.
  ([SubcontractorHub labor burden calculator](https://www.subcontractorhub.com/tools/contractor-labor-burden-calculator),
  [PushLeads burdened labor rate guide](https://pushleads.com/job-costing-for-service-contractors/how-to-calculate-your-burdened-labor-rate/))
- **56% of small service businesses** are also carrying unpaid AR (avg $17,500)
  and 34% cite weather/seasonality as their top growth blocker — both already have
  dedicated tools on the site (`cash-flow-gap-calculator`, `weather-day-calculator`),
  so overtime was the strongest *not-yet-built* angle with solid, current sourcing.

**Decision:** build a calculator that turns "we've just been asking the crew to
stay late" into a real annual number, and stacks it against the fully-loaded cost
of hiring one more tech — a comparison none of the 49 existing tools makes.

## What it does

Inputs: techs regularly working OT, avg OT hours/week per tech, regular hourly
rate, OT multiplier (1.5x-2.5x, covering time-and-a-half through holiday rates).

Outputs: OT premium cost per week, OT premium cost per year (the pure markup over
straight time), total spent on those OT hours per year, and a comparison line
against a fully-loaded new hire (base rate x 1.35 burden x 2,000 regular hrs/yr —
the 35% burden and 40hr/50wk-year are both standard industry rules of thumb, cited
in the footer).

## Sample run (see `output.txt` / `calc.py`)

4 techs, 8 OT hrs/week each, $28/hr, 1.5x (time-and-a-half):
- OT premium: **$448/week, $22,400/year** (pure markup, on top of straight-time pay)
- Total spent on those OT hours: **$67,200/year**
- Fully-loaded cost of one new hire: **$75,600/year**
- Gap: the shop is already spending within **$8,400** of a full new hire's salary —
  just to cover 32 hrs/week of overflow with existing staff.

Sensitivity checks: same shop at 2x (weekend rate) pushes total OT spend to
$89,600/yr — $14,000 *more* than a new hire. A smaller 2-tech shop at 5 OT hrs/week
each stays well under the hiring threshold ($24,000 OT vs $86,400 new-hire cost),
showing the tool scales sensibly with shop size.

## Files

- `calc.py` / `output.txt` — sample calculation, verified to match the web tool's JS exactly
- `screenshot.png` — live tool screenshot
- `../../overtime-cost-calculator/index.html` — the live web tool
