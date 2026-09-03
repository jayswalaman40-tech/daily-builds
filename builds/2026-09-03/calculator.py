#!/usr/bin/env python3
"""
Unsold Estimate Recovery Calculator - sample run.

Simulates one month of quotes for a small home-service business (a mix of
plumbing/HVAC-style jobs) and measures:
  1. Close rate by number of follow-up contacts made on each quote.
  2. Dollar value still sitting open, broken out by how neglected it is.
  3. What closing the "neglected" pile at the shop's own achieved rate for
     well-followed-up quotes would be worth.

Sample data only - no real customer data. Numbers below are generated to be
directionally realistic (close rate rises with follow-up count, most shops
stop following up after 1-2 touches), matching industry-reported patterns:
initial close rates of ~23-30%, 60% of sales happening after the 4th
follow-up contact.
"""

import random

random.seed(7)

JOB_TYPES = ["Water heater replace", "AC tune-up", "Drain clear", "Panel upgrade",
             "Furnace repair", "Pipe repipe", "Duct cleaning", "Sump pump install",
             "Toilet install", "Mini-split install", "Leak repair", "Breaker replace"]

quotes = []
for i in range(24):
    value = random.randint(180, 3800)
    follow_ups = random.choices([0, 1, 2, 3, 4, 5], weights=[22, 26, 20, 14, 11, 7])[0]
    days_open = random.randint(1, 30)
    # Higher follow-up count -> higher chance won, matching the stat that
    # most sales land after the 4th contact.
    win_chance = {0: 0.08, 1: 0.14, 2: 0.24, 3: 0.34, 4: 0.52, 5: 0.61}[follow_ups]
    if days_open < 3:
        status = "open"  # too fresh to have a verdict yet
    else:
        status = "won" if random.random() < win_chance else ("open" if random.random() < 0.4 else "lost")
    quotes.append({
        "job": JOB_TYPES[i % len(JOB_TYPES)],
        "value": value,
        "follow_ups": follow_ups,
        "days_open": days_open,
        "status": status,
    })

total_quotes = len(quotes)
total_value = sum(q["value"] for q in quotes)
won = [q for q in quotes if q["status"] == "won"]
lost = [q for q in quotes if q["status"] == "lost"]
open_q = [q for q in quotes if q["status"] == "open"]

won_value = sum(q["value"] for q in won)
close_rate = len(won) / total_quotes * 100

# Close rate by follow-up bucket
buckets = {"0-1 follow-ups": [0, 1], "2-3 follow-ups": [2, 3], "4+ follow-ups": [4, 5]}
bucket_stats = {}
for label, fus in buckets.items():
    in_bucket = [q for q in quotes if q["follow_ups"] in fus and q["status"] != "open"]
    won_in_bucket = [q for q in in_bucket if q["status"] == "won"]
    rate = (len(won_in_bucket) / len(in_bucket) * 100) if in_bucket else 0
    bucket_stats[label] = {"n": len(in_bucket), "won": len(won_in_bucket), "rate": round(rate, 1)}

# Neglected open quotes: sitting >3 days old with fewer than 2 follow-ups
neglected = [q for q in open_q if q["days_open"] > 3 and q["follow_ups"] < 2]
neglected_value = sum(q["value"] for q in neglected)

# Best achieved close rate (4+ follow-ups bucket) applied to the neglected pile
best_rate = bucket_stats["4+ follow-ups"]["rate"] / 100
recoverable = round(neglected_value * best_rate)

print(f"Quotes sent this month:        {total_quotes}")
print(f"Total quoted value:            ${total_value:,}")
print(f"Won so far:                    {len(won)} (${won_value:,}) -> {close_rate:.1f}% close rate")
print(f"Lost:                          {len(lost)}")
print(f"Still open:                    {len(open_q)}")
print()
print("Close rate by follow-up count:")
for label, s in bucket_stats.items():
    print(f"  {label:16s} n={s['n']:2d}  won={s['won']:2d}  close rate={s['rate']}%")
print()
print(f"Neglected open quotes (>3 days old, <2 follow-ups): {len(neglected)}")
print(f"Value sitting neglected:        ${neglected_value:,}")
print(f"Close rate this shop hits with 4+ follow-ups: {bucket_stats['4+ follow-ups']['rate']}%")
print(f"If applied to the neglected pile -> recoverable: ${recoverable:,}")
