import pandas as pd
df = pd.read_csv("01_Dataset/Customer_Factory_Distances.csv")
distance_cols = [c for c in df.columns if c.startswith("Distance to")]
result = df.groupby("Region")[distance_cols].mean().round(2)
print("===== FACTORY SCENARIO SIMULATION =====")
print(result)
result["Recommended Factory"] = result.idxmin(axis=1)
result["Recommended Factory"] = (
result["Recommended Factory"]
.str.replace("Distance to ", "", regex=False).str.replace(" (KM)", "", regex=False))
print("\n===== RECOMMENDED FACTORY BY REGION =====")
print(result["Recommended Factory"])
result.to_csv("01_Dataset/Scenario_Results.csv")
print("\nScenario simulation completed successfully.")