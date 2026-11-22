"""
Coforge Enterprise Data Engineering
Pandas Practice Test - Questions 1 to 55

Expected CSV files:
    data/employees/it_employees.csv
    data/employees/hr_employees.csv
    data/employees/finance_employees.csv
    data/employees/sales_employees.csv
    data/employees/operations_employees.csv

Install Pandas if required:
    pip install pandas
"""

import pandas as pd
from pathlib import Path


# ------------------------------------------------------------
# SETUP: Locate the folder containing the five employee CSVs
# ------------------------------------------------------------

# By default, this script expects a "data/employees" folder
# beside test.py. If your CSVs are somewhere else, change this path.
BASE_PATH = Path(__file__).resolve().parent / "data" / "employees"

# If test.py is in a different folder, you can use an absolute path:
# BASE_PATH = Path(r"C:\Users\YourName\Project\data\employees")


# ============================================================
# SECTION 1: CSV LOADING AND DATAFRAME OPERATIONS (Q1-Q10)
# ============================================================

# Q1. Read all five departmental CSV files into separate Pandas DataFrames.
it_df = pd.read_csv(BASE_PATH / "it_employees.csv")
hr_df = pd.read_csv(BASE_PATH / "hr_employees.csv")
finance_df = pd.read_csv(BASE_PATH / "finance_employees.csv")
sales_df = pd.read_csv(BASE_PATH / "sales_employees.csv")
operations_df = pd.read_csv(BASE_PATH / "operations_employees.csv")


# Q2. Combine all five DataFrames into one employee_df using pd.concat().
employee_df = pd.concat(
    [it_df, hr_df, finance_df, sales_df, operations_df],
    ignore_index=True
)


# Q3. Display the first 20 employee records from the consolidated DataFrame.
print(employee_df.head(20))


# Q4. Display the last 20 employee records.
print(employee_df.tail(20))


# Q5. Find the total number of employees across all departments.
print(employee_df.shape[0])


# Q6. Display the column names and data types of employee_df.
employee_df.info()
print(employee_df.dtypes)


# Q7. Check whether any column contains missing values.
print(employee_df.isnull().sum())


# Q8. Identify duplicate records based on emp_id.
print(employee_df[employee_df.duplicated(subset="emp_id", keep=False)])


# Q9. Display the number of employees in each department.
print(employee_df["department"].value_counts())


# Q10. Find the total number of unique cities in the dataset.
print(employee_df["city"].nunique())


# ============================================================
# SECTION 2: BASIC FILTERING AND SELECTION (Q11-Q20)
# ============================================================

# Q11. Display all employees working in the IT department.
print(employee_df[employee_df["department"] == "IT"])


# Q12. Find employees working in the Finance department.
print(employee_df[employee_df["department"] == "Finance"])


# Q13. Display employees whose salary is greater than Rs. 100,000.
print(employee_df[employee_df["salary"] > 100000])


# Q14. Find employees earning between Rs. 50,000 and Rs. 90,000.
print(employee_df[employee_df["salary"].between(50000, 90000)])


# Q15. Display all employees located in Pune.
print(employee_df[employee_df["city"] == "Pune"])


# Q16. Find employees working in IT and located in Bangalore.
print(employee_df[
    (employee_df["department"] == "IT") &
    (employee_df["city"] == "Bangalore")
])


# Q17. Display Finance employees earning more than Rs. 80,000.
print(employee_df[
    (employee_df["department"] == "Finance") &
    (employee_df["salary"] > 80000)
])


# Q18. Find employees belonging to either HR or Sales.
print(employee_df[employee_df["department"].isin(["HR", "Sales"])])


# Q19. Display employees whose salary is less than Rs. 40,000
#      and who work in Chennai.
print(employee_df[
    (employee_df["salary"] < 40000) &
    (employee_df["city"] == "Chennai")
])


