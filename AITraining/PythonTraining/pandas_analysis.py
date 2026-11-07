import pandas as pd
import numpy_operations as np
#Step2 - Create pandas Series
salary_series = pd.Series([65000,58000,72000,85000,68000,90000,76000])

print("============salary_series================")
print(salary_series)


print("===================Defining Properties================")
print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)

#Step 3 -Series with Custom Index
employee_series = pd.Series(
    ["Shiv","Atharva","Sahil","Shreyansh","Prince","Hitesh","Akashdeep","Pranjali"]
    ,
    index=["E101","E102","E103","E104","E105","E106","E107","E108"]
)
print("====================Series with  Custom Index===============")
print(employee_series)

#Retrive employees:
print("==============Employees Name with E103===========")
print(employee_series["E103"])
print("==================Employee Name with E106==========")
print(employee_series["E106"])