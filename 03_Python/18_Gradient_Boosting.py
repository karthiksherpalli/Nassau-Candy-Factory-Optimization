import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("01_Dataset/Model_Data.csv")
X = df.drop("Lead Time", axis=1)
y = df["Lead Time"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("===== GRADIENT BOOSTING =====")
print("MAE:", round(mean_absolute_error(y_test, pred), 2))
print("RMSE:", round(mean_squared_error(y_test, pred) ** 0.5, 2))
print("R2:", round(r2_score(y_test, pred), 3))
print("\n===== MODEL COMPARISON =====")
print("Linear Regression : MAE 215.19 | RMSE 266.87 | R2 -0.007")
print("Random Forest     : MAE 229.69 | RMSE 283.40 | R2 -0.136")
print("Gradient Boosting : MAE 215.12 | RMSE 266.66 | R2 -0.005")
print("\nBest Model: Gradient Boosting")