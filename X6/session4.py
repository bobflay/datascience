import pandas as pd

# load the dataset from a url

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# print("original data")
# # print(df.head())

pd.set_option('display.max_rows', None);

# print(df.info())

# print(df.describe())

data  = {'score': [1, None, 3, 2, 100,None]}
df2 = pd.DataFrame(data)
# # mean_score = df2['score'].mean()
# # print("mean score: ", mean_score)

# std = df2['score'].std()
# print("std score: ", std)


# print(df.columns)

# print(df.shape)

#detect null values
# print("null value in df2")
# print(df2.isnull().sum())

# print('data frame with null values')
# df2.dropna(inplace=True)
# print(df2)


# print(df[df['total_bill']>20])

# print(df[(df['total_bill']>20) & (df['tip']>3)])




print(df.groupby('sex')['tip'].mean())

print(df.groupby(['sex','smoker'])['tip'].mean())