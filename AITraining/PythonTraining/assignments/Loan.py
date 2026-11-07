salary = int(input("Monthly Salary: "))
credit_score = int(input("Credit Score: "))
existing_loan = int(input("Existing Loan Amount: "))
employment_type = input("Employment Type: ")

if salary > 80000 and credit_score > 750 and existing_loan < 20000:
    print("Loan Approved Immediately")
elif salary > 50000 and credit_score > 650:
    print("Loan Approved with Caution")
elif credit_score < 600:
    print("Loan Rejected")
else:
    print("Manual Review Required")
