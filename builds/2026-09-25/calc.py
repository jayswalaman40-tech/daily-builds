"""Overtime Cost Calculator — sample run (matches the web tool's JS exactly).

Sample shop profile:
  4 techs regularly working overtime, 8 OT hours/week each,
  $28/hr regular rate, 1.5x (time-and-a-half) overtime multiplier.
"""

WEEKS = 50
BURDEN = 1.35
REG_HOURS_YEAR = 2000  # 40 hrs x 50 weeks


def run(techs, ot_hrs_per_week, rate, mult):
    ot_rate = rate * mult
    premium_per_hour = ot_rate - rate
    weekly_ot_hours = techs * ot_hrs_per_week
    prem_week = weekly_ot_hours * premium_per_hour
    prem_year = prem_week * WEEKS
    total_ot_week = weekly_ot_hours * ot_rate
    total_ot_year = total_ot_week * WEEKS
    new_hire_cost = rate * BURDEN * REG_HOURS_YEAR
    return {
        "techs": techs,
        "ot_hrs_per_week": ot_hrs_per_week,
        "rate": rate,
        "mult": mult,
        "weekly_ot_hours": weekly_ot_hours,
        "premium_per_hour": premium_per_hour,
        "ot_premium_per_week": round(prem_week, 2),
        "ot_premium_per_year": round(prem_year, 2),
        "total_ot_spend_per_year": round(total_ot_year, 2),
        "fully_loaded_new_hire_per_year": round(new_hire_cost, 2),
        "gap": round(total_ot_year - new_hire_cost, 2),
    }


if __name__ == "__main__":
    print("=== Sample shop: 4 techs, 8 OT hrs/week each, $28/hr, 1.5x ===")
    base = run(4, 8, 28, 1.5)
    for k, v in base.items():
        print(f"{k}: {v}")

    print()
    print("=== Sensitivity: same shop but 2x weekend/OT rate ===")
    double = run(4, 8, 28, 2.0)
    for k, v in double.items():
        print(f"{k}: {v}")

    print()
    print("=== Smaller shop: 2 techs, 5 OT hrs/week, $32/hr, 1.5x ===")
    small = run(2, 5, 32, 1.5)
    for k, v in small.items():
        print(f"{k}: {v}")
