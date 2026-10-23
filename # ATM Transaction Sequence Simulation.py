# ATM Transaction Sequence Simulation

balance = 5000.00
withdrawal_limit = 2000.00

transactions = [
    ("deposit", 1500),
    ("withdraw", 1200),
    ("withdraw", 2500),
    ("withdraw", 6000),
    ("withdraw", 500),
    ("deposit", -100),
    ("transfer", 100)
]

deposit_total = 0.0
withdrawal_total = 0.0
accepted = 0
rejected = 0

for kind, amount in transactions:
    kind = kind.lower()

    if amount <= 0 or kind not in ("deposit", "withdraw"):
        print("REJECTED:", kind, amount, "- invalid transaction")
        rejected += 1

    elif kind == "deposit":
        balance += amount
        deposit_total += amount
        accepted += 1

        print("ACCEPTED deposit:", amount,
              "Balance:", round(balance, 2))

    elif amount > withdrawal_limit:
        print("REJECTED withdrawal:", amount,
              "- exceeds per-transaction limit")
        rejected += 1

    elif amount > balance:
        print("REJECTED withdrawal:", amount,
              "- insufficient balance")
        rejected += 1

    else:
        balance -= amount
        withdrawal_total += amount
        accepted += 1

        print("ACCEPTED withdrawal:", amount,
              "Balance:", round(balance, 2))

print("\nTRANSACTION SUMMARY")
print("Opening balance: 5000.00")
print("Deposits:", round(deposit_total, 2))
print("Withdrawals:", round(withdrawal_total, 2))
print("Accepted:", accepted, "Rejected:", rejected)
print("Final balance:", round(balance, 2))