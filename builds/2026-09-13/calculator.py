#!/usr/bin/env python3
"""
Weather Day / Rain-Out Cost Calculator
Sample data only — no real customer or crew data.

Models the hidden cost of a weather day for outdoor trades (roofing,
landscaping, exterior HVAC/solar install crews): idle labor cost (crew
still paid or still costs you the day) + the revenue that would have
been billed that day but wasn't.

cost_per_day  = (crew_size * hourly_wage * hours_per_day) + revenue_lost_per_day
cost_per_month = cost_per_day * weather_days_per_month
cost_per_year  = cost_per_month * 12
"""

HOURS_PER_DAY = 8


def weather_day_cost(crew_size, hourly_wage, weather_days_per_month, revenue_lost_per_day):
    labor_cost_per_day = crew_size * hourly_wage * HOURS_PER_DAY
    cost_per_day = labor_cost_per_day + revenue_lost_per_day
    cost_per_month = cost_per_day * weather_days_per_month
    cost_per_year = cost_per_month * 12
    return {
        "labor_cost_per_day": labor_cost_per_day,
        "cost_per_day": cost_per_day,
        "cost_per_month": cost_per_month,
        "cost_per_year": cost_per_year,
    }


def fmt(n):
    return "${:,.0f}".format(n)


def run_scenario(title, crew_size, hourly_wage, weather_days_per_month, revenue_lost_per_day):
    r = weather_day_cost(crew_size, hourly_wage, weather_days_per_month, revenue_lost_per_day)
    print(f"--- {title} ---")
    print(f"Crew size: {crew_size} workers | Wage: ${hourly_wage}/hr | "
          f"Weather days/month: {weather_days_per_month} | Revenue lost/day: {fmt(revenue_lost_per_day)}")
    print(f"Idle labor cost per weather day: {fmt(r['labor_cost_per_day'])}")
    print(f"Total cost per weather day:      {fmt(r['cost_per_day'])}")
    print(f"Cost per month:                  {fmt(r['cost_per_month'])}")
    print(f"Cost per year:                   {fmt(r['cost_per_year'])}")
    print()
    return r


if __name__ == "__main__":
    print("=== Weather Day / Rain-Out Cost Calculator — sample runs ===")
    print("(Sample crew/revenue data only — no real customer or business data)\n")

    # Scenario 1: small roofing crew, moderate-rain region — the tool's default sliders
    s1 = run_scenario(
        "Small roofing crew, moderate-rain region (tool defaults)",
        crew_size=5, hourly_wage=28, weather_days_per_month=4, revenue_lost_per_day=2200,
    )

    # Scenario 2: 3-person landscaping crew, fewer weather days
    s2 = run_scenario(
        "3-person landscaping crew, drier climate",
        crew_size=3, hourly_wage=22, weather_days_per_month=2, revenue_lost_per_day=1400,
    )

    # Scenario 3: sanity-check against published industry benchmark
    # Wrenchway/industry write-ups: a 5-worker crew at $25/hr loses $30,000-$50,000/yr
    # in idle labor alone to weather delays (labor cost only, no revenue term).
    s3 = run_scenario(
        "Benchmark check: 5-worker crew, $25/hr, labor cost only (no revenue term)",
        crew_size=5, hourly_wage=25, weather_days_per_month=3.33, revenue_lost_per_day=0,
    )
    lo, hi = 30000, 50000
    in_range = lo <= s3["cost_per_year"] <= hi
    print(f"Sanity check vs published $30,000-$50,000/yr benchmark for this crew profile: "
          f"{fmt(s3['cost_per_year'])}/yr -> {'MATCHES' if in_range else 'OUT OF RANGE'}")

    # Recovery framing: cutting weather days in half via buffer-day scheduling / rescheduling speed
    reduced_days = 4 / 2
    s1_reduced = weather_day_cost(5, 28, reduced_days, 2200)
    recoverable = s1["cost_per_year"] - s1_reduced["cost_per_year"]
    print(f"\nIf scenario 1's crew cut weather days lost from 4/mo to {reduced_days}/mo "
          f"(faster reschedule / buffer-day planning): {fmt(recoverable)}/yr recoverable.")
