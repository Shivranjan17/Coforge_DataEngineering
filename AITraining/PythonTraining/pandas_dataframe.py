import pandas as pd 
employee_data={
    "Employee_ID":["E101","E102","E103","E104","E105","E106","E107","E108"],
    "Employee_Name":["Shiv","Atharva","Sahil","Shreyansh","Prince","Hitesh","Akashdeep","Pranjali"],
    "Department":["sales","HR","Sales","Finance","IT","Finance","IT","Finace"],
    "City":["Delhi","Pune","Mumbai","Bihar","Delhi","Pune","Pune","Pune"],
    "Salary":[65000,58000,72000,85000,68000,90000,76000,38223],
    "Experience":[5,4,5,6,7,3,4,6],
    "Rating":[5,5,5,6,3,2,4,5]

}
print("================Create Employee DataFrame=========")
employees_df = pd.DataFrame(employee_data)
print(employees_df)


#Step 5 - Inspect DataFrame
print("==================DataFrame Shapes========================")
print(employees_df.shape)
print(employees_df.columns)
print(employees_df.dtypes)
 
#step 6 - head()
print("=====First 5 records=====")
print(employees_df.head())
 
#First 3:
print("=====First 2 records=====")
print(employees_df.head(2))
 
#Step 6 : tail()
print("==========last 5 Records===============")
print(employees_df.tail())
 
#Last 2
print("=======Last 2 Records=========")
print(employees_df.tail(2))

print("================Describe=============")
employees_df.info()
print(employees_df["Employee_Name"])

#Select One Column
print("================Select One Column==========")
print(employees_df["Employee_Name"])

#Select Multiple Columns 
print("===========Select Multiple Columns==========")
print(employees_df[["Employee_Name","Salary"]])


result = employees_df[
    employees_df["Salary"]>80000
 ]
print("============Employee Salary >80000=============")
print(result)


result1 = employees_df["Salary"]>80000
print("============Employee Salary >80000=============")
print(result1)

Emp_Rating = employees_df[employees_df["Rating"]>4.5]
print(Emp_Rating)

Emp_City = employees_df[employees_df["City"]=="Delhi"]
print(Emp_City)   


result2 = employees_df[(employees_df["Salary"]>80000) & (employees_df["Rating"]>4.5)]
print(result2)

result3 = employees_df[(employees_df["Department"]=="IT") | (employees_df["Department"]=="Finance")]
print("==========result========")
print(result3)


result4 = employees_df[employees_df["Department"].isin(["Finance","IT"])]
print("=============Interview isin============")
print(result4)



employees_df["Annual_Salary"] = employees_df["Salary"] * 12
print(employees_df)


employees_df["Revised Salary"]=employees_df["Salary"]+employees_df["Salary"]*0.08
print(employees_df)


employees_df["Monthly Compunsation"]= employees_df["Salary"]+employees_df["Revised Salary"]
print(employees_df)

emp_mean = employees_df["Salary"].mean()
print(emp_mean)

emp_sum = employees_df["Salary"].sum()
print(emp_sum)

emp_max = employees_df["Salary"].max()
print(f"Max Salary is :{emp_max}")

emp_avg_rating = employees_df["Rating"].mean()
print(f"Avg Mean of Rating  :{emp_avg_rating}")


dept_count = employees_df["Department"].value_counts()
print(dept_count)

dept_len = len(employees_df["Department"])
print(dept_len)

dept = employees_df["Department"].nunique()
print(dept)

sort_salary = employees_df.sort_values(by="Salary")
print(sort_salary)

sort_salary_asc = employees_df.sort_values(by="Salary",ascending=False)
print(sort_salary_asc)


sort_salary_des = employees_df.sort_values(by="Salary",ascending=True)
print(sort_salary_des)


sort_salary_top = employees_df.sort_values(by="Salary",ascending=True).head(3)
print(sort_salary_top)

