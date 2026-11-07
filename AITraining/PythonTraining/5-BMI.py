weight  = float(input("Input Weight :"))
height = float(input("Input Height in meter :"))
bmi = weight / (height * height)
print("BMI =", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")