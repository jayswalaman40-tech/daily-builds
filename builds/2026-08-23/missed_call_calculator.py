#!/usr/bin/env python3
"""
Missed-Call Revenue Calculator (for home-service businesses)
------------------------------------------------------------
Home-service pros (plumbers, HVAC, electricians, roofers) miss calls while
they're on a job or after hours. Every missed call is a job that can go to a
competitor. This reads a call log and estimates the revenue leaking out.

Input CSV columns: timestamp, status (answered|missed), after_hours (yes|no)
Output: a real breakdown + estimated lost revenue.

Pure Python standard library. Sample data only, no real customer data.
Usage:  python missed_call_calculator.py calls.csv
"""
import csv
import sys

# Conservative home-service assumptions (tweak per trade)
AVG_JOB_VALUE = 450.0   # avg ticket for a booked job (USD)
CLOSE_RATE = 0.35       # share of answered new-lead calls that become jobs
WORKING_DAYS = 22       # to project a monthly figure from the sample


def money(x):
    return "${:,.0f}".format(x)


def main(src):
    total = answered = missed = missed_after_hours = 0
    with open(src, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += 1
            status = row.get("status", "").strip().lower()
            after = row.get("after_hours", "").strip().lower() in ("yes", "y", "true", "1")
            if status == "answered":
                answered += 1
            elif status == "missed":
                missed += 1
                if after:
                    missed_after_hours += 1

    # A missed call = a lost booking opportunity at the same close rate.
    lost_per_day = missed * CLOSE_RATE * AVG_JOB_VALUE
    lost_per_month = lost_per_day * WORKING_DAYS
    miss_rate = round(100 * missed / total) if total else 0

    print("Missed-Call Revenue Calculator")
    print("-" * 34)
    print("Calls in sample     : {}".format(total))
    print("Answered            : {}".format(answered))
    print("Missed              : {}  ({}% of calls)".format(missed, miss_rate))
    print("  ...of which after-hours: {}".format(missed_after_hours))
    print("-" * 34)
    print("Assumptions: avg job {}, close rate {:.0f}%".format(money(AVG_JOB_VALUE), CLOSE_RATE * 100))
    print("Lost revenue (this sample): {}".format(money(lost_per_day)))
    print("Projected lost / month    : {}".format(money(lost_per_month)))
    print("-" * 34)
    print("A 24/7 receptionist that answers every call recovers most of this.")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "calls.csv"
    main(src)
