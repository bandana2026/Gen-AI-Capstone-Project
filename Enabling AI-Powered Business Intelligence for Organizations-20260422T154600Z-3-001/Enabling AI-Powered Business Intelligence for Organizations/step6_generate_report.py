from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Image
import pandas as pd
import ollama

# Load dataset
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
You are a senior Business Intelligence consultant.
Generate executive-level insights in structured bullet format for a board meeting.

Dataset Summary:
{summary_text}
"""

response = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": prompt}]
)

insights = response['message']['content']

# Create PDF
doc = SimpleDocTemplate("Executive_BI_Report.pdf")
elements = []

styles = getSampleStyleSheet()
elements.append(Paragraph("<b>Executive Business Intelligence Report</b>", styles['Title']))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph(insights.replace("\n", "<br/>"), styles['Normal']))

doc.build(elements)

print("✅ Executive_BI_Report.pdf generated successfully!")