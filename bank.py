import sys

script_name = sys.argv[0]


initial_bal = float(sys.argv[1])
deposit_amount = float(sys.argv[2])

updated_bal = initial_bal + deposit_amount

print("Initial Balance:",initial_bal)
print("Deposit Amount:",deposit_amount)
print("Updated Balance:",updated_bal)
