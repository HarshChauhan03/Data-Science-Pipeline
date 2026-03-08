import pandas as pd

# Load raw dataset
df = pd.read_csv("step1_raw.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing values
df.fillna(method="ffill", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicates removed")

# Save cleaned dataset
df.to_csv("step2_clean.csv", index=False)

print("\nClean dataset saved as step2_clean.csv")