#!/usr/bin/env python3
"""Cash Flow Gap Calculator — sample runs (matches cash-flow-gap-calculator/index.html JS)."""


def calc(monthly_slowpay_revenue, days_waiting, apr_pct, avg_job_value):
    daily_revenue = monthly_slowpay_revenue * 12 / 365
    cash_trapped = daily_revenue * days_waiting
    jobs_worth = cash_trapped / avg_job_value if avg_job_value else 0
    annual_financing_cost = cash_trapped * (apr_pct / 100)
    monthly_financing_cost = annual_financing_cost / 12
    return {
        "daily_revenue": daily_revenue,
        "cash_trapped": cash_trapped,
        "jobs_worth": jobs_worth,
        "annual_financing_cost": annual_financing_cost,
        "monthly_financing_cost": monthly_financing_cost,
    }


SCENARIOS = [
    ("Small HVAC shop — light GC/insurance work", 20000, 30, 22, 500),
    ("Mid-size plumbing co — GC + property mgmt mix (default)", 45000, 45, 22, 650),
    ("Larger contractor — heavy insurance/warranty billing", 90000, 60, 24, 800),
]

if __name__ == "__main__":
    for label, rev, days, apr, job in SCENARIOS:
        r = calc(rev, days, apr, job)
        print(f"--- {label} ---")
        print(f"  Monthly slow-pay revenue: ${rev:,}/mo | Days waiting: {days} | APR: {apr}% | Avg job: ${job}")
        print(f"  Daily revenue:            ${r['daily_revenue']:,.2f}")
        print(f"  Cash trapped right now:   ${r['cash_trapped']:,.0f}")
        print(f"  Jobs' worth of cash tied up: {r['jobs_worth']:,.1f} jobs")
        print(f"  Cost to bridge the gap:   ${r['monthly_financing_cost']:,.0f}/mo  (${r['annual_financing_cost']:,.0f}/yr)")
        print()
