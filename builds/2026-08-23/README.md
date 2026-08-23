# Missed-Call Revenue Calculator

A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers)
that estimates the revenue leaking out through missed calls.

**What it does**
- Reads a call log (answered vs missed, after-hours flag)
- Counts missed + after-hours-missed calls
- Estimates lost revenue = missed × close rate × average job value
- Projects a monthly figure

**Run**
```bash
python missed_call_calculator.py calls.csv
```

**Real run on the sample (`calls.csv`, 20 calls)**
```
Calls in sample     : 20
Answered            : 9
Missed              : 11  (55% of calls)
  ...of which after-hours: 5
Lost revenue (this sample): $1,732
Projected lost / month    : $38,115
```

Assumptions: avg job $450, close rate 35% (tweak per trade). Sample data only —
no real customer data. This is exactly the leak AnswerCatch's 24/7 AI receptionist
is built to plug.
