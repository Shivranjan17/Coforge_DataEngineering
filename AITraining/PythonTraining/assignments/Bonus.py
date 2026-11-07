rating = int(input("Enter Rating (1-5): "))
experience = int(input("Enter Years of Experience: "))
delivery = input("Project Delivery Status (on time/delayed): ")

if rating == 5 and experience > 10 and delivery == "on time":
    print("Bonus = 30%")
elif rating == 4 and experience > 7:
    print("Bonus = 20%")
elif rating == 3 and delivery == "delayed":
    print("Bonus = 5%")
else:
    print("No Bonus")