import pandas as pd
df = pd.read_csv(r"C:\tennis-data\TML-Database\2025.csv")
print(df.shape)
print(df.head())
print(df.columns.tolist())
print(df.isna().sum())
print(df["surface"].value_counts())