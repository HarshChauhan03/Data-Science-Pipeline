import pandas as pd

df = pd.read_csv("step3_transformed.csv")

# Sales by category
sales_category = df.groupby("Category")["Sales"].sum()

# Sales by region
sales_region = df.groupby("Region")["Sales"].sum()

# Profit by category
profit_category = df.groupby("Category")["Profit"].sum()

summary = pd.DataFrame({
    "Sales_by_Category": sales_category,
    "Profit_by_Category": profit_category
})

print(summary)

summary.to_csv("summary_report.csv")

print("Summary report saved as summary_report.csv")