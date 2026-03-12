import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("step3_transformed.csv")

# Sales distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.savefig("Figure_1.png")

print("Visualization saved as Figure_1.png")