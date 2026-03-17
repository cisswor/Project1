def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    return tip, total

bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage (e.g. 15): "))

tip, total = calculate_tip(bill, tip_percent)

print(f"Tip amount: ${tip:.2f}")
print(f"Total to pay: ${total:.2f}")