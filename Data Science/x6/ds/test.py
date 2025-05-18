import pandas as pd

data = {
    'name':['John','Sarah','Michael','Anna','Sarah'],
    'age':[28,22,35,29,22],
    'city':['New York','Los Angeles','Chicago','Houston','Los Angeles'],
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#detect duplicate rows
duplicates = df.duplicated()
print("\nDuplicate Rows:")
print(df[duplicates])




