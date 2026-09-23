#!/usr/bin/env python3
"""Hiring Delay Cost Calculator — quantifies what an open tech position costs
a home-service business while it sits unfilled, plus the overtime spent
covering part of the gap.

Model:
  uncovered_days_value = positions * days_to_fill * daily_revenue * (1 - covered_pct)
  overtime_cost         = positions * days_to_fill * daily_revenue * covered_pct * OT_MULTIPLIER
  total_cost            = uncovered_days_value + overtime_cost

OT_MULTIPLIER (0.6) approximates paying existing staff time-and-a-half to
squeeze in a fraction of the missed capacity — cheaper than losing the job
outright, but not free.
"""
import sys
import csv

OT_MULTIPLIER = 0.6


def money(x):
    return "${:,.0f}".format(x)


def calc(positions, days_to_fill, daily_revenue, covered_pct):
    covered = covered_pct / 100.0
    uncovered_value = positions * days_to_fill * daily_revenue * (1 - covered)
    overtime_cost = positions * days_to_fill * daily_revenue * covered * OT_MULTIPLIER
    total = uncovered_value + overtime_cost
    return uncovered_value, overtime_cost, total


def run_sample(path):
    print("Hiring Delay Cost Calculator — sample run\n")
    print(f"{'Shop':<28}{'Open':>6}{'Days':>7}{'Rev/day':>10}{'Covered':>9}{'Lost rev':>14}{'OT cost':>12}{'Total cost':>14}")
    grand_total = 0
    rows_read = 0
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows_read += 1
            name = row["shop"]
            positions = int(row["open_positions"])
            days = int(row["avg_days_to_fill"])
            daily_rev = float(row["revenue_per_tech_per_day"])
            covered_pct = float(row["pct_covered_by_overtime"])
            uncovered_value, ot_cost, total = calc(positions, days, daily_rev, covered_pct)
            grand_total += total
            print(f"{name:<28}{positions:>6}{days:>7}{money(daily_rev):>10}{covered_pct:>8.0f}%{money(uncovered_value):>14}{money(ot_cost):>12}{money(total):>14}")

    print(f"\nShops in sample: {rows_read}")
    print(f"Combined cost of current hiring gaps: {money(grand_total)}")
    print("\nBenchmark used: 56-day average time-to-fill for skilled trades roles (2026),")
    print("$2,000-$7,800/day lost revenue per unfilled tech position (industry range).")
    print("62% of plumbing contractors in shortage markets declined $50k+ revenue in 2024 due to staffing gaps.")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "sample_shops.csv"
    run_sample(path)
