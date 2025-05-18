# This script trains a Random Forest model to predict crop prices based on location and month.
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Load dataset
df = pd.read_csv("sample_data.csv")

# Rename avg_price to price if needed
if "avg_price" in df.columns:
    df.rename(columns={"avg_price": "price"}, inplace=True)

# Drop rows with missing values in key columns
df.dropna(subset=["crop", "location", "month", "price"], inplace=True)

X = df[["crop", "location", "month"]]
y = df["price"]

categorical_features = ["crop", "location"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
], remainder='passthrough')  # month passed through as is

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X, y)
joblib.dump(pipeline, "model.pkl")