# Q20. Find all employees whose city is not Mumbai.
print(employee_df[employee_df["city"] != "Mumbai"])


# ============================================================
# SECTION 3: SUM AND TOTAL SALARY CALCULATIONS (Q21-Q30)
# ============================================================

# Q21. Calculate the total salary expenditure across all five departments.
print(employee_df["salary"].sum())


# Q22. Calculate the total salary paid to IT employees.
print(employee_df.loc[employee_df["department"] == "IT", "salary"].sum())


# Q23. Calculate the total salary paid to HR employees.
print(employee_df.loc[employee_df["department"] == "HR", "salary"].sum())


# Q24. Calculate the total salary paid to Finance employees.
print(employee_df.loc[employee_df["department"] == "Finance", "salary"].sum())


# Q25. Calculate the total salary paid to Sales employees.
print(employee_df.loc[employee_df["department"] == "Sales", "salary"].sum())


# Q26. Calculate the total salary paid to Operations employees.
print(employee_df.loc[
    employee_df["department"] == "Operations", "salary"
].sum())


# Q27. Calculate department-wise total salary expenditure using groupby().
print(employee_df.groupby("department")["salary"].sum())


# Q28. Calculate city-wise total salary expenditure.
print(employee_df.groupby("city")["salary"].sum())


# Q29. Find the combined salary expenditure for IT and Finance.
print(employee_df[
    employee_df["department"].isin(["IT", "Finance"])
]["salary"].sum())


# Q30. Calculate each department's percentage contribution to the company's
#      total salary expenditure.
department_salary = employee_df.groupby("department")["salary"].sum()
department_percentage = (
    department_salary / employee_df["salary"].sum()
) * 100

print(department_percentage)


# ============================================================
# SECTION 4: MAX, MIN AND AVG OPERATIONS (Q31-Q40)
# ============================================================

# Q31. Find the maximum salary across the company.
print(employee_df["salary"].max())


# Q32. Find the minimum salary across the company.
print(employee_df["salary"].min())


# Q33. Calculate the average salary of all employees.
print(employee_df["salary"].mean())


# Q34. Find the maximum salary in each department.
print(employee_df.groupby("department")["salary"].max())


# Q35. Find the minimum salary in each department.
print(employee_df.groupby("department")["salary"].min())


# Q36. Calculate the average salary in each department.
print(employee_df.groupby("department")["salary"].mean())


# Q37. Find the maximum salary in each city.
print(employee_df.groupby("city")["salary"].max())


# Q38. Find the minimum salary in each city.
print(employee_df.groupby("city")["salary"].min())


# Q39. Calculate the average salary for employees in Pune.
print(employee_df.loc[employee_df["city"] == "Pune", "salary"].mean())


# Q40. Find the difference between maximum and minimum salary
#      for every department.
department_salary_range = employee_df.groupby("department")["salary"].agg(
    lambda salary: salary.max() - salary.min()
)

print(department_salary_range)


# ============================================================
# SECTION 5: GROUP BY - DEPARTMENT AND CITY ANALYSIS (Q41-Q50)
# ============================================================

# Q41. Group employees by department and calculate employee count.
print(employee_df.groupby("department")["emp_id"].count())


# Q42. Group employees by city and calculate employee count.
print(employee_df.groupby("city")["emp_id"].count())


# Q43. Group by department and calculate total salary, average salary,
#      minimum salary and maximum salary in one DataFrame.
department_summary = employee_df.groupby("department")["salary"].agg(
    total_salary="sum",
    average_salary="mean",
    minimum_salary="min",
    maximum_salary="max"
)

print(department_summary)


# Q44. Group by department and city and calculate total salary.
print(employee_df.groupby(["department", "city"])["salary"].sum())


# Q45. Group by department and city and calculate average salary.
print(employee_df.groupby(["department", "city"])["salary"].mean())


# Q46. Group by department and city and calculate employee count.
print(employee_df.groupby(["department", "city"])["emp_id"].count())


