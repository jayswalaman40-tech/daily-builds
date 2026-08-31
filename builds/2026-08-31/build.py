#!/usr/bin/env python3
"""Emergency / After-Hours Call-Out Fee Calculator - sample run.

Logic mirrors the web tool: given a normal hourly rate and when the call
comes in, recommend a dispatch (call-out) fee and a labor rate multiplier,
based on published 2026 industry norms for plumbing/HVAC/electrical
after-hours pricing (see builds/2026-08-31/README.md for sources).
"""

TIME_BUCKETS = [
    # key,                 label,                              dispatch_fee, labor_mult
    ("weekday_day",        "Weekday, 8am-5pm",                 0,   1.00),
    ("weekday_evening",    "Weekday, 5pm-9pm",                 75,  1.25),
    ("weekday_overnight",  "Weekday, 9pm-8am",                 175, 1.60),
    ("weekend_day",        "Weekend, 8am-5pm",                 100, 1.40),
    ("weekend_evening",    "Weekend, 5pm-9pm",                 150, 1.60),
    ("weekend_overnight",  "Weekend, 9pm-8am",                 200, 1.75),
    ("holiday",            "Major holiday, any time",          275, 2.00),
]

def recommend(base_rate, bucket_key, est_hours=1.5):
    bucket = next(b for b in TIME_BUCKETS if b[0] == bucket_key)
    _, label, dispatch_fee, labor_mult = bucket
    after_hours_rate = round(base_rate * labor_mult)
    labor_total = round(after_hours_rate * est_hours)
    job_total = dispatch_fee + labor_total
    normal_labor_total = round(base_rate * est_hours)
    normal_total = normal_labor_total  # no dispatch fee assumed baseline
    premium_dollars = job_total - normal_total
    premium_pct = round((premium_dollars / normal_total) * 100) if normal_total else 0
    return {
        "window": label,
        "dispatch_fee": dispatch_fee,
        "after_hours_rate": after_hours_rate,
        "est_hours": est_hours,
        "job_total": job_total,
        "normal_total": normal_total,
        "premium_dollars": premium_dollars,
        "premium_pct": premium_pct,
    }

if __name__ == "__main__":
    # Sample dispatch log: 8 real-shaped after-hours calls a home-service
    # business might log in a week (base rate + when the call came in).
    sample_calls = [
        ("Burst pipe - Sat 11pm",        95, "weekend_overnight"),
        ("No heat - Sun 7am",            90, "weekend_day"),
        ("AC down - Tue 6:30pm",         95, "weekday_evening"),
        ("Sewer backup - Wed 2am",       95, "weekday_overnight"),
        ("Water heater - Fri 8pm",       90, "weekday_evening"),
        ("Power outage - Sat 3pm",       100, "weekend_day"),
        ("Gas smell - Thu 10:15pm",      95, "weekday_overnight"),
        ("No heat - Thanksgiving Day",   90, "holiday"),
    ]

    lines = []
    lines.append(f"{'Call':32} {'Window':22} {'Dispatch':>9} {'Rate/hr':>8} {'Job total':>10} {'vs normal':>10}")
    lines.append("-" * 96)
    total_premium = 0
    total_normal = 0
    total_job = 0
    for name, rate, bucket in sample_calls:
        r = recommend(rate, bucket)
        lines.append(
            f"{name:32} {r['window']:22} ${r['dispatch_fee']:>7} ${r['after_hours_rate']:>6}/hr "
            f"${r['job_total']:>8} +{r['premium_pct']:>3}%"
        )
        total_premium += r["premium_dollars"]
        total_normal += r["normal_total"]
        total_job += r["job_total"]

    avg_premium_pct = round((total_premium / total_normal) * 100) if total_normal else 0

    lines.append("-" * 96)
    lines.append(f"Calls logged: {len(sample_calls)}")
    lines.append(f"Total job revenue if priced right: ${total_job:,}")
    lines.append(f"Total left on the table if all charged at normal daytime rate: ${total_premium:,}")
    lines.append(f"Average after-hours premium recommended: {avg_premium_pct}%")

    out = "\n".join(lines)
    print(out)
    with open("output.txt", "w") as f:
        f.write(out + "\n")
