# Double-Booking Checker

A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers,
landscapers) that scans a day's booked jobs per technician and flags any two
jobs that overlap on the calendar — including the drive-time/reset buffer
between them.

Live tool: https://answercatch.com/tools/double-booking-checker/

## What it does

Given a list of jobs (tech, customer, start time, duration, job value), it
checks — per technician — whether any job starts before the previous job
(plus a configurable drive/reset buffer) actually finishes. Two jobs
overlapping on one tech's calendar means a truck can't physically be in two
places on time.

## Python demo (`double_booking_checker.py`)

Runs against a sample 3-tech, 16-job day (plumbing/HVAC-style business) with
a 15-minute drive buffer between jobs. Real output from this run:

```
Techs scheduled today: 3
Jobs booked today: 16
Total booked job value: $5,815

CONFLICTS FOUND: 3
- Mike: R. Alvarez (8:00AM-9:30AM) overlaps T. Nguyen (9:00AM-10:00AM) by 45 min
- Sarah: L. Chen (11:00AM-12:00PM) overlaps B. Foster (11:45AM-1:15PM) by 30 min
- Sarah: A. Grant (4:00PM-5:00PM) overlaps J. Ibarra (4:15PM-5:15PM) by 60 min

Jobs touched by a conflict: 6 of 16 (38%)
Revenue riding on the at-risk (later) jobs: $920
Share of today's booked value at risk: 16%
```

Full output saved in `output.txt`.

## Web version

`double-booking-checker/index.html` (repo root) — a self-contained,
mobile-responsive, interactive tool. Enter each job's tech, start time,
duration and value in an editable table, set the drive/reset buffer with a
slider, and it checks every tech's schedule live in the browser, highlighting
any overlapping rows and totaling the revenue at risk. No backend, no
external libraries.

Sample data only — no real customer data.
