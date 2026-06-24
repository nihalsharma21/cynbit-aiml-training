import pandas as pd

data = {
    "Name": ["Ram", "Rahul", "Aman", "Priya"],
    "Age": [22, None, 19, 23],
    "Marks": [78, 93, 87, None]
}

df = pd.DataFrame(data)
print("Original Dataset: ")
print(df)
df_clean = df.dropna()
print("Dataset After Removing Null Values:")
print(df_clean)