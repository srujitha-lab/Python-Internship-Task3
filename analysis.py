import pandas as pd
import matplotlib.pyplot as plt

# Create dataset (no CSV file needed)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Age": [25, 30, 35, 28, 40, None, 29],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "IT", "Finance"],
    "Salary": [40000, 60000, 65000, 50000, 45000, 70000, 52000]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)


# Data Cleaning
# # Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove duplicates (if any)
df = df.drop_duplicates()

print("\nCleaned Data:\n")
print(df)


# Filtering
high_salary = df[df["Salary"] > 50000]

print("\nEmployees with Salary > 50000:\n")
print(high_salary)


# Grouping
dept_avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:\n")
print(dept_avg_salary)


# Insights
print("\nInsights:")
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("Average Age:", df["Age"].mean())


# Optional Graph

dept_avg_salary.plot(kind="bar", title="Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()