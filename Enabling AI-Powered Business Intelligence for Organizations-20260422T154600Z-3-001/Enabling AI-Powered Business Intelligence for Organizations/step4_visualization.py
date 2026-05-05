import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create Age Group
df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[18, 30, 45, 60, 80],
    labels=['Young', 'Mid-Age', 'Senior', 'Elder']
)

# ==============================
# 1. Sales Distribution
# ==============================

plt.figure()
plt.hist(df['Sales'], bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# ==============================
# 2. Sales by Age Group
# ==============================

age_group_sales = df.groupby('Age_Group')['Sales'].mean()

plt.figure()
age_group_sales.plot(kind='bar')
plt.title("Average Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Sales")
plt.show()

# ==============================
# 3. Satisfaction vs Sales
# ==============================

plt.figure()
plt.scatter(df['Customer_Satisfaction'], df['Sales'])
plt.title("Customer Satisfaction vs Sales")
plt.xlabel("Customer Satisfaction")
plt.ylabel("Sales")
plt.show()