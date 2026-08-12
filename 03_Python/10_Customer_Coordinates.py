import pandas as pd
import pgeocode
df = pd.read_csv("01_Dataset/Customer_Locations.csv")
print("Customer locations loaded successfully.")
print("Total locations:", len(df))
geo = pgeocode.Nominatim("us")
df["Postal Code"] = (df["Postal Code"].astype(str).str.replace(".0", "", regex=False).str.zfill(5))
coordinates = geo.query_postal_code(df["Postal Code"].tolist())
df["Customer Latitude"] = coordinates["latitude"].values
df["Customer Longitude"] = coordinates["longitude"].values
print("\nFirst 10 Customer Coordinates:")
print(df[["State/Province","City","Postal Code","Customer Latitude","Customer Longitude"]].head(10).to_string(index=False))
print("\nMissing Latitude:", df["Customer Latitude"].isna().sum())
print("Missing Longitude:", df["Customer Longitude"].isna().sum())
df.to_csv("01_Dataset/Customer_Locations_Coordinates.csv",index=False)
print("\nCustomer coordinates completed successfully.")
print("Saved: 01_Dataset/Customer_Locations_Coordinates.csv")