#!/usr/bin/env python3
"""
2026 Tax Set-Aside Calculator for home-service business owners (sole prop / single-member LLC / 1099).
Real 2026 IRS figures (single-filer & MFJ brackets, standard deduction, SS wage base) via web research 2026-09-26.
Mirrors the JS in tax-set-aside-calculator/index.html exactly.
"""

SS_WAGE_BASE_2026 = 184500
ADDL_MEDICARE_THRESHOLD = {"single": 200000, "mfj": 250000}

BRACKETS = {
    "single": [
        (0, 12400, 0.10),
        (12400, 50400, 0.12),
        (50400, 105700, 0.22),
        (105700, 201775, 0.24),
        (201775, 256225, 0.32),
        (256225, 640600, 0.35),
        (640600, float("inf"), 0.37),
    ],
    "mfj": [
        (0, 24800, 0.10),
        (24800, 100800, 0.12),
        (100800, 211400, 0.22),
        (211400, 403550, 0.24),
        (403550, 512450, 0.32),
        (512450, 768700, 0.35),
        (768700, float("inf"), 0.37),
    ],
}

STANDARD_DEDUCTION = {"single": 16100, "mfj": 32200}

QUARTERLY_DUE_DATES = ["Apr 15, 2026", "Jun 15, 2026", "Sep 15, 2026", "Jan 15, 2027"]


def federal_tax(taxable_income, filing_status):
    tax = 0.0
    for lo, hi, rate in BRACKETS[filing_status]:
        if taxable_income > lo:
            tax += (min(taxable_income, hi) - lo) * rate
        else:
            break
    return tax


def compute(net_profit, filing_status, state_rate_pct, avg_job_revenue=None):
    net_earnings = net_profit * 0.9235

    ss_taxable = min(net_earnings, SS_WAGE_BASE_2026)
    ss_tax = ss_taxable * 0.124
    medicare_tax = net_earnings * 0.029
    addl_medicare = max(0, net_earnings - ADDL_MEDICARE_THRESHOLD[filing_status]) * 0.009
    se_tax = ss_tax + medicare_tax + addl_medicare

    se_tax_deduction = se_tax / 2
    agi = max(0, net_profit - se_tax_deduction)
    taxable_income = max(0, agi - STANDARD_DEDUCTION[filing_status])
    fed_tax = federal_tax(taxable_income, filing_status)

    state_tax = max(0, net_profit) * (state_rate_pct / 100.0)

    total_tax = se_tax + fed_tax + state_tax
    set_aside_pct = (total_tax / net_profit * 100.0) if net_profit > 0 else 0
    quarterly_payment = total_tax / 4.0
    per_job = (avg_job_revenue * (set_aside_pct / 100.0)) if avg_job_revenue else None

    return {
        "net_profit": net_profit,
        "filing_status": filing_status,
        "state_rate_pct": state_rate_pct,
        "se_tax": round(se_tax, 2),
        "federal_tax": round(fed_tax, 2),
        "state_tax": round(state_tax, 2),
        "total_tax": round(total_tax, 2),
        "set_aside_pct": round(set_aside_pct, 2),
        "quarterly_payment": round(quarterly_payment, 2),
        "per_job_setaside": round(per_job, 2) if per_job is not None else None,
        "quarterly_due_dates": QUARTERLY_DUE_DATES,
    }


if __name__ == "__main__":
    samples = [
        {"label": "Solo plumber, sole prop, single, no state tax, $450 avg job",
         "net_profit": 95000, "filing_status": "single", "state_rate_pct": 0, "avg_job_revenue": 450},
        {"label": "3-tech HVAC shop owner, single-member LLC, single, 5% state tax, $650 avg job",
         "net_profit": 180000, "filing_status": "single", "state_rate_pct": 5, "avg_job_revenue": 650},
        {"label": "Married electrician, MFJ, 4.5% state tax, $500 avg job",
         "net_profit": 130000, "filing_status": "mfj", "state_rate_pct": 4.5, "avg_job_revenue": 500},
    ]
    for s in samples:
        r = compute(s["net_profit"], s["filing_status"], s["state_rate_pct"], s["avg_job_revenue"])
        print("=" * 70)
        print(s["label"])
        for k, v in r.items():
            print(f"  {k}: {v}")
