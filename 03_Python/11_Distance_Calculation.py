import pandas as pd
import pgeocode
df = pd.read_csv("01_Dataset/Nassau Candy Distributor.csv",dtype={"Postal Code": str})
locations = df[["Country/Region","State/Province","City","Postal Code","Region"]].drop_duplicates().copy()
locations["Postal Code"] = (locations["Postal Code"].astype(str).str.strip().str.upper())
locations["Customer Latitude"] = pd.NA
locations["Customer Longitude"] = pd.NA
us_geo = pgeocode.Nominatim("us")
ca_geo = pgeocode.Nominatim("ca")
us_mask = locations["Country/Region"] == "United States"
us_postal = (locations.loc[us_mask, "Postal Code"]
.str.replace(".0", "", regex=False).str.zfill(5))
us_coordinates = us_geo.query_postal_code(us_postal.tolist())
locations.loc[us_mask, "Customer Latitude"] = (us_coordinates["latitude"].values)
locations.loc[us_mask, "Customer Longitude"] = (us_coordinates["longitude"].values)
ca_mask = locations["Country/Region"] == "Canada"
ca_postal = locations.loc[ca_mask, "Postal Code"]
ca_coordinates = ca_geo.query_postal_code(ca_postal.tolist())
locations.loc[ca_mask, "Customer Latitude"] = (ca_coordinates["latitude"].values)
locations.loc[ca_mask, "Customer Longitude"] = (ca_coordinates["longitude"].values)
locations["Customer Latitude"] = pd.to_numeric(locations["Customer Latitude"],errors="coerce")
locations["Customer Longitude"] = pd.to_numeric(locations["Customer Longitude"],errors="coerce")
print("===== CUSTOMER COORDINATE SUMMARY =====")
print("Total locations:", len(locations))
print("Missing Latitude:",locations["Customer Latitude"].isna().sum())
print("Missing Longitude:",
locations["Customer Longitude"].isna().sum())
print("\nCountry Counts:")
print(locations["Country/Region"].value_counts())
print("\nCanada Sample:")
print(locations[locations["Country/Region"] == "Canada"][["City","State/Province","Postal Code",
"Customer Latitude","Customer Longitude"]].head(10).to_string(index=False))
locations.to_csv("01_Dataset/Customer_Locations_Coordinates.csv",index=False)
print("\nCustomer coordinate processing completed.")
print("Saved: 01_Dataset/Customer_Locations_Coordinates.csv")