# University Scholarship Allocation
MIN_AGGREGATE = 75
MIN_SUBJECT = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

applicants = [
    {"name": "Asha", "aggregate": 88,
     "subjects": [82, 91, 85],
     "attendance": 92, "income": 180000},
    {"name": "Bharat", "aggregate": 78,
     "subjects": [65, 72, 60],
     "attendance": 86, "income": 250000},
    {"name": "Charan", "aggregate": 74,
     "subjects": [80, 78, 75],
     "attendance": 95, "income": 150000},
    {"name": "Divya", "aggregate": 88,
     "subjects": [70, 84, 79],
     "attendance": 92, "income": 160000}
]

eligible = []
rejected = []

for student in applicants:
    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("aggregate below minimum")

    if not student["subjects"] or min(student["subjects"]) < MIN_SUBJECT:
        reasons.append("subject score below minimum")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("attendance below minimum")

    if student["income"] > MAX_INCOME:
        reasons.append("income above limit")

    if reasons:
        rejected.append((student["name"], reasons))
    else:
        eligible.append(student)

eligible.sort(key=lambda s: (
    -s["aggregate"],
    -s["attendance"],
    s["income"],
    s["name"].lower()
))

print("SCHOLARSHIP RANK LIST")

for rank, student in enumerate(eligible, start=1):
    print(rank, student["name"], student["aggregate"],
          student["attendance"], student["income"])

print("\nNOT ELIGIBLE")

for name, reasons in rejected:
    print(name + ":", ", ".join(reasons))