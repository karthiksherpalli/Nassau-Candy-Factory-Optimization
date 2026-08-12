import pandas as pd
df = pd.read_csv("01_Dataset/Distance_Improvement.csv")
df["Lead Time"] = (
pd.to_datetime(df["Ship Date"]) -
pd.to_datetime(df["Order Date"])).dt.days
model_data = df[["Product Name", "Factory", "Region", "Ship Mode","Current Distance KM", "Sales", "Gross Profit", "Lead Time"]].copy()
model_data = pd.get_dummies(model_data,columns=["Product Name", "Factory", "Region", "Ship Mode"])
print("Model Dataset Shape:", model_data.shape)
print("Missing Values:", model_data.isnull().sum().sum())
print("Average Lead Time:", round(model_data["Lead Time"].mean(), 2), "Days")
model_data.to_csv("01_Dataset/Model_Data.csv", index=False)
print("\nModel preparation completed successfully.")
print("\n===== LEAD TIME CHECK =====")
print(df[["Order Date", "Ship Date", "Lead Time"]].head(10))
print("\nMinimum Lead Time:", model_data["Lead Time"].min())
print("Maximum Lead Time:", model_data["Lead Time"].max())