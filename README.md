# IDX-High-Dividend-20
IDX High Dividend 20

IDX High Dividend 20 Stock Price Predictor
Overview
This Streamlit application predicts future prices of the IDX High Dividend 20 index (IDXHIDIV20.JK), a stock index on the Indonesia Stock Exchange (IDX) comprising 20 high-dividend-yield stocks. The app fetches historical price data from the Twelve Data API and uses the Prophet time series forecasting model to generate predictions. Users can visualize historical trends, specify a prediction horizon, and view forecasted prices with confidence intervals.
Features

Historical Data Visualization: Displays a line chart of historical IDX High Dividend 20 index prices.
Customizable Predictions: Allows users to input the number of days for forecasting (1 to 365 days).
Model Evaluation: Shows the Mean Absolute Error (MAE) to indicate prediction reliability.
Interactive Interface: Built with Streamlit for an intuitive user experience.

Prerequisites

Python: Version 3.7 or later.
Twelve Data API Key: Required for fetching historical stock data. Sign up for a free key at Twelve Data Pricing.
Internet Connection: Needed to fetch data from the Twelve Data API.

Installation

Clone or Download the Repository:Ensure you have the project files, including idx_high_dividend_predictor.py and requirements.txt.

Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

The requirements.txt file contains:
streamlit
pandas
prophet
requests
scikit-learn



Configuration
The app requires a Twelve Data API key to fetch historical data. Follow these steps:

Obtain an API Key:Sign up at Twelve Data to get a free API key.

Configure the API Key:

Local Development: Replace 'your_api_key_here' in idx_high_dividend_predictor.py with your actual API key. Be cautious not to commit this key to version control (e.g., Git).
Production: Use Streamlit’s secrets management by creating a .streamlit/secrets.toml file with:[secrets]
TWELVE_DATA_API_KEY = "your_actual_api_key"

See Streamlit Secrets Management for details.



Usage

Run the App:After installing dependencies and configuring the API key, start the app:
streamlit run idx_high_dividend_predictor.py


Interact with the App:

The app will open in your default web browser.
View the historical price chart of the IDX High Dividend 20 index.
Enter the number of days for prediction (e.g., 30 days).
Review the forecasted prices, including confidence intervals, and the model’s MAE.



Model Details
The app uses the Prophet library, developed by Facebook, for time series forecasting. Prophet is well-suited for daily stock data, handling trends and seasonality effectively. The model is trained on 80% of the historical data, with the remaining 20% used to evaluate performance via the Mean Absolute Error (MAE).
Limitations

API Limits: The free tier of the Twelve Data API has request limits, which may affect data retrieval frequency.
Prophet Installation: Prophet requires a C++ compiler for its dependencies (pystan or cmdstanpy). If installation issues arise, consider using a conda environment or following Prophet’s installation guide (Prophet Installation).
Prediction Accuracy: Stock prices are influenced by unpredictable factors like economic events and market sentiment. The app’s predictions are probabilistic and cannot achieve 99% accuracy, as requested. The displayed MAE provides insight into the model’s performance.

Disclaimer
Stock price prediction is inherently uncertain due to market volatility and external factors. This app uses the Prophet model to provide forecasts based on historical data, but achieving 99% accuracy is not feasible. Use the predictions as a guide, not a guarantee. Always conduct thorough research before making investment decisions.
Dependencies
The following table lists the Python packages required by the app:



Package
Purpose
PyPI Link



streamlit
Builds the interactive web interface
PyPI: streamlit


pandas
Handles data manipulation and processing
PyPI: pandas


prophet
Performs time series forecasting
PyPI: prophet


requests
Makes API calls to fetch stock data
PyPI: requests


scikit-learn
Calculates model evaluation metrics (MAE)
PyPI: scikit-learn


Troubleshooting

API Key Errors: Ensure the Twelve Data API key is correctly configured. Check the API response for errors if data fetching fails.
Prophet Installation Issues: If prophet fails to install, ensure you have a compatible Python version (3.7+) and a C++ compiler. Alternatively, use conda install prophet.
Streamlit Not Running: Verify that all dependencies are installed and that you’re running the command from the correct directory containing idx_high_dividend_predictor.py.

Contributing
Contributions are welcome! If you have suggestions for improving the app, such as adding new features or enhancing the model, please submit a pull request or open an issue on the project’s repository (if hosted on GitHub).
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, please contact the project maintainer (add contact details if applicable).
