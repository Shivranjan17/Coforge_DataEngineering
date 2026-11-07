import pandas as pd
import numpy as np

# Read the HSBC customer dataset
df = pd.read_csv("HSBC_Synthetic_Banking_Customers.csv")

# Convert account balance column into a NumPy array
balance_arr = df["Account_Balance"].to_numpy()

# Display array properties
print("NDIM:", balance_arr.ndim)
print("SHAPE:", balance_arr.shape)
print("SIZE:", balance_arr.size)
print("DTYPE:", balance_arr.dtype)

# Find minimum and maximum account balances
print("Minimum Balance:", np.min(balance_arr))
print("Maximum Balance:", np.max(balance_arr))

# Calculate basic statistics for balances
print("Balance Sum:", np.sum(balance_arr))
print("Balance Mean:", np.mean(balance_arr))
print("Balance Median:", np.median(balance_arr))
print("Balance Std:", np.std(balance_arr))

# Calculate balance percentiles
print("25th Percentile:", np.percentile(balance_arr, 25))
print("50th Percentile:", np.percentile(balance_arr, 50))
print("75th Percentile:", np.percentile(balance_arr, 75))

# Display balances greater than 500000
print("Balances > 500000")
print(balance_arr[balance_arr > 500000])

# Convert credit scores into NumPy array
credit_arr = df["Credit_Score"].to_numpy()

# Find customers with credit score less than 650
print("Credit Score < 650")
print(credit_arr[credit_arr < 650])

# Sort balances in ascending order
print("Ascending Sort")
print(np.sort(balance_arr))

# Sort balances in descending order
print("Descending Sort")
print(np.sort(balance_arr)[::-1])

# Calculate total deposits and withdrawals
print("Total Deposits:", np.sum(df["Monthly_Deposit"]))
print("Total Withdrawals:", np.sum(df["Monthly_Withdrawal"]))

# Increase all balances by 5 percent
new_balance = balance_arr * 1.05
print("5% Increased Balance")
print(new_balance)

# Classify balances as High or Low
balance_class = np.where(balance_arr > 500000, "High", "Low")
print(balance_class)

# Categorize balances into Low, Medium and High
conditions = [
    balance_arr < 100000,
    (balance_arr >= 100000) & (balance_arr <= 500000),
    balance_arr > 500000
]

choices = ["Low", "Medium", "High"]

balance_category = np.select(conditions, choices, default="Unknown")

print("Balance Categories")
print(balance_category)

# Calculate deposit to income ratio safely
deposit_income_ratio = np.where(
    df["Monthly_Income"] != 0,
    df["Monthly_Deposit"] / df["Monthly_Income"],
    0
)

print("Deposit Income Ratio")
print(deposit_income_ratio)

# Find records where withdrawals are greater than deposits
print("Withdrawal Greater Than Deposit")
print(df[df["Monthly_Withdrawal"] > df["Monthly_Deposit"]])

# Find unique credit scores and their frequencies
scores, counts = np.unique(credit_arr, return_counts=True)

print("Unique Credit Scores")
print(scores)

print("Count of Each Score")
print(counts)

# Find indexes of top 5 balances
largest_idx = np.argsort(balance_arr)[-5:]

print("Top 5 Balance Indexes")
print(largest_idx)

# Perform Min-Max normalization
min_bal = np.min(balance_arr)
max_bal = np.max(balance_arr)

if max_bal != min_bal:
    normalized = (balance_arr - min_bal) / (max_bal - min_bal)
else:
    normalized = balance_arr

print("Normalized Balance")
print(normalized)

# Calculate z-score for balances
mean_bal = np.mean(balance_arr)
std_bal = np.std(balance_arr)

if std_bal != 0:
    zscore = (balance_arr - mean_bal) / std_bal
else:
    zscore = balance_arr

print("Z Score")
print(zscore)

# Create a 2D array of balance, deposit and withdrawal
bank_array = np.column_stack((
    df["Account_Balance"],
    df["Monthly_Deposit"],
    df["Monthly_Withdrawal"]
))

print("2D Banking Array")
print(bank_array)

# Calculate column-wise totals
print("Column Totals")
print(bank_array.sum(axis=0))

