import numpy as np
salary = np.array([65000,58000,72000,80000,85000,85000,68000,90000,76000])
print("============salary==================")
print(salary)


# Check Numpy Array Properties 

print("===========================salary Operations================")
print("Array :",salary)
print("Type :",type(salary))
print("Dimensions :",salary.ndim)
print("Shape :",salary.shape)
print("Size :",salary.size)
print("Data Type : ",salary.dtype)
salary = np.array([65000,58000,72000,80000,85000,85000,68000,90000,76000])


rating = np.array([4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3,4.2])
print("================Rating================")
print(rating)

#Check Properties
print("===============Ratings Properties===================")
print("Rating Shape",rating.shape)
print("Rating Size",rating.size)
print("Rating Data Type :",rating.dtype)


#Numpy Indexing
print("=====================Numpy Indexing=============")
print("First Salary :",salary[0])
print("Third Salary :",salary[2])
print("Last Salary :",salary[-1])
print("Second Last Salary :",salary[-2])
print("Third Last Salary :",salary[-3])


#Numpy Slicing
#First Three
print("====================Numpy Slicing======================")
print(salary[0:3])

#Last Three
print(salary[-3:])

#All except first two
print(salary[2:])


#Find Employees Earning Above 75000
#Business:Identify employees in higher salary bracket

print("===============Salary Above 75000===============")
high_salary=salary[salary>75000]
print("Employees Salary:",high_salary)
print("Employees Count:",len(high_salary))


#Find Employees with Rating Above 4.5
#Business: Identify high performing employees

print("=============high  performing employees==========")
high_rating = rating[rating>4.5]
print("High Ratings:",high_rating)
print("Number of Employees: ",len(high_rating))


#Conditional Salary Increment 
#Business : Employees earning below 70000 get 10% increment
#other employees receive 5%

new_salary = np.where(salary<70000,salary*1.10,salary *1.05)
print("Original Salary:",salary)
print("Updated Salary :",new_salary)

#performance Bonus
#Business Employees rated 4.5 or above receive 15% bonus
#Other employees receive 5%

print("=========Performance Bonus===========")
bonus = np.where(rating >=4.5,salary*0.15,salary*0.05)
print(bonus)


#Calculate Salary After Bonus
#Business:Calculate salary plus performance bonus

print("=========Salary After Bonus==============")
# Salary after bonus
salaru_with_bonus=salary+bonus
 
print("Original Salary: ",salary)
print("Bonus: ",bonus)
print("Salary after Salary: ",salaru_with_bonus)
