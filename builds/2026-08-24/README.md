# Speed-to-Lead SLA Report

A tiny tool for home-service businesses that grades how fast they respond to
new leads (Google Ads, website form, Facebook, Yelp, referral) against the
industry-cited 5-minute response benchmark.

**What it does**
- Reads a lead log (when the lead came in, when it was first answered)
- Buckets every lead: under 5 min, 5-30 min, 30-60 min, over 60 min, no response (24h+)
- Computes average and median response time
- Assigns an A-F SLA grade (any unanswered lead automatically caps the grade at F)

**Run**
```bash
python speed_to_lead.py leads.csv
```

**Real run on the sample (`leads.csv`, 25 leads over 3 days)**
```
Leads analyzed        : 25
Responded             : 24 (96%)
No response logged    : 1 (4%)

Avg response time     : 101.9 min
Median response time  : 4.0 min

Response speed breakdown:
  Under 5 min  (gold)  : 13  (52%)
  5-30 min             :  1  (4%)
  30-60 min            :  6  (24%)
  Over 60 min          :  4  (16%)
  No response (24h+)   :  1  (4%)

SLA Grade              : F
```

Sample data only — no real customer data. The median (4 min) tells a
different story than the average (102 min): half the leads were answered
almost instantly, but a handful of slow ones — and one lead that never got a
callback — drag the SLA grade down to an F. That gap between "usually fast"
and "reliably fast" is exactly what AnswerCatch's 24/7 AI receptionist is
built to close, since it never skips a lead.

**Web version:** interactive grader at `/speed-to-lead-tracker/` — plug in
your own leads/month, response mix, and close rates to get your own SLA
grade and a projected monthly job count lost to slow response.
