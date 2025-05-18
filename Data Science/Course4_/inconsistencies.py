import pandas as pd

# Create a sample dataset
data = {
    "Name": ["John", "Sarah", "Michael", "Anna"],
    "City": ["New York", "new york", "Los Angeles ", "N.Y."],
    "Income": [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# 1. Standardize Text Case (e.g., Make All Text Lowercase)
df['City'] = df['City'].str.lower()
print("\nAfter Standardizing Text Case:")
print(df)

# 2. Remove Leading and Trailing Whitespaces
df['City'] = df['City'].str.strip()
print("\nAfter Removing Leading/Trailing Whitespaces:")
print(df)

# 3. Replace Inconsistent Values
# Map inconsistent or misspelled values to a standard format
city_mapping = {
    "new york": "new york",
    "n.y.": "new york",
    "los angeles": "los angeles"
}
df['City'] = df['City'].replace(city_mapping)
print("\nAfter Replacing Inconsistent Values:")
print(df)

# 4. Validate Unique Categories
# Check unique values in the 'City' column to confirm consistency
unique_cities = df['City'].unique()
print("\nUnique Cities After Fixing Inconsistencies:")
print(unique_cities)

# Save the cleaned dataset
df.to_csv("cleaned_dataset_fixed_inconsistencies.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_dataset_fixed_inconsistencies.csv'")