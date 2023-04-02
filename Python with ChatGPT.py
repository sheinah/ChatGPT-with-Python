import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def create_features(stock_data):
    stock_data['Date'] = stock_data.index
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data['Year'] = stock_data['Date'].dt.year
    stock_data['Month'] = stock_data['Date'].dt.month
    stock_data['Day'] = stock_data['Date'].dt.day
    return stock_data

def predict_stock_price(ticker, start_date, end_date, future_date):
    stock_data = get_stock_data(ticker, start_date, end_date)
    stock_data = create_features(stock_data)

    X = stock_data[['Year', 'Month', 'Day']]
    y = stock_data['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print("Model accuracy: {:.2f}".format(score))

    future_date = pd.to_datetime(future_date)
    future_data = {'Year': [future_date.year], 'Month': [future_date.month], 'Day': [future_date.day]}
    future_df = pd.DataFrame(future_data)

    predicted_price = model.predict(future_df)
    return predicted_price[0]

ticker = 'AAPL'
start_date = '2018-01-01'
end_date = '2022-12-31'
future_date = '2023-04-30'

predicted_price = predict_stock_price(ticker, start_date, end_date, future_date)
print(f"Predicted price for {ticker} on {future_date}: ${predicted_price:.2f}")