# Q47. Find the department with the highest total salary expenditure.
department_totals = employee_df.groupby("department")["salary"].sum()
print(department_totals.idxmax())


# Q48. Find the department with the lowest average salary.
department_averages = employee_df.groupby("department")["salary"].mean()
print(department_averages.idxmin())


# Q49. Find the city with the highest number of employees.
city_employee_count = employee_df.groupby("city")["emp_id"].count()
print(city_employee_count.idxmax())


# Q50. Create a department-wise salary summary sorted by total salary
#      in descending order.
department_salary_report = employee_df.groupby("department")["salary"].agg(
    total_salary="sum",
    average_salary="mean"
).sort_values("total_salary", ascending=False)

print(department_salary_report)


# ============================================================
# SECTION 6: HAVING-STYLE GROUP FILTERING (Q51-Q55)
# ============================================================

# Q51. Find departments whose total salary expenditure exceeds Rs. 10,000,000.
department_total = employee_df.groupby("department")["salary"].sum()
print(department_total[department_total > 10000000])


# Q52. Find departments whose average salary exceeds Rs. 90,000.
department_avg = employee_df.groupby("department")["salary"].mean()
print(department_avg[department_avg > 90000])


# Q53. Find departments whose minimum salary is greater than Rs. 25,000.
department_min = employee_df.groupby("department")["salary"].min()
print(department_min[department_min > 25000])


# Q54. Find departments whose maximum salary exceeds Rs. 140,000.
department_max = employee_df.groupby("department")["salary"].max()
print(department_max[department_max > 140000])


# Q55. Find cities where the total salary expenditure exceeds Rs. 15,000,000.
city_total = employee_df.groupby("city")["salary"].sum()
print(city_total[city_total > 15000000])


# ------------------------------------------------------------
# END OF QUESTIONS 1-55
# ------------------------------------------------------------
#============================================================
#SECTION 6: HAVING-STYLE GROUP FILTERING (Q56-Q60)
#============================================================

# Q56. Find department-city combinations whose average salary exceeds Rs. 100,000.

dept_city_avg = employee_df.groupby(
    ["department", "city"]
)["salary"].mean()

print(dept_city_avg[dept_city_avg > 100000])


# Q57. Find departments having more than 150 employees.

department_count = employee_df.groupby(
    "department"
)["emp_id"].count()

print(department_count[department_count > 150])


# Q58. Find cities having more than 100 employees.

city_count = employee_df.groupby(
    "city"
)["emp_id"].count()

print(city_count[city_count > 100])


# Q59. Find department-city combinations whose total salary exceeds Rs. 3,000,000.

dept_city_total = employee_df.groupby(
    ["department", "city"]
)["salary"].sum()

print(dept_city_total[dept_city_total > 3000000])


# Q60. Find departments whose average salary is greater than the overall company average salary.

overall_avg_salary = employee_df["salary"].mean()

department_avg_salary = employee_df.groupby(
    "department"
)["salary"].mean()

print(department_avg_salary[department_avg_salary > overall_avg_salary])


#============================================================
#SECTION 7: MULTIPLE AGGREGATIONS AND ADVANCED GROUPBY (Q61-Q70)
#============================================================

# Q61. Create a department-wise summary containing total salary,
# average salary, maximum salary, minimum salary and employee count.

