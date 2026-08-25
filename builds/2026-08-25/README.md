# Job Quote & Margin Checker

A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers)
that audits a batch of job quotes against a target profit margin and flags the
ones that are quietly underpriced.

**What it does**
- Reads a quote log (labor hours, labor cost/hr, materials cost, trip fee, what was actually quoted)
- Computes the true cost and actual margin % on every job
- Flags any quote that falls below your target margin (default 30%)
- Shows what each underpriced job *should* have been quoted, and how much was left on the table
- Projects a monthly leak estimate if the same underpricing rate holds

**Run**
```bash
python quote_margin_checker.py quotes.csv --target 30
```

**Real run on the sample (`quotes.csv`, 20 quotes)**
```
Quotes analyzed        : 20
Target margin          : 30%
Average actual margin  : 41.5%
Quotes below target    : 6 (30%)
$ left on the table     : $201  (this batch)

Worst-margin jobs (below target):
  Q105  Faucet install                   margin   1.7%  quoted $150  should be ~$211  (short $61)
  Q102  Drain cleaning                   margin   6.7%  quoted $150  should be ~$200  (short $50)
  Q118  Leaky pipe fix                   margin  13.5%  quoted $130  should be ~$161  (short $31)
  Q113  Thermostat install               margin  17.6%  quoted $170  should be ~$200  (short $30)
  Q106  Furnace tune-up                  margin  20.3%  quoted $160  should be ~$182  (short $22)

Projected monthly leak (~40 jobs/mo, same underpriced rate): ~$401/mo
```

The pattern: big installs (water heaters, mini-splits, panel upgrades) were
priced fine. It's the small, fast "quick call" jobs — the ones people often
still quote off an old flat-rate card — that were quietly running near
break-even margin.

**Web version**
A live, interactive instant-quote calculator: https://answercatch.com/tools/quote-margin-checker/
Plug in labor hours, labor cost, materials, trip fee and your target margin —
it tells you the price to quote and your dollar profit, live.

**Files**
- `quote_margin_checker.py` — the analysis tool
- `quotes.csv` — sample quote log (sample data, not real customers)
- `output.txt` — real run output above
- `screenshot.png` — screenshot of the live web tool
