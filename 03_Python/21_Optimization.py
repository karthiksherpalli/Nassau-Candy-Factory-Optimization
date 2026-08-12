import pandas as pd
df = pd.read_csv("01_Dataset/Distance_Improvement.csv")
df["Recommended Factory"] = df["Nearest Factory"]
recommend = df[(df["Factory"] != df["Recommended Factory"]) &(df["Distance Saved KM"] > 0)].copy()
recommend = recommend.sort_values("Distance Improvement %",ascending=False)
print("===== TOP FACTORY RECOMMENDATIONS =====")
print(recommend[["Product Name", "Factory", "Recommended Factory",
"Distance Saved KM", "Distance Improvement %","Gross Profit"]].head(10).round(2))
recommend.to_csv("01_Dataset/Final_Recommendations.csv",index=False)
print("\nOptimization completed successfully.")
coverage = len(recommend) / len(df) * 100
avg_improvement = recommend["Distance Improvement %"].mean()
recommend["Confidence Score"] = (recommend["Distance Improvement %"].clip(0, 100))
print("\n===== OPTIMIZATION KPIs =====")
print("Lead/Distance Reduction %:", round(avg_improvement, 2))
print("Recommendation Coverage %:", round(coverage, 2))
print("Scenario Confidence Score:", round(recommend["Confidence Score"].mean(), 2))
print("Profit Impact Stability:", "Stable" if recommend["Gross Profit"].mean() > 0 else "Risk")