jobs_per_month = 15
material_cost_per_job = 7500
price_increase_pct = 9
no_clause_pct = 65

increase_per_job = material_cost_per_job * (price_increase_pct/100)
unprotected_jobs = jobs_per_month * (no_clause_pct/100)
eaten_per_month = unprotected_jobs * increase_per_job
eaten_per_year = eaten_per_month * 12

# industry benchmark tariff line item: 1.0-1.5% of total job value (material is a % of total)
# assume material is ~35% of total job value -> avg total job value
avg_total_job_value = material_cost_per_job / 0.35
benchmark_pct = 1.25
recommended_line_item = avg_total_job_value * (benchmark_pct/100)
recoverable_per_year_at_benchmark = recommended_line_item * jobs_per_month * 12

print(f"Sample: mid-size remodeling/roofing contractor")
print(f"Material-heavy jobs/month: {jobs_per_month}")
print(f"Avg material cost per job at quote time: ${material_cost_per_job:,.0f}")
print(f"Material price increase since quoting (tariffs, steel/aluminum/lumber): {price_increase_pct}%")
print(f"% of jobs fixed-price with NO escalation clause: {no_clause_pct}%")
print()
print(f"Increase $ per unprotected job: ${increase_per_job:,.0f}")
print(f"Unprotected jobs/month: {unprotected_jobs:.2f}")
print(f"EATEN per month (contractor pays out of margin): ${eaten_per_month:,.0f}")
print(f"EATEN per year: ${eaten_per_year:,.0f}")
print()
print(f"Industry benchmark tariff/escalation line item: {benchmark_pct}% of total job value")
print(f"Est. avg total job value (material ~35% of total): ${avg_total_job_value:,.0f}")
print(f"Recommended line item per job: ${recommended_line_item:,.0f}")
print(f"If added to ALL {jobs_per_month} jobs/month going forward, protects: ${recoverable_per_year_at_benchmark:,.0f}/yr")
