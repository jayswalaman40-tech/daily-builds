# Build 2026-08-31: Emergency Call-Out Fee Calculator

## Research: what does the demand signal say?

Spent the first part of this run searching what home-service owners are
actually asking about right now (late August — hurricane/storm season,
approaching fall HVAC tune-up season, water heater failures picking up).

Candidates considered:

1. **Hourly rate / overhead calculator** — very common search
   ("how much should I charge per hour 2026"), but already crowded: free
   versions exist from ServiceTitan, House Call Pro, FieldStackPro,
   Intry, build-folio, and others. Not a gap.
2. **Emergency / after-hours call-out fee calculator** — a narrower,
   repeatedly-asked question ("how much to charge for emergency call
   out?" — Contractor Talk forum; multiple blog posts on pricing
   emergency/after-hours plumbing, electrical, and roofing calls fairly
   in 2026). Far fewer free interactive tools exist for this specific
   question, and the "quote it on the phone before the tech shows up"
   problem is a direct match for AnswerCatch's after-hours answering
   pitch. **Picked this one.**
3. **Job costing / change-order calculator** — real pain but harder for
   a non-technical owner to "get" in 30 seconds; parked for a future
   build.

Sources: Contractor Talk forum thread on emergency call-out pricing,
WorkZen "How to Price Emergency Service Calls Without Backlash",
PricingLink after-hours electrical pricing guide, AlertPlumber emergency
plumber cost guide (all pulled via web search this run).

## What it does

Owner picks their normal hourly rate, when the call came in (weekday
day/evening/overnight, weekend day/evening/overnight, or major holiday),
and estimated hours on site. The tool returns:
- a fair dispatch/call-out fee
- a recommended after-hours hourly rate
- the estimated job total
- how much they'd be **underpricing** the job by if they just charged
  their normal daytime rate

Pricing rules are based on 2026 industry-standard after-hours premiums
found in the research above (dispatch fees $75–$275, labor multipliers
1.25x–2.0x depending on the time window).

## Real run — sample dispatch log (8 after-hours calls)

See `output.txt` for the full table. Headline numbers from `build.py`:

- 8 sample after-hours calls logged across a week (burst pipe, no heat,
  AC down, sewer backup, water heater, power outage, gas smell, holiday
  no-heat call)
- Total job revenue if priced right: **$2,895**
- Total left on the table if all 8 were billed at normal daytime rate:
  **$1,772**
- Average recommended after-hours premium: **158%**

## Web tool

Live at `/tools/emergency-fee-calculator/`. Same pricing logic as
`build.py`, implemented in vanilla JS, matching the AnswerCatch site
theme (light, Inter, navy/blue gradient).