department_summary = employee_df.groupby("department").agg(
    total_salary=("salary", "sum"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
    minimum_salary=("salary", "min"),
    employee_count=("emp_id", "count")
)

print(department_summary)


# Q62. Create a city-wise summary containing total salary,
# average salary and employee count.

city_summary = employee_df.groupby("city").agg(
    total_salary=("salary", "sum"),
    average_salary=("salary", "mean"),
    employee_count=("emp_id", "count")
)

print(city_summary)


# Q63. Calculate the salary range (maximum minus minimum)
# for every department.

salary_range = employee_df.groupby("department")["salary"].agg(
    lambda x: x.max() - x.min()
)

print(salary_range)


# Q64. Calculate the salary standard deviation for each department.

print(employee_df.groupby("department")["salary"].std())


# Q65. Calculate the median salary for each department.

print(employee_df.groupby("department")["salary"].median())


# Q66. Calculate the 25th and 75th salary percentiles for each department.

department_percentiles = employee_df.groupby(
    "department"
)["salary"].quantile([0.25, 0.75])

print(department_percentiles)


# Q67. Find the top three departments by average salary.

top_departments = employee_df.groupby(
    "department"
)["salary"].mean().nlargest(3)

print(top_departments)


# Q68. Find the top three cities by total salary expenditure.

top_cities = employee_df.groupby(
    "city"
)["salary"].sum().nlargest(3)

print(top_cities)


# Q69. Find the department-city combination with the highest average salary.

dept_city_avg = employee_df.groupby(
    ["department", "city"]
)["salary"].mean()

print(dept_city_avg.idxmax())
print(dept_city_avg.max())


# Q70. Calculate each department's share of total employees
# and total company salary.

department_report = employee_df.groupby("department").agg(
    employee_count=("emp_id", "count"),
    total_salary=("salary", "sum")
)

department_report["employee_share_percent"] = (
    department_report["employee_count"]
    / employee_df.shape[0]
) * 100

department_report["salary_share_percent"] = (
    department_report["total_salary"]
    / employee_df["salary"].sum()
) * 100

print(department_report)


#============================================================
#SECTION 8: MERGE AND JOIN OPERATIONS (Q71-Q80)
#============================================================

# Q71. Create a department salary summary DataFrame and merge it
# with employee_df using department.

department_salary_summary = employee_df.groupby(
    "department"
)["salary"].sum().reset_index(name="department_total_salary")

merged_df = pd.merge(
    employee_df,
    department_salary_summary,
    on="department"
)

print(merged_df)


# Q72. Create a city salary summary DataFrame and merge it with employee_df.

city_salary_summary = employee_df.groupby(
    "city"
)["salary"].sum().reset_index(name="city_total_salary")

merged_df = pd.merge(
    employee_df,
    city_salary_summary,
    on="city"
)

print(merged_df)


# Q73. Create a department employee-count DataFrame and merge it
# with employee_df.

department_count_df = employee_df.groupby(
    "department"
)["emp_id"].count().reset_index(name="department_employee_count")

merged_df = pd.merge(
    employee_df,
    department_count_df,
    on="department"
)

print(merged_df)


# Q74. Create a department average-salary DataFrame and merge it
# with employee_df.

department_avg_df = employee_df.groupby(
    "department"
)["salary"].mean().reset_index(name="department_avg_salary")

merged_df = pd.merge(
    employee_df,
    department_avg_df,
    on="department"
)

print(merged_df)


# Q75. After merging department averages, find employees earning
# more than their department's average salary.

above_avg_salary = merged_df[
    merged_df["salary"] > merged_df["department_avg_salary"]
]

print(above_avg_salary)


# Q76. After merging city averages, find employees earning
# less than their city's average salary.

city_avg_df = employee_df.groupby(
    "city"
)["salary"].mean().reset_index(name="city_avg_salary")

city_merged_df = pd.merge(
    employee_df,
    city_avg_df,
    on="city"
)

below_city_avg = city_merged_df[
    city_merged_df["salary"] < city_merged_df["city_avg_salary"]
]

print(below_city_avg)


# Q77. Create separate department salary-total and employee-count
# summary DataFrames and merge them.

dept_salary_df = employee_df.groupby(
    "department"
)["salary"].sum().reset_index(name="total_salary")

dept_count_df = employee_df.groupby(
    "department"
)["emp_id"].count().reset_index(name="employee_count")

department_summary_df = pd.merge(
    dept_salary_df,
    dept_count_df,
    on="department"
)

print(department_summary_df)


# Q78. Merge department maximum-salary data with employee_df and
# identify employees earning the department maximum.

department_max_df = employee_df.groupby(
    "department"
)["salary"].max().reset_index(name="department_max_salary")

merged_max_df = pd.merge(
    employee_df,
    department_max_df,
    on="department"
)

top_earners = merged_max_df[
    merged_max_df["salary"]
    == merged_max_df["department_max_salary"]
]

print(top_earners)


# Q79. Create department-city salary and employee-count summaries
# and merge them using both department and city.

salary_summary = employee_df.groupby(
    ["department", "city"]
)["salary"].sum().reset_index(name="total_salary")

count_summary = employee_df.groupby(
    ["department", "city"]
)["emp_id"].count().reset_index(name="employee_count")

dept_city_summary = pd.merge(
    salary_summary,
    count_summary,
    on=["department", "city"]
)

print(dept_city_summary)


# Q80. Demonstrate inner, left, right and outer joins.

department_reference = employee_df[
    ["department"]
].drop_duplicates()

inner_join = pd.merge(
    department_salary_summary,
    department_reference,
    on="department",
    how="inner"
)

left_join = pd.merge(
    department_salary_summary,
    department_reference,
    on="department",
    how="left"
)

right_join = pd.merge(
    department_salary_summary,
    department_reference,
    on="department",
    how="right"
)

outer_join = pd.merge(
    department_salary_summary,
    department_reference,
    on="department",
    how="outer"
)

print(inner_join)
print(left_join)
print(right_join)
print(outer_join)


#============================================================
#SECTION 9: ADVANCED SALARY ANALYTICS (Q81-Q90)
#============================================================

# Q81. Find the top 10 highest-paid employees in the company.

print(employee_df.nlargest(10, "salary"))


# Q82. Find the five lowest-paid employees in each department.

lowest_paid = employee_df.groupby(
    "department",
    group_keys=False
).apply(lambda x: x.nsmallest(5, "salary"))

print(lowest_paid)


# Q83. Rank employees by salary within their department.

employee_df["department_salary_rank"] = employee_df.groupby(
    "department"
)["salary"].rank(
    ascending=False,
    method="dense"
)

print(employee_df)


# Q84. Calculate each employee's salary difference
# from department average.

department_avg = employee_df.groupby(
    "department"
)["salary"].transform("mean")

employee_df["salary_difference"] = (
    employee_df["salary"] - department_avg
)

print(employee_df)


# Q85. Calculate each employee's salary percentage
# above or below department average.

employee_df["salary_percent_difference"] = (
    (employee_df["salary"] - department_avg)
    / department_avg
) * 100

print(employee_df)


# Q86. Calculate cumulative salary expenditure
# within each department ordered by salary descending.

employee_df = employee_df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)

