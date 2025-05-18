import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Year": [2017, 2018, 2019, 2020, 2021],
    "Sales": [200, 220, 250, 270, 300],
    "Profit": [50, 60, 70, 80, 100],
    "Region": ["North", "South", "East", "West", "North"]
}

df = pd.DataFrame(data)
print(df)



# Bar Chart
# plt.figure(figsize=(8, 5))
# sns.barplot(x="Year", y="Sales", data=df)
# plt.title("Sales Over the Years")
# plt.xlabel("Year")
# plt.ylabel("Sales")
# plt.show()

# # Line Plot
# plt.figure(figsize=(8, 5))
# plt.plot(df["Year"], df["Sales"], marker='o', label="Sales")
# plt.plot(df["Year"], df["Profit"], marker='o', label="Profit", linestyle='--')
# plt.title("Sales and Profit Trends")
# plt.xlabel("Year")
# plt.ylabel("Values")
# plt.legend()
# plt.show()


# Scatter Plot
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x="Sales", y="Profit", hue="Region", data=df)
# plt.title("Sales vs. Profit by Region")
# plt.xlabel("Sales")
# plt.ylabel("Profit")
# plt.show()

# Histogram
# plt.figure(figsize=(8, 5))
# sns.histplot(df["Profit"], bins=5, kde=True)
# plt.title("Profit Distribution")
# plt.xlabel("Profit")
# plt.ylabel("Frequency")
# plt.show()


# import numpy as np

# # Stacked Bar Chart
# x = np.arange(len(df["Year"]))
# width = 0.4

# plt.figure(figsize=(8, 5))
# plt.bar(x - width/2, df["Sales"], width, label="Sales")
# plt.bar(x + width/2, df["Profit"], width, label="Profit")
# plt.xticks(x, df["Year"])
# plt.title("Sales vs Profit Comparison")
# plt.xlabel("Year")
# plt.ylabel("Values")
# plt.legend()
# plt.show()