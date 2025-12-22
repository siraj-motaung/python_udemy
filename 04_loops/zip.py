# You are preparing an order summary with customer names and their total bill.
# Task:
#       - Use two lists: One for names and one for bills.
#       - Print: "[Name] paid R[amount]"

names = ["Siraj", "Shameel", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount}")