employee_df["cumulative_salary"] = employee_df.groupby(
    "department"
)["salary"].cumsum()

print(employee_df)


# Q87. Find percentage of employees earning more than
# Rs. 100,000 in each department.

high_salary_percent = employee_df.groupby(
    "department"
)["salary"].apply(
    lambda x: (x > 100000).mean() * 100
)

print(high_salary_percent)


# Q88. Calculate annual salary expenditure assuming
# salary contains monthly salaries.

annual_salary_expenditure = employee_df["salary"].sum() * 12

print(annual_salary_expenditure)


# Q89. Calculate additional monthly payroll cost if everyone
# receives a 10% salary increase.

additional_cost = employee_df["salary"].sum() * 0.10

print(additional_cost)


# Q90. Calculate department-wise additional payroll cost.

hike_rates = {
    "IT": 0.12,
    "HR": 0.08,
    "Finance": 0.10,
    "Sales": 0.15,
    "Operations": 0.07
}

department_payroll = employee_df.groupby(
    "department"
)["salary"].sum()

additional_payroll_cost = department_payroll * pd.Series(hike_rates)

print(additional_payroll_cost)


#============================================================
#SECTION 10: ENTERPRISE REPORTING AND CAPSTONE CHALLENGES (Q91-Q100)
#============================================================

