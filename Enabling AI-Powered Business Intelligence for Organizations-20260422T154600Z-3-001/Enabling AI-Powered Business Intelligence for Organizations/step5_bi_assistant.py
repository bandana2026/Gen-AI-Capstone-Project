import pandas as pd
import ollama

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create Age Groups
df['Age_Group'] = pd.cut(
    df['Customer_Age'],
    bins=[18, 30, 45, 60, 80],
    labels=['Young', 'Mid-Age', 'Senior', 'Elder']
)

# Create business summary
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

print("📊 InsightForge BI Assistant Ready.")
print("Type your question or type 'exit' to quit.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Goodbye 👋")
        break

    prompt = f"""
    You are an AI Business Intelligence Assistant.

    Use the dataset summary below to answer the user's question clearly and professionally.

    Dataset Summary:
    {summary_text}

    User Question:
    {user_question}
    """

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\n🤖 AI Response:\n")
    print(response['message']['content'])
    print("\n---------------------------------\n")