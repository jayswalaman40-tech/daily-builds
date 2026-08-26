# No-Show Predictor

A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers)
that scores booked appointments for no-show risk using booking-time signals,
then tallies how much job revenue is sitting at risk this week.

## Signals used
- Hours' notice given for the booking (short notice = higher risk)
- Confirmation status (unconfirmed = higher risk)
- This customer's prior no-show count (repeat offenders = higher risk)
- Day of week (Fri/Sat carry a small bump — weekend plans compete)

Each appointment gets a 0-100 risk score and a tier: Low / Medium / High.

## Run it
```
python3 no_show_predictor.py
```
Reads `sample_appointments.csv` (20 sample bookings, no real customer data),
writes `output.txt`.

## Real result from this run
- 20 jobs scanned, $7,625 total booked revenue
- **10 jobs (50%) scored High risk — $4,770 (63% of revenue) at risk**
- 0 Medium, 10 Low
- Highest-risk jobs: short notice (1-4h) + unconfirmed + repeat no-show history

## Web version
Live, interactive version (sliders + instant score) at:
https://answercatch.com/tools/no-show-predictor/

Source: `../../no-show-predictor/index.html`

## Files
- `no_show_predictor.py` — the scoring script
- `sample_appointments.csv` — sample input (20 rows, fake data)
- `output.txt` — real output from running the script
- `screenshot.png` — screenshot of the live web tool
