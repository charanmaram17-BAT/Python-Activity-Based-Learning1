# University Admission Decision Engine

rules = {
    "CSE": {"aggregate": 80, "subject": "Maths", "minimum": 75},
    "ECE": {"aggregate": 75, "subject": "Physics", "minimum": 70},
    "Mechanical": {"aggregate": 70, "subject": "Maths", "minimum": 60}
}

applicants = [
    {"name": "Asha", "course": "CSE", "aggregate": 88,
     "Maths": 90, "Physics": 82, "Chemistry": 85},
    {"name": "Bharat", "course": "CSE", "aggregate": 84,
     "Maths": 92, "Physics": 80, "Chemistry": 79},
    {"name": "Charan", "course": "ECE", "aggregate": 77,
     "Maths": 72, "Physics": 74, "Chemistry": 76},
    {"name": "Divya", "course": "Mechanical", "aggregate": 73,
     "Maths": 68, "Physics": 65, "Chemistry": 70}
]

by_course = {course: [] for course in rules}
rejected = []

for person in applicants:
    course = person["course"]

    if course not in rules:
        rejected.append((person["name"], "unknown course"))
        continue

    rule = rules[course]
    reasons = []

    if person["aggregate"] < rule["aggregate"]:
        reasons.append("aggregate below course threshold")

    if person[rule["subject"]] < rule["minimum"]:
        reasons.append(rule["subject"] + " below course threshold")

    if reasons:
        rejected.append((person["name"], "; ".join(reasons)))
    else:
        by_course[course].append(person)

for course, people in by_course.items():
    subject = rules[course]["subject"]

    people.sort(key=lambda p: (
        -p[subject],
        -p["aggregate"],
        p["name"].lower()
    ))

    print("\n", course, "RANK LIST")

    for rank, p in enumerate(people, 1):
        print(rank, p["name"], "aggregate:", p["aggregate"],
              subject + ":", p[subject])

print("\nNOT ELIGIBLE")

for name, reason in rejected:
    print(name + ":", reason) 