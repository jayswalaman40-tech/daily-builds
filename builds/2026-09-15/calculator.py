#!/usr/bin/env python3
"""
BYOM (Bring-Your-Own-Materials) Job Pricing Calculator
Sample data only — no real business, customer, or job data.

Models the margin a home-service contractor loses when a customer supplies
their own materials and expects a labor-only discount — repeatedly cited as
the single most common complaint on plumbing/HVAC trade forums and
subreddits (customer buys the part online, contractor just "installs it").

markup_lost          = materials_value * (markup_pct / 100)
recommended_fee      = materials_value * (surcharge_pct / 100)
still_left_on_table  = markup_lost - recommended_fee   (per job, even if charged)
fully_uncharged_loss = markup_lost                      (per job, if no fee charged at all)
monthly / annual      = per-job figure * byom_jobs_per_month [* 12]
"""

MARKUP_LOW, MARKUP_HIGH = 15, 35        # sourced typical contractor material markup range
SURCHARGE_LOW, SURCHARGE_HIGH = 15, 20  # sourced typical BYOM handling/risk surcharge range


def byom_math(materials_value, markup_pct, surcharge_pct, byom_jobs_per_month):
    markup_lost = materials_value * (markup_pct / 100)
    recommended_fee = materials_value * (surcharge_pct / 100)
    still_left_on_table = max(0.0, markup_lost - recommended_fee)
    monthly_if_charged = still_left_on_table * byom_jobs_per_month
    monthly_if_not_charged = markup_lost * byom_jobs_per_month
    return {
        "markup_lost": markup_lost,
        "recommended_fee": recommended_fee,
        "still_left_on_table": still_left_on_table,
        "monthly_if_charged": monthly_if_charged,
        "annual_if_charged": monthly_if_charged * 12,
        "monthly_if_not_charged": monthly_if_not_charged,
        "annual_if_not_charged": monthly_if_not_charged * 12,
    }


def fmt(n):
    return "${:,.0f}".format(n)


def run_scenario(title, materials_value, markup_pct, surcharge_pct, byom_jobs_per_month):
    r = byom_math(materials_value, markup_pct, surcharge_pct, byom_jobs_per_month)
    print(f"--- {title} ---")
    print(f"Avg materials value/job if contractor supplied: {fmt(materials_value)} | "
          f"Normal markup: {markup_pct}% | BYOM handling fee charged: {surcharge_pct}% | "
          f"BYOM jobs/mo: {byom_jobs_per_month}")
    print(f"Markup lost per BYOM job (no fee):     {fmt(r['markup_lost'])}")
    print(f"Recommended handling fee per job:      {fmt(r['recommended_fee'])}")
    print(f"Still left on table per job (charged): {fmt(r['still_left_on_table'])}")
    print(f"If NO fee charged  -> per month: {fmt(r['monthly_if_not_charged'])} | per year: {fmt(r['annual_if_not_charged'])}")
    print(f"If fee IS charged  -> per month: {fmt(r['monthly_if_charged'])} | per year: {fmt(r['annual_if_charged'])}")
    print()
    return r


if __name__ == "__main__":
    print("=== BYOM Job Pricing Calculator — sample runs ===")
    print("(Sample business data only — no real customer or job data)\n")

    # Scenario 1: tool defaults — mid-size plumbing/HVAC shop
    s1 = run_scenario(
        "Mid-size plumbing/HVAC shop (tool defaults)",
        materials_value=650, markup_pct=25, surcharge_pct=15, byom_jobs_per_month=8,
    )

    # Scenario 2: solo operator, high-ticket fixture installs, no fee charged at all today
    s2 = run_scenario(
        "Solo operator, high-ticket fixture installs, charging $0 fee today",
        materials_value=1200, markup_pct=30, surcharge_pct=0, byom_jobs_per_month=5,
    )

    # Scenario 3: sanity-check against sourced range — low end of markup, low end of surcharge
    s3 = run_scenario(
        "Benchmark check: low end of sourced ranges (15% markup, 15% surcharge)",
        materials_value=500, markup_pct=MARKUP_LOW, surcharge_pct=SURCHARGE_LOW, byom_jobs_per_month=6,
    )
    # At equal low-end pct (15% markup, 15% surcharge) the fee should fully offset the markup loss
    checks_out = abs(s3["still_left_on_table"]) < 0.01
    print(f"Sanity check — equal 15%/15% (low end of both sourced ranges) should leave $0 on the "
          f"table per job when the fee is charged: {fmt(s3['still_left_on_table'])} -> "
          f"{'MATCHES' if checks_out else 'MISMATCH'}")

    # Recovery framing for scenario 1
    print(f"\nScenario 1 shop (8 BYOM jobs/mo, $650 avg materials value, 25% normal markup): "
          f"charging nothing costs {fmt(s1['annual_if_not_charged'])}/yr in lost margin. "
          f"Charging the sourced 15% handling fee still leaves {fmt(s1['annual_if_charged'])}/yr on "
          f"the table (25%-15% = 10% margin gap) — but recovers "
          f"{fmt(s1['annual_if_not_charged'] - s1['annual_if_charged'])}/yr versus charging nothing.")
