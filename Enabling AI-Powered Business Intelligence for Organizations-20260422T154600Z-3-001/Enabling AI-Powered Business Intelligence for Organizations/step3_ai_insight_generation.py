import pandas as pd
import ollama


df = pd.read_csv("sales_data.csv")

df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[18, 30, 45, 60, 80],
    labels=['Young', 'Mid-Age', 'Senior', 'Elder']
)

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


summary_text = f"""
Total Records: {business_summary['total_records']}
Average Sales: {business_summary['average_sales']}
Median Sales: {business_summary['median_sales']}
Sales Standard Deviation: {business_summary['sales_std_dev']}
Average Customer Age: {business_summary['average_customer_age']}
Average Customer Satisfaction: {business_summary['average_customer_satisfaction']}
Top Revenue Age Group: {business_summary['top_age_group_by_sales']}
"""


prompt = f"""
You are a Senior Business Intelligence Consultant presenting to the Board of Directors.

Analyze the dataset summary carefully and generate a professional executive briefing.

Structure your response EXACTLY in the following sections:

=== Executive Performance Overview ===
- 3–4 bullet insights

=== Risk & Performance Gaps ===
- Identify measurable concerns

=== Revenue-Driving Segments ===
- Highlight strongest customer segments

=== Strategic Recommendations ===
- Provide 3 high-impact strategic actions
- Each action must include expected business outcome

Dataset Summary:
{summary_text}
"""

response = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": prompt}]
)

print("\n📈 AI Executive Insights:\n")
print(response['message']['content'])
