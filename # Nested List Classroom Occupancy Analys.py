# Nested List Classroom Occupancy Analysis
# None = vacant; "RESERVED" = unavailable seat

classrooms = {
    "A": [[None, None, "RESERVED"], [None, None, None]],
    "B": [[None, "RESERVED"], [None, None]]
}

assignments = [
    ("ST101", "A", 0, 0),
    ("ST102", "A", 0, 1),
    ("ST103", "A", 0, 2),
    ("ST104", "B", 1, 0),
    ("ST101", "B", 0, 0),
    ("ST105", "Z", 0, 0)
]

assigned_ids = set()

for student_id, room, row, seat in assignments:

    if room not in classrooms:
        print("REJECTED", student_id, "- unknown room", room)
        continue

    if student_id in assigned_ids:
        print("REJECTED", student_id, "- duplicate assignment")
        continue

    seats = classrooms[room]

    if (row < 0 or row >= len(seats)
            or seat < 0 or seat >= len(seats[row])):
        print("REJECTED", student_id, "- invalid seat position")
        continue

    if seats[row][seat] == "RESERVED":
        print("REJECTED", student_id, "- seat is reserved")
        continue

    if seats[row][seat] is not None:
        print("REJECTED", student_id, "- seat already occupied")
        continue

    seats[row][seat] = student_id
    assigned_ids.add(student_id)

    print("ALLOCATED", student_id, "to", room, row, seat)

print("\nCLASSROOM SUMMARY")

for room, rows in classrooms.items():
    flat = [seat for row in rows for seat in row]

    occupied = sum(
        seat is not None and seat != "RESERVED"
        for seat in flat
    )

    reserved = flat.count("RESERVED")
    vacant = flat.count(None)

    print(room, "total:", len(flat),
          "occupied:", occupied,
          "reserved:", reserved,
          "vacant:", vacant)

    print("Layout:", rows)