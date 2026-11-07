income = float(input("Annual Income: "))
age = int(input("Age: "))
investment = float(input("Investment Amount: "))

taxable_income = income - investment

if age >= 60:
    print("Senior Citizen Exemption Applied")

if taxable_income < 500000:
    tax = 0
elif taxable_income < 1000000:
    tax = taxable_income * 0.10
elif taxable_income < 2000000:
    tax = taxable_income * 0.20
else:
    tax = taxable_income * 0.30

print("Tax Amount =", tax)