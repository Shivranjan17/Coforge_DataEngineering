salary = int(input("Salary :"))
if salary == 50000:
    bonus = salary * 20 / 100
    print(bonus)

elif salary >= 30000 and salary <= 50000:
    bonus = salary * 10 / 100
    print( bonus)

elif salary < 30000:
    bonus = salary * 5 / 100
    print( bonus)