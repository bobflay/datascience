import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["John", "Sarah", "Michael", "Anna"],
    "Age": [25, 30, np.nan, 28],
    "Income": [50000, np.nan, 45000, 52000],
    "City": ["New York", "Los Angeles", "New York", np.nan]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# Handling Missing Values

# 1. Mean Imputation (for 'Age')
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nAfter Mean Imputation (Age):")
print(df)

# 2. Median Imputation (for 'Income')
df['Income'] = df['Income'].fillna(df['Income'].median())
print("\nAfter Median Imputation (Income):")
print(df)

# 3. Mode Imputation (for 'City')
df['City'] = df['City'].fillna(df['City'].mode()[0])
print("\nAfter Mode Imputation (City):")
print(df)

# 4. Constant Value Imputation (optional, replacing NaN with 'Unknown')
df['City'] = df['City'].fillna('Unknown')
print("\nAfter Constant Value Imputation (City):")
print(df)

# Save the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.csv'")