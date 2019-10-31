import pandas as pd
df = pd.read_csv(
    "http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
df_sex = df.groupby(['sex'])
# print(df_sex.mean())
print(df_sex.head())
# print(df[ df['salary'] > 120000])
# print(df[ df['salary'] > 120000])
# print(df.cumsum())
