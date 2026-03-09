import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("step2_clean.csv")

# Convert date column
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Create new features
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month

# Encode categorical columns
encoder = LabelEncoder()

df["Category_encoded"] = encoder.fit_transform(df["Category"])
df["Region_encoded"] = encoder.fit_transform(df["Region"])

print("Transformation completed")

# Save transformed dataset
df.to_csv("step3_transformed.csv", index=False)

print("Transformed data saved as step3_transformed.csv")