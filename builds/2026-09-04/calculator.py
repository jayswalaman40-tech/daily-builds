#!/usr/bin/env python3
"""
Callback & Rework Cost Calculator - sample run.

Simulates one month of completed jobs for a small home-service shop
(plumbing/HVAC/electrical) and measures how much unbilled callback/rework
trips actually cost, compared to the industry benchmark callback rate.

Sample data only - no real customers. Seeded random for reproducibility.
"""
import random

random.seed(4)

# --- Industry benchmarks found in research (see README.md) ---
BENCHMARK_RATE = 0.02      # 2% = "acceptable" callback rate (best-in-class < 1.5%)
RED_FLAG_RATE = 0.03       # >3% callback rate is a red flag
AVG_CALLBACK_COST_LOW = 300   # $ per callback (truck roll + tech time + parts, low end)
AVG_CALLBACK_COST_HIGH = 650  # $ per callback (service call, high end)

# --- Simulate one month of completed jobs for a 4-tech shop ---
JOBS_PER_MONTH = 130
AVG_JOB_VALUE = 410

jobs = []
for i in range(JOBS_PER_MONTH):
    job_value = round(random.gauss(AVG_JOB_VALUE, 90))
    job_value = max(120, job_value)
    # this shop runs a bit hot: ~6% of jobs come back as a callback/rework trip
    is_callback = random.random() < 0.065
    callback_cost = round(random.uniform(AVG_CALLBACK_COST_LOW, AVG_CALLBACK_COST_HIGH)) if is_callback else 0
    jobs.append({"job": i + 1, "value": job_value, "callback": is_callback, "callback_cost": callback_cost})

total_jobs = len(jobs)
callbacks = [j for j in jobs if j["callback"]]
n_callbacks = len(callbacks)
callback_rate = n_callbacks / total_jobs

monthly_callback_cost = sum(j["callback_cost"] for j in callbacks)
annual_callback_cost = monthly_callback_cost * 12

# cost if this shop instead ran at the benchmark rate (2%), same avg cost/callback
avg_cost_per_callback = monthly_callback_cost / n_callbacks if n_callbacks else 0
benchmark_callbacks = total_jobs * BENCHMARK_RATE
benchmark_monthly_cost = benchmark_callbacks * avg_cost_per_callback
monthly_savings_at_benchmark = monthly_callback_cost - benchmark_monthly_cost
annual_savings_at_benchmark = monthly_savings_at_benchmark * 12

flag = "RED FLAG (above 3%)" if callback_rate > RED_FLAG_RATE else (
    "above benchmark" if callback_rate > BENCHMARK_RATE else "at/below benchmark"
)

print("=== Callback & Rework Cost Calculator — sample run ===")
print(f"Jobs completed this month: {total_jobs}")
print(f"Callbacks/rework trips: {n_callbacks}")
print(f"Callback rate: {callback_rate*100:.1f}%  ({flag})")
print(f"Average cost per callback (this shop): ${avg_cost_per_callback:,.0f}")
print(f"Monthly cost of callbacks: ${monthly_callback_cost:,.0f}")
print(f"Annualized cost of callbacks: ${annual_callback_cost:,.0f}")
print()
print(f"Industry benchmark callback rate: {BENCHMARK_RATE*100:.0f}%")
print(f"Callbacks/month at benchmark rate: {benchmark_callbacks:.1f}")
print(f"Monthly cost at benchmark rate: ${benchmark_monthly_cost:,.0f}")
print(f"Monthly $ recoverable by hitting benchmark: ${monthly_savings_at_benchmark:,.0f}")
print(f"Annual $ recoverable by hitting benchmark: ${annual_savings_at_benchmark:,.0f}")
