import pandas as pd


df = pd.read_csv("sales_data.csv")


print("First 5 rows:\n")
print(df.head())


print("\nDataset Info:\n")
print(df.info())


print("\nStatistical Summary:\n")
print(df.describe())



print("\n🔹 Average Sales:", df['Sales'].mean())
print("🔹 Median Sales:", df['Sales'].median())
print("🔹 Standard Deviation of Sales:", df['Sales'].std())

print("\n🔹 Average Customer Age:", df['Customer_Age'].mean())
print("🔹 Average Customer Satisfaction:", df['Customer_Satisfaction'].mean())


df['Age_Group'] = pd.cut(df['Customer_Age'],
                         bins=[18,30,45,60,80],
                         labels=['Young','Mid-Age','Senior','Elder'])

print("\n🔹 Sales by Age Group:\n")
print(df.groupby('Age_Group', observed=False)['Sales'].mean())


business_summary = {
    "total_records": int(len(df)),
    "average_sales": round(float(df['Sales'].mean()), 2),
    "median_sales": round(float(df['Sales'].median()), 2),
    "sales_std_dev": round(float(df['Sales'].std()), 2),
    "average_customer_age": round(float(df['Customer_Age'].mean()), 2),
    "average_customer_satisfaction": round(float(df['Customer_Satisfaction'].mean()), 2),
    "top_age_group_by_sales": df.groupby(
        'Age_Group', observed=False
    )['Sales'].mean().idxmax()
}

print("\n📊 Clean Business Summary:\n")
print(business_summary)