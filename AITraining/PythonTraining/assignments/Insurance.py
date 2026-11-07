age = int(input("Age: "))
smoker = input("Smoker (yes/no): ")
bmi = float(input("BMI: "))
disease = input("Pre-existing Disease (yes/no): ")

if disease == "yes" and age > 60:
    print("Insurance Rejected")

elif smoker == "yes" and age > 50:
    print("High Premium")

elif bmi >= 25:
    print("Medium Premium")

elif age < 30 and smoker == "no" and bmi < 25:
    print("Low Premium")

else:
    print("Standard Premium")