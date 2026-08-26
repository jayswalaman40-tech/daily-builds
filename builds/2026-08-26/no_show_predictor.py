"""
No-Show Predictor
------------------
Scores upcoming home-service appointments for no-show risk using
booking-time signals (notice window, confirmation status, prior
no-show history, weekend vs weekday), then reports how much job
revenue is sitting at high risk this week.

Sample data only. No real customer data.
"""

import csv

INPUT_FILE = "sample_appointments.csv"
OUTPUT_FILE = "output.txt"

HIGH_RISK_DAYS = {"Fri", "Sat"}


def risk_score(row):
    score = 10  # base risk every appointment carries

    hours_notice = float(row["hours_notice"])
    if hours_notice < 6:
        score += 35
    elif hours_notice < 24:
        score += 20
    elif hours_notice < 48:
        score += 8

    if row["confirmed"].strip().lower() != "yes":
        score += 25

    prior = int(row["prior_no_shows"])
    score += min(prior, 3) * 12

    if row["day_of_week"] in HIGH_RISK_DAYS:
        score += 8

    return min(score, 100)


def tier(score):
    if score >= 60:
        return "High"
    if score >= 35:
        return "Medium"
    return "Low"


def main():
    rows = []
    with open(INPUT_FILE, newline="") as f:
        for row in csv.DictReader(f):
            row["risk_score"] = risk_score(row)
            row["tier"] = tier(row["risk_score"])
            row["job_value"] = float(row["job_value"])
            rows.append(row)

    rows.sort(key=lambda r: r["risk_score"], reverse=True)

    total_jobs = len(rows)
    high = [r for r in rows if r["tier"] == "High"]
    medium = [r for r in rows if r["tier"] == "Medium"]
    low = [r for r in rows if r["tier"] == "Low"]

    revenue_at_risk_high = sum(r["job_value"] for r in high)
    revenue_at_risk_medium = sum(r["job_value"] for r in medium)
    total_revenue = sum(r["job_value"] for r in rows)

    lines = []
    lines.append("NO-SHOW PREDICTOR — this week's booked jobs")
    lines.append("=" * 52)
    lines.append(f"Jobs scanned: {total_jobs}")
    lines.append(f"Total booked revenue: ${total_revenue:,.0f}")
    lines.append("")
    lines.append(f"High risk:   {len(high)} jobs  (${revenue_at_risk_high:,.0f} at risk)")
    lines.append(f"Medium risk: {len(medium)} jobs  (${revenue_at_risk_medium:,.0f} at risk)")
    lines.append(f"Low risk:    {len(low)} jobs")
    lines.append("")
    pct_high = (len(high) / total_jobs) * 100
    pct_rev_high = (revenue_at_risk_high / total_revenue) * 100
    lines.append(f"-> {pct_high:.0f}% of this week's jobs are high no-show risk,")
    lines.append(f"   representing {pct_rev_high:.0f}% of booked revenue (${revenue_at_risk_high:,.0f}).")
    lines.append("")
    lines.append("Top 5 highest-risk appointments:")
    lines.append(f"{'Job':<6}{'Customer':<16}{'Day':<5}{'Notice':<9}{'Confirmed':<11}{'PriorNS':<9}{'Score':<7}{'Value':<9}")
    for r in rows[:5]:
        lines.append(
            f"{r['job_id']:<6}{r['customer']:<16}{r['day_of_week']:<5}"
            f"{r['hours_notice']+'h':<9}{r['confirmed']:<11}{r['prior_no_shows']:<9}"
            f"{r['risk_score']:<7}${r['job_value']:.0f}"
        )
    lines.append("")
    lines.append("Recommendation: send a confirmation text 24h before + a same-day")
    lines.append("reminder to every High-risk job. That's the cheapest lever that")
    lines.append("moves a no-show back into a kept appointment.")

    report = "\n".join(lines)
    print(report)
    with open(OUTPUT_FILE, "w") as f:
        f.write(report + "\n")


if __name__ == "__main__":
    main()
