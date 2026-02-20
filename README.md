# 🚖 Uber Demand Forecasting & Analysis

## 📌 Overview

This project simulates Uber ride demand data and performs time-series forecasting and demand analysis using multiple techniques. The workflow includes synthetic dataset generation, ARIMA-based forecasting, deep learning forecasting with LSTM, big data aggregation using Apache Spark, and interactive visualization using Plotly.

The dataset used in this project is synthetically generated for demonstration and learning purposes.

---

## 🧪 Dataset Description

The dataset is programmatically generated with the following attributes:

- 365 days of data starting from May 1, 2024
- 6 cities: Hyderabad, Bangalore, Mumbai, Ahmedabad, Chennai, Kolkata
- Random daily demand values between 1000 and 10000
- Weather condition (Sunny, Windy, Rainy, Cloudy)
- Day of week

The dataset is saved as:
uber_demand_data.csv 

---

## 📊 Time Series Analysis

For a selected city (Ahmedabad), the following analysis is performed:

- Time series visualization of daily ride demand
- Seasonal decomposition using additive model (weekly seasonality)
- ARIMA-based forecasting for 30 future days

---

## 📈 ARIMA Model

The ARIMA model is configured with:

- Order: (5, 1, 0)
- Forecast horizon: 30 days

Evaluation metrics used:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The trained ARIMA model is saved as:
uber_demand_arima_model.pkl 

---

## 🤖 LSTM Deep Learning Model

A deep learning forecasting model is implemented using:

- Two LSTM layers (50 units each)
- Dropout regularization (0.2)
- Sequence length of 30 days
- Mean Squared Error (MSE) loss function

The LSTM model forecasts the next 7 days of demand based on previous demand patterns.

---

## ⚡ Apache Spark Analysis

Using PySpark:

- The dataset is loaded into a Spark DataFrame
- Average demand per city is calculated
- Demonstrates scalable big data processing capability

---

## 📊 Interactive Visualization

Using Plotly:

- Interactive city-level demand trend visualization
- Dynamic line chart for selected city demand analysis

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels (ARIMA)
- TensorFlow / Keras (LSTM)
- Scikit-learn
- PySpark
- Plotly
- Joblib

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt 
2. Run the script:
python your_script_name.py

---

## 📌 Project Highlights

- End-to-end synthetic data generation
- Classical time-series forecasting using ARIMA
- Deep learning forecasting using LSTM
- Big data aggregation using Apache Spark
- Interactive visualization using Plotly
- Model persistence using Joblib

This project demonstrates both traditional statistical modeling and modern deep learning approaches for demand forecasting, along with scalable data processing techniques.