# Find correlation between income and balance
correlation = np.corrcoef(
    df["Monthly_Income"],
    df["Account_Balance"]
)

print("Income vs Balance Correlation")
print(correlation)

# Display first 10 rows
print("First 10 Rows")
print(df.head(10))

# Display last 10 rows
print("Last 10 Rows")
print(df.tail(10))

# Check dataframe shape
print("Shape")
print(df.shape)

# Display all column names
print("Columns")
print(df.columns)

# Display data types
print("Data Types")
print(df.dtypes)

# Display dataframe information
df.info()

# Generate descriptive statistics
print("Statistical Summary")
print(df.describe())

# Check missing values
print("Missing Values")
print(df.isnull().sum())

# Check duplicate customer IDs
print("Duplicate Customer IDs")
print(df["Customer_ID"].duplicated().sum())

# Select important customer columns
print(df[[
    "Customer_Name",
    "City",
    "Account_Balance",
    "Credit_Score"
]])

# Filter customers aged between 25 and 40
age_filter = df[
    (df["Age"] >= 25) &
    (df["Age"] <= 40)
]

print("Customers Between 25 and 40")
print(age_filter)

# Find active savings account customers
active_savings = df[
    (df["Account_Status"] == "Active") &
    (df["Account_Type"] == "Savings")
]

print("Active Savings Accounts")
print(active_savings)

# Sort by balance and income in descending order
sorted_df = df.sort_values(
    ["Account_Balance", "Monthly_Income"],
    ascending=False
)

print("Sorted Data")
print(sorted_df)

# Create new column for net monthly flow
df["Net_Monthly_Flow"] = (
    df["Monthly_Deposit"] -
    df["Monthly_Withdrawal"]
)

print(df.head())

# Calculate city-wise total balance
city_balance = df.groupby("City")["Account_Balance"].sum()

print("City Wise Balance")
print(city_balance)

# Calculate average income by account type
avg_income = df.groupby("Account_Type")["Monthly_Income"].mean()

print("Average Income By Account Type")
print(avg_income)

# Calculate branch-wise deposit and withdrawal totals
branch_totals = df.groupby("Branch")[
    ["Monthly_Deposit", "Monthly_Withdrawal"]
].sum()

print("Branch Totals")
print(branch_totals)

# Generate branch balance statistics
branch_balance_stats = df.groupby("Branch")[
    "Account_Balance"
].agg(["min", "max", "mean", "median"])

print("Branch Balance Statistics")
print(branch_balance_stats)

# Create pivot table for balance by city and account type
pivot_table = pd.pivot_table(
    df,
    values="Account_Balance",
    index="City",
    columns="Account_Type",
    aggfunc="sum"
)

print("Pivot Table")
print(pivot_table)

# Create age groups
bins = [18, 25, 40, 60, 100]
labels = ["18-25", "26-40", "41-60", "61+"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

print(df[["Age", "Age_Group"]])

# Calculate balance difference from branch average
df["Balance_Difference"] = (
    df["Account_Balance"]
    -
    df.groupby("Branch")["Account_Balance"].transform("mean")
)

print(df[["Customer_Name", "Branch", "Balance_Difference"]])

# Create branch details dataframe
branch_details = pd.DataFrame({
    "Branch": ["Mumbai", "Pune", "Delhi"],
    "Region": ["West", "West", "North"]
})

# Merge customer and branch information
merged_df = pd.merge(
    df,
    branch_details,
    on="Branch",
    how="left",
    validate="many_to_one"
)

print("Merged Data")
print(merged_df.head())

# Find top 3 customers by balance in each city
top3 = (
    df.sort_values("Account_Balance", ascending=False)
      .groupby("City")
      .head(3)
)

print("Top 3 Customers In Each City")
print(top3)

# Create branch level summary
branch_summary = df.groupby("Branch").agg(
    Total_Balance=("Account_Balance", "sum"),
    Mean_Credit_Score=("Credit_Score", "mean"),
    Total_Net_Flow=("Net_Monthly_Flow", "sum")
)

# Count account status by branch
status_count = pd.crosstab(
    df["Branch"],
    df["Account_Status"]
)

# Join summary and status counts
branch_summary = branch_summary.join(status_count)

print("Branch Summary")
print(branch_summary)