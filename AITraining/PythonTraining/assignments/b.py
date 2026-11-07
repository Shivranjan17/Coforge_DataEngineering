while True:
    amount = float(input("Enter Purchase Amount: "))

    if amount < 0:
        print("System Stopped")
        break

    if amount == 0:
        continue

    if amount > 1000:
        print("Valid Purchase:", amount)