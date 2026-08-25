#!/usr/bin/env python3
"""
Job Quote & Margin Checker
---------------------------
Reads a log of past job quotes (labor, materials, trip fee, what you
actually quoted the customer) and finds the ones priced below your
target profit margin -- money quietly left on the table.

Usage:
    python quote_margin_checker.py quotes.csv [--target 30]
"""
import csv
import sys


def load_quotes(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["labor_hours"] = float(r["labor_hours"])
        r["labor_rate"] = float(r["labor_rate"])
        r["materials_cost"] = float(r["materials_cost"])
        r["trip_fee"] = float(r["trip_fee"])
        r["quoted_price"] = float(r["quoted_price"])
    return rows


def analyze(rows, target_margin_pct):
    total_cost = 0.0
    total_quoted = 0.0
    total_target_price = 0.0
    underpriced = []

    for r in rows:
        cost = r["labor_hours"] * r["labor_rate"] + r["materials_cost"] + r["trip_fee"]
        quoted = r["quoted_price"]
        margin_pct = ((quoted - cost) / quoted * 100) if quoted else 0.0
        target_price = cost / (1 - target_margin_pct / 100)
        gap = max(0.0, target_price - quoted)

        r["cost"] = cost
        r["margin_pct"] = margin_pct
        r["target_price"] = target_price
        r["gap"] = gap

        total_cost += cost
        total_quoted += quoted
        total_target_price += target_price

        if margin_pct < target_margin_pct:
            underpriced.append(r)

    avg_margin = ((total_quoted - total_cost) / total_quoted * 100) if total_quoted else 0.0
    left_on_table = sum(r["gap"] for r in underpriced)

    return {
        "rows": rows,
        "underpriced": underpriced,
        "avg_margin": avg_margin,
        "left_on_table": left_on_table,
        "total_quoted": total_quoted,
        "total_cost": total_cost,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python quote_margin_checker.py quotes.csv [--target 30]")
        sys.exit(1)

    path = sys.argv[1]
    target = 30.0
    if "--target" in sys.argv:
        target = float(sys.argv[sys.argv.index("--target") + 1])

    rows = load_quotes(path)
    result = analyze(rows, target)

    n = len(rows)
    n_under = len(result["underpriced"])

    print(f"Quotes analyzed        : {n}")
    print(f"Target margin          : {target:.0f}%")
    print(f"Average actual margin  : {result['avg_margin']:.1f}%")
    print(f"Quotes below target    : {n_under} ({n_under / n * 100:.0f}%)")
    print(f"$ left on the table     : ${result['left_on_table']:,.0f}  (this batch)")
    print()
    print("Worst-margin jobs (below target):")
    for r in sorted(result["underpriced"], key=lambda r: r["margin_pct"])[:5]:
        print(
            f"  {r['job_id']:5} {r['job_type']:<32} "
            f"margin {r['margin_pct']:5.1f}%  quoted ${r['quoted_price']:,.0f}  "
            f"should be ~${r['target_price']:,.0f}  (short ${r['gap']:,.0f})"
        )

    monthly_jobs_estimate = 40  # a busy solo/small-crew shop, illustrative
    if n_under:
        avg_gap_per_underpriced_job = result["left_on_table"] / n_under
        projected_underpriced_share = n_under / n
        projected_monthly = (
            avg_gap_per_underpriced_job
            * monthly_jobs_estimate
            * projected_underpriced_share
        )
        print()
        print(
            f"Projected monthly leak (~{monthly_jobs_estimate} jobs/mo, "
            f"same underpriced rate): ~${projected_monthly:,.0f}/mo"
        )


if __name__ == "__main__":
    main()
