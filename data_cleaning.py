import pandas as pd

# Sample dataset with null values
data = {
    "Name": ["Nihal", "Rahul", "Priya"],
    "Age": [20, None, 19],
    "Grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Remove null values
df_clean = df.dropna()

print("\nDataset After Removing Null Values:")
print(df_clean)