import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    "Name": ["John", "Sarah", "Michael", "Anna", "David"],
    "Age": [25, 30, 22, 28, 120],  # Outlier in 'Age'
    "Income": [50000, 60000, 45000, 70000, 1000000]  # Outlier in 'Income'
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

# 1. Detect Outliers Using Interquartile Range (IQR)
def detect_outliers_iqr(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

outliers_iqr_age = detect_outliers_iqr("Age")
outliers_iqr_income = detect_outliers_iqr("Income")
print("\nOutliers Detected (IQR) in Age:")
print(outliers_iqr_age)
print("\nOutliers Detected (IQR) in Income:")
print(outliers_iqr_income)

# 2. Detect Outliers Using Z-Score
def detect_outliers_zscore(column, threshold=3):
    z_scores = zscore(df[column])
    return df[np.abs(z_scores) > threshold]

outliers_zscore_age = detect_outliers_zscore("Age")
outliers_zscore_income = detect_outliers_zscore("Income")
print("\nOutliers Detected (Z-Score) in Age:")
print(outliers_zscore_age)
print("\nOutliers Detected (Z-Score) in Income:")
print(outliers_zscore_income)

# 3. Handle Outliers: Remove Outliers
def remove_outliers_iqr(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df_cleaned = remove_outliers_iqr("Income")
print("\nDataset After Removing Outliers in Income (IQR):")
print(df_cleaned)

# 4. Handle Outliers: Cap Outliers
def cap_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.clip(df[column], lower_bound, upper_bound)
    return df

df_capped = cap_outliers("Income")
print("\nDataset After Capping Outliers in Income (IQR):")
print(df_capped)

# 5. Visualize Outliers Using Boxplot
plt.boxplot(df["Income"])
plt.title("Income Boxplot (After Handling Outliers)")
plt.show()