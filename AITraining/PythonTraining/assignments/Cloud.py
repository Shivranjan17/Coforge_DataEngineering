compute_hours = int(input("Compute Hours: "))
storage = int(input("Storage Used (GB): "))
plan = input("Plan (Basic/Premium/Enterprise): ")

if plan == "Basic":
    support_fee = 500
    bill = (compute_hours * 10) + (storage * 2) + support_fee

elif plan == "Premium":
    support_fee = 1000
    bill = (compute_hours * 8) + (storage * 2) + support_fee

elif plan == "Enterprise":
    support_fee = 2000
    bill = (compute_hours * 7) + (storage * 1.5) + support_fee

else:
    bill = 0
    print("Invalid Plan")

print("Final Bill =", bill)