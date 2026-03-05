import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analytics import *
from src.prediction import revenue_prediction


st.title("Smart Merchant Payment Analyzer")

df = load_data("data/Online Retail.xlsx")

df = clean_data(df)

st.metric("Total Revenue", round(total_revenue(df),2))

st.subheader("Daily Revenue")

daily = daily_sales(df)

st.line_chart(daily)

st.subheader("Revenue by Hour")

hourly = hourly_sales(df)

st.bar_chart(hourly)

st.subheader("Top Selling Products")

st.write(top_products(df))

st.subheader("Top Revenue Products")

st.write(top_revenue_products(df))

st.subheader("Sales by Country")

st.bar_chart(country_sales(df).head(10))

st.subheader("Next Day Revenue Prediction")

prediction = revenue_prediction(daily)

st.success(f"Predicted next day revenue: {round(prediction,2)}")