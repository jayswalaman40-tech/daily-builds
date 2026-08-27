# Appointment Reminder Generator

A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers)
that scans today's booked jobs and writes the exact SMS reminder text that's
due right now — at the 24-hour and 2-hour windows before the appointment.

## How it works
- Each booking carries an hours-until-appointment value.
- If a job falls in the 22-26h window, it gets the "tomorrow" reminder.
- If a job falls in the 0.5-3.5h window, it gets the "we're on our way" reminder.
- Everything else is skipped — no reminder needed yet.

## Run it
```
python3 reminder_generator.py
```
Runs on 12 sample bookings (no real customer data), writes `output.txt` and
`summary.json`.

## Real result from this run
- 12 sample bookings, $4,865 total booked job value
- **11 of 12 (92%) had a reminder due right now** — 5 at the 24h window, 6 at the 2h window
- $4,655 of job value covered by those reminders
- [Projected] using a commonly cited 18% baseline no-show rate and a 30%
  reduction from consistent reminders: ~0.6 no-shows avoided, ~$263 in job
  value protected on this batch (a projection, not a measured client result)

## Web version
Live, interactive version (add your own jobs, get the reminder text instantly) at:
https://answercatch.com/tools/appointment-reminder/

Source: `../../appointment-reminder/index.html`

## Files
- `reminder_generator.py` — the reminder-generation script
- `output.txt` — real console output from running the script
- `summary.json` — the same run's numbers as structured data
- `screenshot.png` — screenshot of the live web tool
