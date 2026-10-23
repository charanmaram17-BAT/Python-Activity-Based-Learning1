# Student Performance Trend Analysis

students = {
    "Asha": {
        "Maths": [62, 70, 82],
        "Physics": [48, 46, 49],
        "Programming": [70, 78, 88]
    },
    "Balu": {
        "Maths": [80, 75, 72],
        "Physics": [65, 68, 70],
        "Programming": [55, 61, 66]
    }
}

for name, subjects in students.items():
    latest_scores = []
    weak_subjects = []

    print("\nStudent:", name)

    for subject, scores in subjects.items():
        if len(scores) < 2 or any(s < 0 or s > 100 for s in scores):
            print(subject, "- invalid score data")
            continue

        change = scores[-1] - scores[0]

        if change > 0:
            trend = "Improved"
        elif change < 0:
            trend = "Declined"
        else:
            trend = "No change"

        if all(score < 50 for score in scores):
            weak_subjects.append(subject)

        latest_scores.append(scores[-1])

        print(subject, "change:", change, "points -", trend)

    average = (
        sum(latest_scores) / len(latest_scores)
        if latest_scores else 0
    )

    if average >= 85:
        category = "Excellent"
    elif average >= 70:
        category = "Good"
    elif average >= 50:
        category = "Needs Improvement"
    else:
        category = "At Risk"

    print("Latest average:", round(average, 2))
    print("Classification:", category)
    print("Consistently weak subjects:", weak_subjects or "None")