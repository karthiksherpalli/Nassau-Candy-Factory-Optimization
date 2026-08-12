import pandas as pd
import numpy as np
df = pd.read_csv(
    "01_Dataset/Customer_Locations_Coordinates.csv"
)
print("Customer coordinate dataset loaded successfully.")
print("Total customer locations:", len(df))
factories = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.119140, -96.181150),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.117500, -89.971107)
}
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate straight-line distance between
    two latitude/longitude points in kilometers.
    """
    earth_radius = 6371.0
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )
    c = 2 * np.arctan2(
        np.sqrt(a),
        np.sqrt(1 - a)
    )
    return earth_radius * c
for factory, coordinates in factories.items():
    factory_lat = coordinates[0]
    factory_lon = coordinates[1]
    column_name = f"Distance to {factory} (KM)"
    df[column_name] = haversine(
        factory_lat,
        factory_lon,
        df["Customer Latitude"],
        df["Customer Longitude"]
    )
distance_columns = [
    f"Distance to {factory} (KM)"
    for factory in factories
]
df["Nearest Factory"] = (
    df[distance_columns]
    .idxmin(axis=1)
    .str.replace("Distance to ", "", regex=False)
    .str.replace(" (KM)", "", regex=False)
)
df["Nearest Factory Distance KM"] = (
    df[distance_columns].min(axis=1)
)
df[distance_columns] = df[distance_columns].round(2)
df["Nearest Factory Distance KM"] = (
    df["Nearest Factory Distance KM"].round(2)
)
print("\n===== DISTANCE CALCULATION SAMPLE =====")
print(
    df[
        [
            "Country/Region",
            "City",
            "State/Province",
            "Region",
            "Nearest Factory",
            "Nearest Factory Distance KM"
        ]
    ]
    .head(20)
    .to_string(index=False)
)
print("\n===== NEAREST FACTORY COUNTS =====")
print(
    df["Nearest Factory"]
    .value_counts()
)
print("\nMissing Distance Values:")
print(
    df[distance_columns]
    .isna()
    .sum()
)
print(
    "\nMinimum Distance:",
    round(df["Nearest Factory Distance KM"].min(), 2)
)
print(
    "Average Nearest Distance:",
    round(df["Nearest Factory Distance KM"].mean(), 2)
)
print(
    "Maximum Nearest Distance:",
    round(df["Nearest Factory Distance KM"].max(), 2)
)
df.to_csv(
    "01_Dataset/Customer_Factory_Distances.csv",
    index=False
)
print("\nDistance calculation completed successfully.")
print(
    "Saved: 01_Dataset/Customer_Factory_Distances.csv"
)