# Q91. Create consolidated department-wise management report.

management_report = employee_df.groupby("department").agg(
    employee_count=("emp_id", "count"),
    total_salary=("salary", "sum"),
    average_salary=("salary", "mean"),
    minimum_salary=("salary", "min"),
    maximum_salary=("salary", "max")
)

print(management_report)


# Q92. Create city-wise salary expenditure report.

city_report = employee_df.groupby("city")["salary"].sum()\
    .sort_values(ascending=False)

print(city_report)


# Q93. Create a department-city pivot table showing
# total salary expenditure.

salary_pivot = pd.pivot_table(
    employee_df,
    values="salary",
    index="department",
    columns="city",
    aggfunc="sum",
    fill_value=0
)

print(salary_pivot)


# Q94. Create a department-city pivot table showing employee count.

employee_count_pivot = pd.pivot_table(
    employee_df,
    values="emp_id",
    index="department",
    columns="city",
    aggfunc="count",
    fill_value=0
)

print(employee_count_pivot)


# Q95. Identify employees belonging to the top 10% salaries
# within their departments.

top_10_percent = employee_df.groupby(
    "department"
).apply(
    lambda x: x[
        x["salary"] >= x["salary"].quantile(0.90)
    ]
)

print(top_10_percent)


# Q96. Find departments where more than 50% of employees earn
# above overall company average salary.

company_avg = employee_df["salary"].mean()

department_above_avg = employee_df.groupby(
    "department"
)["salary"].apply(
    lambda x: (x > company_avg).mean() * 100
)

print(department_above_avg[department_above_avg > 50])


# Q97. Create salary distribution report.

salary_bands = pd.cut(
    employee_df["salary"],
    bins=[0, 40000, 80000, 120000, float("inf")],
    labels=[
        "Below 40000",
        "40000-79999",
        "80000-119999",
        "120000+"
    ]
)

print(salary_bands.value_counts())


# Q98. Calculate percentage contribution of every city to each
# department's salary expenditure.

dept_city_salary = employee_df.groupby(
    ["department", "city"]
)["salary"].sum()

department_total_salary = employee_df.groupby(
    "department"
)["salary"].sum()

city_contribution = (
    dept_city_salary
    / department_total_salary
) * 100

print(city_contribution)


# Q99. Export payroll analytics report into Excel workbook.

with pd.ExcelWriter("Payroll_Analytics_Report.xlsx") as writer:

    management_report.to_excel(
        writer,
        sheet_name="Department Summary"
    )

    city_report.to_excel(
        writer,
        sheet_name="City Summary"
    )

    salary_pivot.to_excel(
        writer,
        sheet_name="Salary Pivot"
    )

    employee_count_pivot.to_excel(
        writer,
        sheet_name="Employee Count Pivot"
    )


# Q100. Build reusable reporting function.

def generate_reports():

    department_summary = employee_df.groupby("department").agg(
        total_salary=("salary", "sum"),
        average_salary=("salary", "mean"),
        employee_count=("emp_id", "count")
    )

    city_summary = employee_df.groupby("city").agg(
        total_salary=("salary", "sum"),
        average_salary=("salary", "mean"),
        employee_count=("emp_id", "count")
    )

    company_summary = pd.DataFrame({
        "total_employees": [employee_df.shape[0]],
        "total_salary": [employee_df["salary"].sum()],
        "average_salary": [employee_df["salary"].mean()]
    })

    return (
        department_summary,
        city_summary,
        company_summary
    )


department_summary, city_summary, company_summary = generate_reports()

print(department_summary)
print(city_summary)
print(company_summary)