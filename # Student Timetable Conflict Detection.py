# Student Timetable Conflict Detection

# Entry: (course, day, start, end, room)

timetable = [
    ("Python", "Mon", "09:00", "10:00", "R101"),
    ("Maths", "Mon", "09:30", "10:30", "R102"),
    ("Physics", "Mon", "10:00", "11:00", "R101"),
    ("English", "Tue", "11:00", "12:00", "R103")
]

unavailable_rooms = {"R103"}


def to_minutes(time_text):
    hour, minute = map(int, time_text.split(":"))

    if not (0 <= hour < 24 and 0 <= minute < 60):
        raise ValueError("Invalid time: " + time_text)

    return hour * 60 + minute


valid_entries = []

for entry in timetable:
    course, day, start, end, room = entry

    try:
        start_m = to_minutes(start)
        end_m = to_minutes(end)

        if start_m >= end_m:
            print("INVALID time interval:", course)
        else:
            valid_entries.append(
                (course, day, start_m, end_m, room)
            )

    except ValueError as error:
        print("INVALID entry:", error)

conflicts = []

for i in range(len(valid_entries)):
    c1, d1, s1, e1, r1 = valid_entries[i]

    if r1 in unavailable_rooms:
        conflicts.append(f"{c1}: room {r1} is unavailable")

    for j in range(i + 1, len(valid_entries)):
        c2, d2, s2, e2, r2 = valid_entries[j]

        overlap = d1 == d2 and max(s1, s2) < min(e1, e2)

        if overlap:
            conflicts.append(
                f"{c1} and {c2}: overlapping class times"
            )

            if r1 == r2:
                conflicts.append(
                    f"{c1} and {c2}: room {r1} double-booked"
                )

print("CONFLICT REPORT")

if conflicts:
    for item in conflicts:
        print("-", item)

    print("Timetable valid:", False)
else:
    print("No conflicts found.")
    print("Timetable valid:", True)