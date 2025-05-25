import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd




# # Line plot
# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# plt.title('Basic Line Plot 2025')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()


# 📊 Bar Chart – Compare Categories
# 	•	Use When:
# You want to compare the size, count, or frequency of different categories.
# 	•	Examples:
# 	•	Revenue by product
# 	•	Number of users per country
# 	•	Average tip per day in a restaurant dataset
# 	•	Best For:
# Categorical data (nominal or ordinal)

# # Sample data
# categories = ['A', 'B', 'C', 'D']
# values = [10, 24, 36, 18]

# # Create bar chart
# plt.bar(categories, values, color='skyblue')
# plt.title('Bar Chart Example')
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.show()



# ⚫ Scatter Plot – Explore Relationships Between Two Variables
# 	•	Use When:
# You want to visualize the relationship or correlation between two continuous variables.
# 	•	Examples:
# 	•	Height vs. weight
# 	•	Price vs. size of a house
# 	•	Total bill vs. tip in a restaurant
# 	•	Best For:
# Continuous numeric data, especially to spot trends, clusters, or outliers.

# # Scatter plot example

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [5, 7, 4, 6, 8]

# # Create scatter plot
# plt.scatter(x, y, color='red', marker='o')
# plt.title('Scatter Plot Example')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.show()


# 📈 Histogram – Understand Distribution
# 	•	Use When:
# You want to see the distribution of a single continuous variable — how often values fall into specific ranges (bins).
# 	•	Examples:
# 	•	Distribution of customer ages
# 	•	Frequency of daily sales amounts
# 	•	Spread of exam scores


# # Generate random data
# data = np.random.randn(1000)

# # Create histogram
# plt.hist(data, bins=30, color='purple', edgecolor='black')
# plt.title('Histogram Example')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()


