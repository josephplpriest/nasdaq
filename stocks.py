import pandas as pd

dow_30 = pd.read_csv("data/dow_30.csv")

apple = pd.read_csv("data/AAPL.csv")

apple["pct_increase"] = (apple.Close - apple.Open) / apple.Open * 100

print(apple.sort_values("pct_increase", ascending=False).head(10))