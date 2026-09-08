#!/usr/bin/env python3
"""
Technician Turnover Cost Calculator - sample run on realistic (non-customer) data.

Research-backed assumptions used below (see README.md for sources):
- Trade turnover rates run 12%-21% depending on trade (ServiceTitan "State of the Trades").
- Replacing a service tech costs 0.5x-2x their annual salary once lost productivity,
  team disruption, recruiting and training-to-full-productivity are counted
  (Wrenchway / Applause HQ industry data).
"""

def turnover_cost(num_techs, avg_salary, turnover_rate_pct, replace_multiplier):
    techs_lost_per_year = num_techs * (turnover_rate_pct / 100)
    cost_per_lost_tech = avg_salary * replace_multiplier
    annual_cost = techs_lost_per_year * cost_per_lost_tech
    monthly_cost = annual_cost / 12
    return techs_lost_per_year, cost_per_lost_tech, annual_cost, monthly_cost


def fmt(x):
    return "${:,.0f}".format(x)


def run_case(label, num_techs, avg_salary, turnover_rate_pct, replace_multiplier):
    lost, cost_each, annual, monthly = turnover_cost(
        num_techs, avg_salary, turnover_rate_pct, replace_multiplier
    )
    print(f"--- {label} ---")
    print(f"Technicians on staff:        {num_techs}")
    print(f"Average annual salary:       {fmt(avg_salary)}")
    print(f"Annual turnover rate:        {turnover_rate_pct}%")
    print(f"Replacement cost multiplier: {replace_multiplier}x salary")
    print(f"Techs lost per year:         {lost:.1f}")
    print(f"Cost per lost tech:          {fmt(cost_each)}")
    print(f"Monthly cost of turnover:    {fmt(monthly)}")
    print(f"Annual cost of turnover:     {fmt(annual)}")
    print()
    return annual


if __name__ == "__main__":
    print("=" * 60)
    print("TECHNICIAN TURNOVER COST CALCULATOR - sample run")
    print("Sample data only. No real employee or customer data.")
    print("=" * 60)
    print()

    # Case 1: small home-service shop (AnswerCatch's core audience) - matches
    # the 4-tech shop used in the 2026-09-04 callback-cost-calculator sample.
    small = run_case(
        "Small shop (4 techs)",
        num_techs=4,
        avg_salary=58000,
        turnover_rate_pct=20,
        replace_multiplier=1.5,
    )

    # Case 2: mid-size shop at the blended industry turnover rate (17.5%),
    # replicating the ServiceTitan/Wrenchway benchmark scenario for sanity-check.
    mid = run_case(
        "Mid-size shop (20 techs, industry-benchmark 17.5% turnover)",
        num_techs=20,
        avg_salary=55000,
        turnover_rate_pct=17.5,
        replace_multiplier=1.0,
    )

    # Case 3: same small shop, but if it cut turnover to a strong-retention 8%
    small_low = run_case(
        "Small shop (4 techs) at strong-retention 8% turnover",
        num_techs=4,
        avg_salary=58000,
        turnover_rate_pct=8,
        replace_multiplier=1.5,
    )

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Small 4-tech shop, 20% turnover -> {fmt(small)}/year hidden cost")
    print(f"Same shop at 8% turnover        -> {fmt(small_low)}/year hidden cost")
    print(f"Recoverable by cutting turnover  -> {fmt(small - small_low)}/year")
    print(f"20-tech shop at 17.5% (benchmark)-> {fmt(mid)}/year hidden cost")
