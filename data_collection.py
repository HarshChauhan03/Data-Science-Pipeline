import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Dataset Loaded Successfully")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

# Save raw data
df.to_csv("step1_raw.csv", index=False)

print("\nRaw dataset saved as step1_raw.csv")