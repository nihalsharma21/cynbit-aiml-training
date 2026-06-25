import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Student": ["Rahul", "Priya", "Aman", "Ram"],
    "Marks": [72, 90, 68, 78]
}
df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(df["Student"], df["Marks"])
plt.title("Student Marks (Bar Chart)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.figure(figsize=(5, 5))
plt.pie(
    df["Marks"],
    labels=df["Student"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Marks Distribution (Pie Chart)")
plt.show()