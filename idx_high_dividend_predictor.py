import streamlit as st
import pandas as pd
from prophet import Prophet
import requests
from sklearn.metrics import mean_absolute_error

# Function to fetch data from Twelve Data API
def fetch_data(symbol, api_key):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if 'values' not in data:
        st.error("Failed to fetch data. Please check the API key or symbol.")
        return None
    df = pd.DataFrame(data['values']).rename(columns={'datetime': 'ds', 'close': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df['y'] = df['y'].astype(float)
    return df

# Streamlit app
st.title("IDX High Dividend 20 Stock Price Predictor")

# API key (store securely in production)
api_key = st.secrets.get("TWELVE_DATA_API_KEY", "your_api_key_here")  # Replace with actual key
symbol = "IDXHIDIV20.JK"

# Fetch data
data = fetch_data(symbol, api_key)
if data is None:
    st.stop()

# Split data for training and testing
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Train Prophet model
model = Prophet()
model.fit(train_data)

# User input for prediction horizon
days_to_predict = st.number_input("Number of days to predict", min_value=1, max_value=365, value=30)

# Make future predictions
future = model.make_future_dataframe(periods=days_to_predict)
forecast = model.predict(future)

# Evaluate model
if not test_data.empty:
    test_forecast = forecast[forecast['ds'].isin(test_data['ds'])]
    mae = mean_absolute_error(test_data['y'], test_forecast['yhat'])
    st.write(f"Model Mean Absolute Error (MAE): {mae:.2f}")

# Display historical data
st.subheader("Historical Data")
st.line_chart(data.set_index('ds')['y'])

# Display forecast
st.subheader("Forecast")
st.line_chart(forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']])

# Show predicted price for the last day
last_pred = forecast.iloc[-1]['yhat']
last_date = forecast.iloc[-1]['ds'].date()
st.write(f"Predicted price for {last_date}: {last_pred:.2f} IDR")

# Disclaimer
st.write("**Disclaimer**: Stock price prediction is probabilistic and cannot achieve 99% accuracy due to market volatility. This app uses the Prophet model to provide forecasts based on historical data. Actual performance may vary.")
