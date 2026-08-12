import pandas as pd
df = pd.read_csv("01_Dataset/Nassau_Candy_Featured.csv")
print("Dataset loaded successfully.")
print("Dataset Shape:", df.shape)
product_factory = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts","Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts","Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's","Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack","Nerds": "Sugar Shack","Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack","Everlasting Gobstopper": "Secret Factory",
    "Lickable Wallpaper": "Secret Factory","Wonka Gum": "Secret Factory",
    "Hair Toffee": "The Other Factory","Kazookles": "The Other Factory"
}
df["Factory"] = df["Product Name"].map(product_factory)
factory_coordinates = {"Lot's O' Nuts": (32.881893, -111.768036),"Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.119140, -96.181150),"Secret Factory": (41.446333, -90.565487),"The Other Factory": (35.117500, -89.971107)
}
df["Factory Latitude"] = df["Factory"].map(lambda x: factory_coordinates.get(x, (None, None))[0])
df["Factory Longitude"] = df["Factory"].map(lambda x: factory_coordinates.get(x, (None, None))[1])
print("\n===== FACTORY MAPPING SUMMARY =====")
print("\nOrders by Factory:")
print(df["Factory"].value_counts())
print("\nProducts Without Factory Mapping:")
print(df.loc[df["Factory"].isna(), "Product Name"].unique())
print("\nMissing Factory Values:")
print(df["Factory"].isna().sum())
print("\nFactory Coordinates:")
print(df[["Factory", "Factory Latitude", "Factory Longitude"]].drop_duplicates().to_string(index=False))
print("\nProduct → Factory Mapping:")
print(df[["Product Name", "Factory"]].drop_duplicates().sort_values("Factory").to_string(index=False))
output_file = "01_Dataset/Nassau_Candy_Factory_Mapped.csv"
df.to_csv(output_file, index=False)
print("\nFactory mapping completed successfully.")
print("Saved File:", output_file)
print("Final Dataset Shape:", df.shape)