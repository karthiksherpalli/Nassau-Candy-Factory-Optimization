import pandas as pd
import numpy as np
df = pd.read_csv("01_Dataset/Nassau_Candy_Cleaned.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
print("Dataset loaded successfully.")
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())
df["Profit Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Quarter"] = df["Order Date"].dt.quarter
df["Order Weekday"] = df["Order Date"].dt.day_name()
print("\nNew Features Created:")
print(df[["Sales","Gross Profit","Profit Margin %","Order Year","Order Month","Order Quarter","Order Weekday"]].head())
print("\nDataset Shape After Feature Engineering:")
print(df.shape)
df.to_csv("01_Dataset/Nassau_Candy_Featured.csv",index=False)
print("\nFeature engineered dataset saved successfully.")
print("Final Dataset Shape:", df.shape)