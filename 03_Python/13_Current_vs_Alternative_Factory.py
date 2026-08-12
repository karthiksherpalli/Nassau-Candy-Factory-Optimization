import pandas as pd
orders = pd.read_csv("01_Dataset/Nassau_Candy_Factory_Mapped.csv")
dist = pd.read_csv("01_Dataset/Customer_Factory_Distances.csv")
df = orders.merge(dist,on=["Country/Region", "State/Province", "City", "Postal Code", "Region"],how="left")
df["Reallocation Needed"] = df["Factory"] != df["Nearest Factory"]
print("\n===== FACTORY REALLOCATION ANALYSIS =====")
print("Total Records:", len(df))
print("Reallocation Needed:", df["Reallocation Needed"].sum())
percentage = df["Reallocation Needed"].mean() * 100
print("Reallocation Percentage:", round(percentage, 2), "%")
print("\nCurrent Factory vs Nearest Factory:")
print(df.groupby(["Factory", "Nearest Factory"]).size()
.sort_values(ascending=False).head(15))
df.to_csv("01_Dataset/Current_vs_Alternative_Factory.csv",index=False)
print("\nAnalysis completed successfully.")