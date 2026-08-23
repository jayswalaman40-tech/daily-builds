# Lead List Cleaner

A tiny tool that turns a messy leads CSV into a clean, ready-to-use one.

**What it does**
- Trims whitespace, fixes name/company casing
- Validates + lowercases emails (drops invalid ones)
- Normalises phone numbers
- Removes duplicate leads by email
- Prints a real before/after summary

**Run**
```bash
python lead_cleaner.py leads_raw.csv leads_clean.csv
```

**Real run on the sample (`leads_raw.csv`, 10 rows)**
```
Rows in            : 10
Clean leads out    : 5
Dropped (bad email): 3
Dropped (duplicate): 2
Junk removed       : 50% of the list
```

No client data is used — `leads_raw.csv` is fabricated sample data.
