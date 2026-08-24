#!/usr/bin/env python3
"""
Speed-to-Lead SLA Report
Reads a lead log (when a lead came in, when the business first responded)
and grades response speed against the industry 5-minute benchmark.

Sample data only. No real customer data.
"""
import csv
import sys
from datetime import datetime

FMT = "%Y-%m-%d %H:%M"
NO_RESPONSE_CUTOFF_MIN = 24 * 60  # treat blank / >24h as "no response"


def load_leads(path):
    leads = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            received = datetime.strptime(row["lead_received"].strip(), FMT)
            resp_raw = row["first_response"].strip()
            if resp_raw:
                responded = datetime.strptime(resp_raw, FMT)
                minutes = (responded - received).total_seconds() / 60
            else:
                minutes = None
            leads.append({
                "id": row["lead_id"],
                "source": row["source"],
                "minutes": minutes,
            })
    return leads


def bucket(minutes):
    if minutes is None or minutes > NO_RESPONSE_CUTOFF_MIN:
        return "no_response"
    if minutes <= 5:
        return "under_5"
    if minutes <= 30:
        return "5_to_30"
    if minutes <= 60:
        return "30_to_60"
    return "over_60"


def grade(pct_under_5, pct_no_response):
    if pct_no_response > 0:
        return "F"
    if pct_under_5 >= 80:
        return "A"
    if pct_under_5 >= 60:
        return "B"
    if pct_under_5 >= 40:
        return "C"
    if pct_under_5 >= 20:
        return "D"
    return "F"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "leads.csv"
    leads = load_leads(path)
    total = len(leads)

    buckets = {"under_5": 0, "5_to_30": 0, "30_to_60": 0, "over_60": 0, "no_response": 0}
    responded_minutes = []

    for lead in leads:
        b = bucket(lead["minutes"])
        buckets[b] += 1
        if b != "no_response":
            responded_minutes.append(lead["minutes"])

    responded_count = len(responded_minutes)
    avg_min = sum(responded_minutes) / responded_count if responded_count else 0
    sorted_min = sorted(responded_minutes)
    median_min = (
        sorted_min[responded_count // 2]
        if responded_count % 2 == 1
        else (sorted_min[responded_count // 2 - 1] + sorted_min[responded_count // 2]) / 2
    ) if responded_count else 0

    pct_under_5 = 100 * buckets["under_5"] / total
    pct_no_response = 100 * buckets["no_response"] / total
    sla_grade = grade(pct_under_5, pct_no_response)

    lines = []
    lines.append("SPEED-TO-LEAD SLA REPORT")
    lines.append("=" * 40)
    lines.append(f"Leads analyzed        : {total}")
    lines.append(f"Responded             : {responded_count} ({100*responded_count/total:.0f}%)")
    lines.append(f"No response logged    : {buckets['no_response']} ({pct_no_response:.0f}%)")
    lines.append("")
    lines.append(f"Avg response time     : {avg_min:.1f} min")
    lines.append(f"Median response time  : {median_min:.1f} min")
    lines.append("")
    lines.append("Response speed breakdown:")
    lines.append(f"  Under 5 min  (gold)  : {buckets['under_5']:>2}  ({100*buckets['under_5']/total:.0f}%)")
    lines.append(f"  5-30 min             : {buckets['5_to_30']:>2}  ({100*buckets['5_to_30']/total:.0f}%)")
    lines.append(f"  30-60 min            : {buckets['30_to_60']:>2}  ({100*buckets['30_to_60']/total:.0f}%)")
    lines.append(f"  Over 60 min          : {buckets['over_60']:>2}  ({100*buckets['over_60']/total:.0f}%)")
    lines.append(f"  No response (24h+)   : {buckets['no_response']:>2}  ({pct_no_response:.0f}%)")
    lines.append("")
    lines.append(f"SLA Grade              : {sla_grade}")
    lines.append("")
    lines.append("Benchmark (industry-cited, for context only): leads contacted within")
    lines.append("5 minutes convert far more often than leads contacted later — most")
    lines.append("studies on lead response time put speed-to-lead among the single")
    lines.append("biggest levers on close rate for inbound leads.")

    report = "\n".join(lines)
    print(report)
    with open("output.txt", "w") as f:
        f.write(report + "\n")


if __name__ == "__main__":
    main()
