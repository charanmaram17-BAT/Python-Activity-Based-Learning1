# Food Waste Monitoring System

LIMIT_PERCENT = 10

daily_data = [
    ("Monday", 200, 170, 30),
    ("Tuesday", 180, 170, 10),
    ("Wednesday", 220, 190, 30),
    ("Thursday", 150, 145, 5),
    ("Friday", 200, 180, 25)
]

exceeded_days = []

for day, prepared, served, leftovers in daily_data:

    if prepared <= 0 or served < 0 or leftovers < 0:
        print(day, "- INVALID negative/zero counts")
        continue

    if served + leftovers > prepared:
        print(day, "- DATA ERROR: served + leftovers exceeds prepared")
        continue

    waste_percent = leftovers / prepared * 100

    status = (
        "EXCEEDS LIMIT"
        if waste_percent > LIMIT_PERCENT
        else "Within limit"
    )

    print(day, "waste:", round(waste_percent, 2), "% -", status)

    if waste_percent > LIMIT_PERCENT:
        exceeded_days.append(day)

print("Acceptable limit:", LIMIT_PERCENT, "%")
print("Days exceeding limit:", exceeded_days or "None")