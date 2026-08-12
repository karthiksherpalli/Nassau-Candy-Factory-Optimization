import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("01_Dataset/Nassau_Candy_Factory_Mapped.csv")
data = df.groupby(["Product Name", "Region"]).agg(Sales=("Sales", "sum"),Profit=("Gross Profit", "sum"),Units=("Units", "sum")).reset_index()
X = StandardScaler().fit_transform(data[["Sales", "Profit", "Units"]])
data["Cluster"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)
print("===== ROUTE & PRODUCT CLUSTERING =====")
print(data.head(15))
print("\nCluster Counts:")
print(data["Cluster"].value_counts().sort_index())
data.to_csv("01_Dataset/Route_Product_Clusters.csv", index=False)
print("\nClustering completed successfully.")