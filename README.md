# Nassau Candy Factory Reallocation & Shipping Optimization

## 📌 Project Overview

The **Nassau Candy Factory Reallocation & Shipping Optimization Recommendation System** is a data-driven project designed to help identify better factory assignments for customer orders.

The main idea is simple: when an order is currently being supplied from a factory that is far away from the customer, the system checks whether another factory could serve that customer with a shorter shipping distance.

The project analyzes customer locations, factory locations, shipping distances, sales, units, gross profit, regions, products, and shipping modes to identify factory reallocation opportunities.

The final system provides optimization recommendations through data analysis, machine learning techniques, scenario simulation, Power BI, and an interactive Streamlit dashboard.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze current factory-to-customer shipping distances.
- Identify suitable alternative factories for customer orders.
- Calculate the potential distance that can be saved.
- Measure the improvement percentage after factory reallocation.
- Recommend better factory assignments.
- Analyze sales and profit across regions and factories.
- Analyze shipping modes and product performance.
- Support logistics and supply-chain decision making.
- Provide an interactive dashboard for exploring recommendations.

---

## 🛠️ Technologies Used

The project was developed using the following technologies:

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **SQL**
- **Streamlit**
- **Power BI**
- **Machine Learning**
- **Data Visualization**
- **Geographic Distance Analysis**

---

## 📂 Project Structure

```text
Nassau-Candy-Factory-Optimization/
│
├── 01_Dataset/
│   └── Project datasets and processed CSV files
│
├── 02_SQL/
│   └── SQL analysis queries
│
├── 03_Python/
│   └── Data analysis, feature engineering,
│       distance analysis and optimization scripts
│
├── 04_PowerBI/
│   └── Power BI dashboard
│
├── 05_Models/
│   └── Model comparison and model-related files
│
├── 06_Reports/
│   └── Project reports
│
├── 07_Dashboard/
│   └── Streamlit interactive dashboard
│
├── 08_Documentation/
│   └── Technical documentation
│
└── README.md
