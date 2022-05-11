import yfinance as yf
import pandas as pd
import time

dow = pd.read_csv("data/dow_30.csv")

print(dow[["Company","Symbol"]])

for ticker in dow.Symbol:
    data = yf.download(ticker, start="2017-05-10")
    data.to_csv(f"{ticker}.csv", index=True, header=True)
    time.sleep(5)