# Multi-Currency Travel Budget Analysis

budget_inr = 50000
fee_rate = 0.02

rates_to_inr = {
    "USD": 83.0,
    "EUR": 90.0,
    "JPY": 0.56
}

expenses = [
    ("Hotel", 200, "USD"),
    ("Food", 80, "EUR"),
    ("Transport", 5000, "JPY"),
    ("Shopping", 100, "USD"),
    ("Food", 30, "USD")
]

category_totals = {}
total_spending = 0.0

for category, amount, currency in expenses:
    if amount < 0 or currency not in rates_to_inr:
        print("Skipped invalid expense:", category, amount, currency)
        continue

    converted = amount * rates_to_inr[currency]
    fee = converted * fee_rate
    total = converted + fee

    category_totals[category] = (
        category_totals.get(category, 0) + total
    )

    total_spending += total

print("CATEGORY TOTALS (INR)")

for category, amount in sorted(category_totals.items()):
    print(category, round(amount, 2))

if category_totals:
    largest = max(category_totals, key=category_totals.get)
    print("Largest expense category:", largest)

print("Total spending:", round(total_spending, 2))
print("Budget:", budget_inr)

if total_spending > budget_inr:
    print("Over budget by", round(total_spending - budget_inr, 2), "INR")
else:
    print("Within budget; remaining:",
          round(budget_inr - total_spending, 2), "INR")