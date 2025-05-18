import pandas as pd

df = pd.read_csv('/Users/bob/Courses/Data Science/Course4_/dataset.csv')

print(df.head()) # print the first 5 rows of the dataframe


print(df.info()) # print the information about the dataframe

print(df.describe()) # print the summary statistics of the dataframe

# Check for missing values
print(df.isnull().sum())

numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("Numerical Columns:", numerical_cols)
print("Categorical Columns:", categorical_cols)



df = df.dropna(axis=0)  # Drop rows with missing values
df = df.dropna(axis=1)  # Drop columns with missing values