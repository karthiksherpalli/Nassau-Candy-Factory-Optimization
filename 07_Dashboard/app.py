import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Nassau Candy Optimization",
    page_icon="🍬",
    layout="wide"
)

# Load Data
df = pd.read_csv("01_Dataset/Final_Recommendations.csv")

st.title("🍬 Nassau Candy Factory Optimization")
st.write("Factory Reallocation & Shipping Optimization Recommendation System")

# Filters
c1, c2, c3 = st.columns(3)

with c1:
    product = st.selectbox(
        "Product",
        ["All"] + sorted(df["Product Name"].unique())
    )

with c2:
    region = st.selectbox(
        "Region",
        ["All"] + sorted(df["Region"].unique())
    )

with c3:
    ship = st.selectbox(
        "Ship Mode",
        ["All"] + sorted(df["Ship Mode"].unique())
    )

data = df.copy()

if product != "All":
    data = data[data["Product Name"] == product]

if region != "All":
    data = data[data["Region"] == region]

if ship != "All":
    data = data[data["Ship Mode"] == ship]

# Priority
priority = st.slider(
    "Speed vs Profit Priority",
    0, 100, 50
)

# Normalize + Score
distance = data["Distance Improvement %"] / 100

profit = (
    (data["Gross Profit"] - data["Gross Profit"].min()) /
    (data["Gross Profit"].max() - data["Gross Profit"].min())
)

data["Recommendation Score"] = (
    distance * (priority / 100) +
    profit.fillna(0) * ((100 - priority) / 100)
) * 100

data = data.sort_values(
    "Recommendation Score",
    ascending=False
).reset_index(drop=True)

data.insert(0, "S.NO", range(1, len(data) + 1))

# KPIs
st.subheader("Optimization KPIs")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Recommendations", len(data))

k2.metric(
    "Avg Distance Saved",
    f"{data['Distance Saved KM'].mean():.0f} KM"
)

k3.metric(
    "Avg Improvement",
    f"{data['Distance Improvement %'].mean():.1f}%"
)

k4.metric(
    "Avg Gross Profit",
    f"${data['Gross Profit'].mean():.2f}"
)

# What-if
st.subheader("What-if Analysis")

w1, w2, w3 = st.columns(3)

w1.metric(
    "Current Avg Distance",
    f"{data['Current Distance KM'].mean():.0f} KM"
)

w2.metric(
    "Optimized Avg Distance",
    f"{data['Nearest Factory Distance KM'].mean():.0f} KM"
)

w3.metric(
    "Distance Reduction",
    f"{data['Distance Saved KM'].mean():.0f} KM"
)

# Recommendations
st.subheader("📊 Factory-wise Distance Saved")

factory_chart = (
    data.groupby("Recommended Factory")["Distance Saved KM"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(factory_chart)
st.subheader("🌍 Region-wise Sales")

region_chart = (
    data.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(region_chart)
st.subheader("🚚 Ship Mode Distribution")

ship_chart = data["Ship Mode"].value_counts()

st.bar_chart(ship_chart)
st.download_button(
    label="📥 Download Recommendations CSV",
    data=data.to_csv(index=False),
    file_name="Final_Recommendations.csv",
    mime="text/csv"
)
st.subheader("🔍 Search Product")

search = st.text_input(
    "Enter Product Name",
    ""
)

if search:
    data = data[
        data["Product Name"]
        .str.contains(search, case=False, na=False)
    ]
    st.subheader("🏆 Top 10 Recommended Products")

top_products = (
    data.groupby("Product Name")["Recommendation Score"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)
st.subheader("Factory Reallocation Recommendations")

cols = [
    "S.NO",
    "Product Name",
    "Region",
    "Ship Mode",
    "Factory",
    "Recommended Factory",
    "Current Distance KM",
    "Nearest Factory Distance KM",
    "Distance Saved KM",
    "Distance Improvement %",
    "Gross Profit",
    "Recommendation Score"
]

st.dataframe(
    data[cols],
    use_container_width=True,
    hide_index=True
)
st.markdown("---")

st.markdown(
    """
### 📌 Project Summary

**Project:** Factory Reallocation & Shipping Optimization Recommendation System

**Organization:** Nassau Candy Distributor

**Technology Stack**
- Python
- Pandas
- Streamlit
- Machine Learning
- SQL
- Power BI

**Models Used**
- Random Forest
- Gradient Boosting
- Clustering
- Scenario Simulation
"""
)
from datetime import datetime

st.caption(
    f"Last Updated : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
st.success("✅ Dashboard Loaded Successfully")