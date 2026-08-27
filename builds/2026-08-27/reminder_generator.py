#!/usr/bin/env python3
"""
Appointment Reminder Generator
-------------------------------
For a home-service business (plumber, HVAC, electrician, roofer...), takes a
day's booked appointments and generates the SMS reminder text that should go
out right now, at two intervals: 24h-before and 2h-before the job.

Sending a reminder at both windows is a well-documented way service
businesses cut no-shows -- this tool just automates writing (and timing) the
text so nobody has to remember to do it by hand.

Sample data only. No real customer data, no messages actually sent.
"""

import json
from datetime import datetime, timedelta

BUSINESS_NAME = "Rivera Plumbing Co."
BUSINESS_PHONE = "(555) 019-2288"

# Industry-cited range for confirmed no-show reduction when a business adds a
# structured reminder sequence (vs. no reminder at all). We use the
# conservative end and label it clearly as a projection, not a measured result.
PROJECTED_NOSHOW_REDUCTION = 0.30  # 30%, conservative end of commonly cited 30-40% range
BASELINE_NOSHOW_RATE = 0.18        # commonly cited baseline for unconfirmed home-service bookings

SAMPLE_APPOINTMENTS = [
    {"name": "D. Alvarez",  "service": "Drain cleaning",     "hours_until": 24.2, "job_value": 220},
    {"name": "M. Chen",     "service": "Water heater repair", "hours_until": 23.6, "job_value": 480},
    {"name": "K. Brooks",   "service": "Leak inspection",     "hours_until": 2.3,  "job_value": 190},
    {"name": "T. Nguyen",   "service": "Pipe replacement",    "hours_until": 1.8,  "job_value": 650},
    {"name": "S. Patel",    "service": "Faucet install",      "hours_until": 47.5, "job_value": 210},
    {"name": "J. Romero",   "service": "Sump pump service",   "hours_until": 24.9, "job_value": 340},
    {"name": "L. Foster",   "service": "Drain cleaning",      "hours_until": 2.0,  "job_value": 220},
    {"name": "A. Kim",      "service": "Water heater install","hours_until": 0.7,  "job_value": 1450},
    {"name": "R. Diaz",     "service": "Toilet repair",       "hours_until": 26.0, "job_value": 160},
    {"name": "B. Walsh",    "service": "Leak inspection",     "hours_until": 3.4,  "job_value": 190},
    {"name": "C. Nolan",    "service": "Gas line check",      "hours_until": 22.5, "job_value": 275},
    {"name": "P. Osei",     "service": "Water heater repair", "hours_until": 1.2,  "job_value": 480},
]

WINDOWS = [
    {"key": "24h", "low": 22.0, "high": 26.0,
     "template": "Hi {first}, this is {business}, reminding you: your {service} appointment is tomorrow. "
                  "Reply Y to confirm or call {phone} to reschedule."},
    {"key": "2h", "low": 0.5, "high": 3.5,
     "template": "Hi {first}, {business} here -- we're on our way for your {service} today, "
                  "arriving in about {hours}h. Reply if anything's changed!"},
]


def first_name(full_name):
    return full_name.split(".")[-1].strip() if "." in full_name else full_name.split()[0]


def due_window(hours_until):
    for w in WINDOWS:
        if w["low"] <= hours_until <= w["high"]:
            return w
    return None


def build_message(appt, window):
    return window["template"].format(
        first=first_name(appt["name"]),
        business=BUSINESS_NAME,
        service=appt["service"].lower(),
        phone=BUSINESS_PHONE,
        hours=round(appt["hours_until"], 1),
    )


def run():
    due_now = []
    not_due = []
    for appt in SAMPLE_APPOINTMENTS:
        window = due_window(appt["hours_until"])
        if window:
            due_now.append({**appt, "window": window["key"], "message": build_message(appt, window)})
        else:
            not_due.append(appt)

    total_appts = len(SAMPLE_APPOINTMENTS)
    reminders_due = len(due_now)
    total_job_value = sum(a["job_value"] for a in SAMPLE_APPOINTMENTS)
    value_covered_by_reminders = sum(a["job_value"] for a in due_now)

    projected_noshows_avoided = round(total_appts * BASELINE_NOSHOW_RATE * PROJECTED_NOSHOW_REDUCTION, 1)
    projected_value_protected = round(total_job_value * BASELINE_NOSHOW_RATE * PROJECTED_NOSHOW_REDUCTION)

    lines = []
    lines.append("=== Appointment Reminder Generator ===")
    lines.append(f"Business: {BUSINESS_NAME}")
    lines.append(f"Run time: sample batch (not wall-clock; hours_until is pre-set per appointment)")
    lines.append("")
    lines.append(f"Appointments in batch: {total_appts}")
    lines.append(f"Reminders due right now: {reminders_due} ({round(100*reminders_due/total_appts)}%)")
    lines.append(f"  - 24h-window reminders: {sum(1 for a in due_now if a['window']=='24h')}")
    lines.append(f"  - 2h-window reminders:  {sum(1 for a in due_now if a['window']=='2h')}")
    lines.append(f"Booked job value in this batch: ${total_job_value:,}")
    lines.append(f"Job value covered by today's reminders: ${value_covered_by_reminders:,}")
    lines.append("")
    lines.append(f"[PROJECTED] Using a {int(BASELINE_NOSHOW_RATE*100)}% baseline no-show rate and a "
                  f"{int(PROJECTED_NOSHOW_REDUCTION*100)}% reduction from consistent reminders:")
    lines.append(f"[PROJECTED]   ~{projected_noshows_avoided} no-shows avoided across this batch")
    lines.append(f"[PROJECTED]   ~${projected_value_protected:,} in job value protected")
    lines.append("(Projections only -- based on commonly cited industry ranges, not a measured client result.)")
    lines.append("")
    lines.append("--- Messages generated right now ---")
    for a in due_now:
        lines.append(f"[{a['window']} | {a['name']} | {a['service']} | ${a['job_value']}]")
        lines.append(f"  \"{a['message']}\"")
    lines.append("")
    lines.append(f"--- Not due yet ({len(not_due)}) ---")
    for a in not_due:
        lines.append(f"  {a['name']} — {a['service']} — {round(a['hours_until'],1)}h out, no reminder window hit")

    output = "\n".join(lines)
    print(output)

    with open("output.txt", "w") as f:
        f.write(output + "\n")

    summary = {
        "total_appointments": total_appts,
        "reminders_due_now": reminders_due,
        "reminders_pct": round(100 * reminders_due / total_appts, 1),
        "total_job_value": total_job_value,
        "value_covered_by_reminders": value_covered_by_reminders,
        "projected_noshow_reduction_pct": int(PROJECTED_NOSHOW_REDUCTION * 100),
        "projected_noshows_avoided": projected_noshows_avoided,
        "projected_value_protected": projected_value_protected,
    }
    with open("summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    return summary


if __name__ == "__main__":
    run()
