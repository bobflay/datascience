import pandas as pd

# Create a sample dataset
data = {
    "Name": ["John", "Sarah", "Michael", "Anna", "Sarah"],
    "Age": [25, 30, 28, 28, 30],
    "City": ["New York", "Los Angeles", "Chicago", "New York", "Los Angeles"]
}   

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# 1. Detect Duplicates
duplicates = df.duplicated()
print("\nDuplicate Rows Detected:")
print(df[duplicates])

# 2. Count the Number of Duplicates
num_duplicates = duplicates.sum()
print(f"\nNumber of Duplicate Rows: {num_duplicates}")

# 3. Remove Duplicate Rows
df_no_duplicates = df.drop_duplicates()
print("\nDataset After Removing Duplicates:")
print(df_no_duplicates)

# 4. Remove Duplicates Based on Specific Columns
# Example: Consider only 'Name' and 'City' columns to check duplicates
df_no_duplicates_specific = df.drop_duplicates(subset=['Name', 'City'])
print("\nDataset After Removing Duplicates Based on 'Name' and 'City':")
print(df_no_duplicates_specific)

# 5. Keep Specific Duplicates
# Example: Keep the first occurrence
df_keep_first = df.drop_duplicates(keep='first')
print("\nDataset Keeping the First Occurrence of Duplicates:")
print(df_keep_first)

# Example: Keep the last occurrence
df_keep_last = df.drop_duplicates(keep='last')
print("\nDataset Keeping the Last Occurrence of Duplicates:")
print(df_keep_last)

# Save the cleaned dataset
df_no_duplicates.to_csv("cleaned_dataset_no_duplicates.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_dataset_no_duplicates.csv'")