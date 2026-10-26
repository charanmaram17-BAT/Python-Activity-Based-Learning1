

available = {
    "projector": 3,
    "laptop": 10,
    "microphone": 2
}


activities = [
    ("Exam", {"projector": 1, "laptop": 4, "microphone": 0}),
    ("AI Workshop", {"projector": 2, "laptop": 5, "microphone": 2}),
    ("Club Meeting", {"projector": 1, "laptop": 3, "microphone": 1})
]

remaining = available.copy()
results = []

for activity, requirements in activities:
    allocated = {}
    shortages = {}

    for resource, needed in requirements.items():

        if needed < 0:
            shortages[resource] = "invalid negative requirement"
            allocated[resource] = 0
            continue

        given = min(needed, remaining.get(resource, 0))

        allocated[resource] = given
        remaining[resource] = remaining.get(resource, 0) - given

        if given < needed:
            shortages[resource] = needed - given

    results.append((activity, allocated, shortages))

    print("\nActivity:", activity)
    print("Allocated:", allocated)
    print("Shortages:", shortages or "None")

print("\nREMAINING RESOURCES:", remaining)
print("Allocation policy: priority order; no resource is over-allocated.")
