import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("01_Dataset/Nassau_Candy_Factory_Mapped.csv")
print("Dataset loaded successfully.")
print("Dataset Shape:", df.shape)
factory_region = df.groupby(["Factory", "Region"]).agg(
Total_Sales=("Sales", "sum"),Total_Profit=("Gross Profit", "sum"),Total_Units=("Units", "sum"),
Total_Orders=("Order ID", "nunique")).reset_index()
factory_region["Profit_Margin_%"] = (factory_region["Total_Profit"]/ factory_region["Total_Sales"]) * 100
print("\n===== FACTORY × REGION ANALYSIS =====")
print(factory_region.sort_values("Total_Sales", ascending=False).round(2).to_string(index=False))
sales_matrix = factory_region.pivot(index="Factory",columns="Region",values="Total_Sales").fillna(0)
print("\n===== FACTORY × REGION SALES MATRIX =====")
print(sales_matrix.round(2))
sales_matrix.plot(kind="bar",figsize=(12, 6))
plt.title("Sales by Factory and Region")
plt.xlabel("Factory")
plt.ylabel("Total Sales")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Region")
plt.tight_layout()
plt.show()
best_region = factory_region.loc[factory_region.groupby("Factory")["Total_Sales"].idxmax(),["Factory", "Region", "Total_Sales", "Total_Profit"]]
print("\n===== TOP REGION FOR EACH FACTORY =====")
print(best_region.round(2).to_string(index=False))