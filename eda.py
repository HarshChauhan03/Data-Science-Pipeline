import pandas as pd

df = pd.read_csv("step3_transformed.csv")

print("Summary Statistics:")
print(df.describe())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nAverage Profit:")
print(df["Profit"].mean())

print("\nCategory Distribution:")
print(df["Category"].value_counts())

print("\nRegion Distribution:")
print(df["Region"].value_counts())