"""
Double-Booking Checker
-----------------------
A tiny tool for home-service businesses (plumbers, HVAC, electricians, roofers,
landscapers) that scans a day's booked jobs per technician and flags any two
jobs that overlap on the calendar -- including the drive-time buffer between
them. Overlaps mean a truck can't physically be in two places on time, which
means a late arrival, an angry customer, or a job that has to be rescheduled
on the spot.

Sample data only -- no real customer data.
"""

from dataclasses import dataclass


@dataclass
class Job:
    tech: str
    customer: str
    start: float  # hour of day, decimal (e.g. 9.5 = 9:30am)
    duration: float  # hours
    value: float  # $ job value
    drive_buffer: float = 0.25  # 15 min drive/reset time required after the job

    @property
    def end(self):
        return self.start + self.duration

    @property
    def blocked_until(self):
        # the tech is not free for a NEW job until the job is done + drive buffer
        return self.end + self.drive_buffer


def fmt_time(h):
    hh = int(h)
    mm = int(round((h - hh) * 60))
    if mm == 60:
        hh += 1
        mm = 0
    period = "AM" if hh < 12 else "PM"
    hh12 = hh % 12
    if hh12 == 0:
        hh12 = 12
    return f"{hh12}:{mm:02d}{period}"


# Sample day of bookings across a 3-tech crew (plumbing/HVAC style business).
# Deliberately includes a few tight back-to-back and overlapping bookings --
# the kind that slip in when jobs are booked by phone/text without checking
# the calendar carefully.
JOBS = [
    Job("Mike",   "R. Alvarez",   8.0, 1.5, 320),
    Job("Mike",   "T. Nguyen",    9.0, 1.0, 210),   # overlaps R. Alvarez
    Job("Mike",   "K. Ellis",    10.75, 2.0, 640),
    Job("Mike",   "P. Duncan",   13.25, 1.5, 480),
    Job("Mike",   "S. Wallace",  15.25, 1.0, 260),
    Job("Sarah",  "D. Ortiz",     8.5, 2.0, 590),
    Job("Sarah",  "L. Chen",     11.0, 1.0, 220),
    Job("Sarah",  "B. Foster",   11.75, 1.5, 410),
    Job("Sarah",  "M. Reyes",    14.0, 1.5, 355),
    Job("Sarah",  "A. Grant",    16.0, 1.0, 240),
    Job("Sarah",  "J. Ibarra",   16.25, 1.0, 300),  # overlaps A. Grant
    Job("Cody",   "H. Patel",     9.0, 1.5, 275),
    Job("Cody",   "V. Marsh",    11.0, 1.0, 195),
    Job("Cody",   "F. Osei",     12.5, 2.0, 720),
    Job("Cody",   "N. Castillo", 14.75, 1.5, 340),
    Job("Cody",   "E. Rowan",    16.5, 1.0, 260),
]


def find_conflicts(jobs):
    conflicts = []
    by_tech = {}
    for j in jobs:
        by_tech.setdefault(j.tech, []).append(j)

    for tech, tech_jobs in by_tech.items():
        tech_jobs.sort(key=lambda j: j.start)
        for i in range(len(tech_jobs) - 1):
            a, b = tech_jobs[i], tech_jobs[i + 1]
            # conflict if the next job starts before the previous one
            # (plus its drive/reset buffer) actually finishes
            if b.start < a.blocked_until:
                overlap_hours = a.blocked_until - b.start
                conflicts.append((tech, a, b, overlap_hours))
    return conflicts


def main():
    total_jobs = len(JOBS)
    total_value = sum(j.value for j in JOBS)
    conflicts = find_conflicts(JOBS)

    affected_jobs = set()
    revenue_at_risk = 0.0
    for tech, a, b, overlap in conflicts:
        affected_jobs.add((tech, a.customer))
        affected_jobs.add((tech, b.customer))
        # the later job is the one that's actually at risk of a late arrival
        revenue_at_risk += b.value

    lines = []
    lines.append("DOUBLE-BOOKING CHECKER — sample day report")
    lines.append("=" * 60)
    lines.append(f"Techs scheduled today: {len(set(j.tech for j in JOBS))}")
    lines.append(f"Jobs booked today: {total_jobs}")
    lines.append(f"Total booked job value: ${total_value:,.0f}")
    lines.append("")
    lines.append(f"CONFLICTS FOUND: {len(conflicts)}")
    lines.append("-" * 60)
    for tech, a, b, overlap in conflicts:
        lines.append(
            f"[{tech}] \"{a.customer}\" ({fmt_time(a.start)}-{fmt_time(a.end)}, "
            f"+{int(a.drive_buffer*60)}m drive) overlaps "
            f"\"{b.customer}\" ({fmt_time(b.start)}-{fmt_time(b.end)}) "
            f"by {overlap*60:.0f} min"
        )
    lines.append("")
    lines.append(f"Jobs touched by a conflict: {len(affected_jobs)} of {total_jobs} "
                  f"({len(affected_jobs)/total_jobs*100:.0f}%)")
    lines.append(f"Revenue riding on the at-risk (later) jobs: ${revenue_at_risk:,.0f}")
    lines.append(f"Share of today's booked value at risk: "
                  f"{revenue_at_risk/total_value*100:.0f}%")

    report = "\n".join(lines)
    print(report)

    with open("output.txt", "w") as f:
        f.write(report + "\n")


if __name__ == "__main__":
    main()
