#!/usr/bin/env python3
"""
Credit Card Processing Fee Calculator
Sample data only — no real business, customer, or processor data.

Models the hidden margin cost of credit card processing fees for a home-
service business: percentage rate on card volume + flat per-transaction
fees, then compares that against net profit and a benchmark interchange-
plus rate to show what's recoverable by negotiating.

fee_per_month = volume * (rate / 100) + (transactions * flat_fee)
fee_per_year  = fee_per_month * 12
annual_profit = volume * 12 * (margin / 100)
pct_of_profit = fee_per_year / annual_profit * 100
savings       = max(0, volume * (rate - benchmark_rate) / 100) * 12
"""

BENCHMARK_RATE = 2.1  # typical achievable interchange-plus effective rate


def fee_cost(volume, rate, transactions, flat_fee, margin):
    fee_per_month = volume * (rate / 100) + (transactions * flat_fee)
    fee_per_year = fee_per_month * 12
    annual_profit = volume * 12 * (margin / 100)
    pct_of_profit = (fee_per_year / annual_profit * 100) if annual_profit > 0 else 0
    savings = max(0, volume * ((rate - BENCHMARK_RATE) / 100)) * 12
    return {
        "fee_per_month": fee_per_month,
        "fee_per_year": fee_per_year,
        "annual_profit": annual_profit,
        "pct_of_profit": pct_of_profit,
        "savings": savings,
    }


def fmt(n):
    return "${:,.0f}".format(n)


def run_scenario(title, volume, rate, transactions, flat_fee, margin):
    r = fee_cost(volume, rate, transactions, flat_fee, margin)
    print(f"--- {title} ---")
    print(f"Card volume/mo: {fmt(volume)} | Rate: {rate}% | Txns/mo: {transactions} | "
          f"Flat fee: ${flat_fee}/txn | Net margin: {margin}%")
    print(f"Fee cost per month:        {fmt(r['fee_per_month'])}")
    print(f"Fee cost per year:         {fmt(r['fee_per_year'])}")
    print(f"Annual profit (pre-fee comparison base): {fmt(r['annual_profit'])}")
    print(f"Fees as % of annual profit: {r['pct_of_profit']:.1f}%")
    print(f"Recoverable/yr at {BENCHMARK_RATE}% benchmark: {fmt(r['savings'])}")
    print()
    return r


if __name__ == "__main__":
    print("=== Credit Card Processing Fee Calculator — sample runs ===")
    print("(Sample business data only — no real customer or processor data)\n")

    # Scenario 1: tool defaults — mid-size home-service business on a flat-rate processor
    s1 = run_scenario(
        "Mid-size home-service business, flat-rate processor (tool defaults)",
        volume=30000, rate=3.2, transactions=120, flat_fee=0.30, margin=12,
    )

    # Scenario 2: solo operator, high-ticket jobs, worse rate
    s2 = run_scenario(
        "Solo operator, high-ticket installs, unnegotiated rate",
        volume=18000, rate=3.5, transactions=25, flat_fee=0.30, margin=15,
    )

    # Scenario 3: sanity-check against published example — $75k/yr revenue business,
    # 10% net margin, $60k/yr processed via card at 2.7% effective rate.
    # Published claim: processing costs > 20% of total annual profit.
    s3_volume_month = 60000 / 12
    s3 = run_scenario(
        "Benchmark check: $75k/yr revenue biz, $60k/yr on cards at 2.7%, 10% margin",
        volume=s3_volume_month, rate=2.7, transactions=0, flat_fee=0, margin=10,
    )
    lo_pct = 20.0
    checks_out = s3["pct_of_profit"] >= lo_pct
    print(f"Sanity check vs published '>20% of annual profit' claim for this exact profile: "
          f"{s3['pct_of_profit']:.1f}% of profit -> {'MATCHES/EXCEEDS' if checks_out else 'BELOW CLAIM'}")

    # Recovery framing: scenario 1's business negotiates its 3.2% flat rate down to 2.1%
    print(f"\nIf scenario 1's business (30,000/mo card volume at 3.2%) negotiated down to "
          f"the {BENCHMARK_RATE}% interchange-plus benchmark: {fmt(s1['savings'])}/yr recoverable "
          f"(rate portion only, before any flat-fee or transaction-count changes).")
