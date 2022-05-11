"""Short script to scrape a list of Dow Jones 30 companies, descriptions and ticker symbols."""

#Use pandas to read html tables from wikipedia
import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average")

#lots of tables on the page, we'll grab the second
dow_30 = tables[1].copy()

#make sure we have all 30 rows/companies of the table
assert(dow_30.shape[0] == 30)

#drop column with mostly NULL values
dow_30.drop(columns="Notes", inplace=True)


dow_30.to_csv("data/dow_30.csv", index=False, header=True)