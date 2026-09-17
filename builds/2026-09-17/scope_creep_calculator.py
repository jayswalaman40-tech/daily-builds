#!/usr/bin/env python3
"""
Scope Creep / Unbilled Change Order Calculator
Estimates the annual revenue a home-service business loses to "just this once"
extra work performed on the jobsite without a signed change order or added invoice line.

Formula:
  affected_jobs   = jobs_per_month * (pct_jobs_with_creep / 100)
  loss_per_job    = (extra_hours * hourly_rate) + extra_materials_cost
  loss_per_month  = affected_jobs * loss_per_job
  loss_per_year   = loss_per_month * 12
"""

def run(label, jobs_per_month, pct_jobs_with_creep, extra_hours, hourly_rate, extra_materials_cost):
    affected_jobs = jobs_per_month * (pct_jobs_with_creep / 100)
    loss_per_job = (extra_hours * hourly_rate) + extra_materials_cost
    loss_per_month = affected_jobs * loss_per_job
    loss_per_year = loss_per_month * 12

    print(f"--- {label} ---")
    print(f"Jobs/month: {jobs_per_month}")
    print(f"Jobs with unbilled extra work: {pct_jobs_with_creep}% -> {affected_jobs:.1f} jobs/mo")
    print(f"Extra unbilled hours/job: {extra_hours}  @ ${hourly_rate}/hr")
    print(f"Extra unbilled materials/job: ${extra_materials_cost}")
    print(f"Loss per affected job: ${loss_per_job:,.2f}")
    print(f"Loss per month: ${loss_per_month:,.2f}")
    print(f"Loss per year: ${loss_per_year:,.2f}")
    print()
    return {
        "label": label,
        "affected_jobs_per_month": round(affected_jobs, 1),
        "loss_per_job": round(loss_per_job, 2),
        "loss_per_month": round(loss_per_month, 2),
        "loss_per_year": round(loss_per_year, 2),
    }


if __name__ == "__main__":
    results = []

    # Scenario 1: default web-tool scenario - mid-size plumbing/HVAC service shop
    results.append(run(
        "Sample: mid-size plumbing/HVAC service shop",
        jobs_per_month=60,
        pct_jobs_with_creep=30,
        extra_hours=2,
        hourly_rate=85,
        extra_materials_cost=60,
    ))

    # Scenario 2: small remodeling contractor, big-ticket jobs, fewer but bigger creep events
    results.append(run(
        "Sample: small remodeling contractor",
        jobs_per_month=12,
        pct_jobs_with_creep=60,
        extra_hours=4,
        hourly_rate=85,
        extra_materials_cost=150,
    ))

    # Scenario 3: 4-person roofing crew
    results.append(run(
        "Sample: 4-person roofing crew",
        jobs_per_month=25,
        pct_jobs_with_creep=40,
        extra_hours=2.5,
        hourly_rate=75,
        extra_materials_cost=90,
    ))

    print("=== Summary ===")
    for r in results:
        print(f"{r['label']}: ${r['loss_per_year']:,.0f}/yr lost to unbilled scope creep "
              f"({r['affected_jobs_per_month']} affected jobs/mo)")
