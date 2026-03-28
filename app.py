import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/sales_model.pkl")

st.title("📈 Sales Forecasting App")

st.write("Enter details to predict next month sales")

# Inputs
year = st.number_input("Year", 2000, 2030, 2020)
month = st.number_input("Month", 1, 12, 1)
lag_1 = st.number_input("Last Month Sales", 0.0, 100000.0, 5000.0)
lag_12 = st.number_input("Sales 12 Months Ago", 0.0, 100000.0, 5000.0)

# Create dataframe
input_data = pd.DataFrame({
    "year": [year],
    "month": [month],
    "lag_1": [lag_1],
    "lag_12": [lag_12]
})

# Predict
if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales: {prediction[0]:.2f}")