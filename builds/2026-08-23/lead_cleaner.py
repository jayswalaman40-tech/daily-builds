#!/usr/bin/env python3
"""
Lead List Cleaner
-----------------
Takes a messy leads CSV (the kind agencies buy or export) and returns a clean one:
  - trims whitespace, fixes name/company casing
  - normalises + validates emails (drops obviously invalid ones)
  - normalises phone numbers to digits (keeps a leading +)
  - removes duplicate leads (by email)
  - writes a clean CSV + prints a real before/after summary

Pure Python standard library. No client data — sample input only.
Usage:  python lead_cleaner.py leads_raw.csv leads_clean.csv
"""
import csv
import re
import sys

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")


def clean_name(value: str) -> str:
    return " ".join(part.capitalize() for part in value.strip().split())


def clean_email(value: str) -> str:
    email = value.strip().lower()
    return email if EMAIL_RE.match(email) else ""


def clean_phone(value: str) -> str:
    raw = value.strip()
    plus = raw.startswith("+")
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return ""
    return ("+" if plus else "") + digits


def main(src: str, dst: str) -> None:
    seen_emails = set()
    total = kept = dropped_invalid = dropped_dupe = 0

    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    cleaned = []
    for row in rows:
        total += 1
        email = clean_email(row.get("email", ""))
        if not email:
            dropped_invalid += 1
            continue
        if email in seen_emails:
            dropped_dupe += 1
            continue
        seen_emails.add(email)
        cleaned.append({
            "name": clean_name(row.get("name", "")),
            "company": clean_name(row.get("company", "")),
            "email": email,
            "phone": clean_phone(row.get("phone", "")),
        })
        kept += 1

    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "company", "email", "phone"])
        writer.writeheader()
        writer.writerows(cleaned)

    print("Lead List Cleaner — run summary")
    print("-" * 34)
    print(f"Rows in            : {total}")
    print(f"Clean leads out    : {kept}")
    print(f"Dropped (bad email): {dropped_invalid}")
    print(f"Dropped (duplicate): {dropped_dupe}")
    pct = round(100 * (total - kept) / total) if total else 0
    print(f"Junk removed       : {pct}% of the list")
    print(f"Saved              : {dst}")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "leads_raw.csv"
    dst = sys.argv[2] if len(sys.argv) > 2 else "leads_clean.csv"
    main(src, dst)
