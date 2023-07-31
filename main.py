# Stocks: 
# HINDUNILVR - 20 shares
# RELIANCE - 10 shares
# SBICARD - 50 shares

# ---------------------------------------------------
import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# Define portfolio
stocks = [
    {
        "Ticker": "HINDUNILVR",
        "Exchange": "NSE",
        "Quantity": "20",
        "Price": None,
        "Market Value": None,
        "% Allocation": None
    },
    {
        "Ticker": "RELIANCE",
        "Exchange": "NSE",
        "Quantity": "10",
        "Price": None,
        "Market Value": None,
        "% Allocation": None
    },
    {
        "Ticker": "SBICARD",
        "Exchange": "NSE",
        "Quantity": "50",
        "Price": None,
        "Market Value": None,
        "% Allocation": None
    }
]

# Convert to pandas dataframe
stocks_df = pd.DataFrame(stocks)


# Scrape the prices
# ------------------------------

# Helper function to clean data
def clean_price(price):
    cleaned_price = re.sub("₹|,", "", price)
    return float(cleaned_price)

# Hindustan Unilever
resp = r.get("https://www.google.com/finance/quote/HINDUNILVR:NSE")
soup = bs(resp.content, "html.parser")
price_1 = soup.find("div", attrs={"class": "YMlKec fxKbKc"}).text
cleaned_price1 = clean_price(price_1)
stocks_df.loc[stocks_df["Ticker"] == "HINDUNILVR", "Price"] = cleaned_price1
quantity = float(stocks_df.loc[stocks_df["Ticker"] == "HINDUNILVR", "Quantity"].iloc[0])
stocks_df.loc[stocks_df["Ticker"] == "HINDUNILVR", "Market Value"]= cleaned_price1 * quantity

# Reliance 
resp = r.get("https://www.google.com/finance/quote/RELIANCE:NSE")
soup = bs(resp.content, "html.parser")
price_2 = soup.find("div", attrs={"class": "YMlKec fxKbKc"}).text
cleaned_price2 = clean_price(price_2)
stocks_df.loc[stocks_df["Ticker"] == "RELIANCE", "Price"]= cleaned_price2
quantity = float(stocks_df.loc[stocks_df["Ticker"] == "RELIANCE", "Quantity"].iloc[0])
stocks_df.loc[stocks_df["Ticker"] == "RELIANCE", "Market Value"]= cleaned_price2 * quantity


# SBI Card
resp = r.get("https://www.google.com/finance/quote/SBICARD:NSE")
soup = bs(resp.content, "html.parser")
price_3 = soup.find("div", attrs={"class": "YMlKec fxKbKc"}).text
cleaned_price3 = clean_price(price_3)
stocks_df.loc[stocks_df["Ticker"] == "SBICARD", "Price"]= cleaned_price3
quantity = float(stocks_df.loc[stocks_df["Ticker"] == "SBICARD", "Quantity"].iloc[0])
stocks_df.loc[stocks_df["Ticker"] == "SBICARD", "Market Value"]= cleaned_price3 * quantity


# Formula for %allocation : marketvalue(current) / total(market value) * 100
total_market_value = stocks_df["Market Value"].sum()
stocks_df.loc[stocks_df["Ticker"] == "HINDUNILVR", "% Allocation"] = (stocks_df.loc[stocks_df["Ticker"] == "HINDUNILVR", "Market Value"] / total_market_value ) * 100
stocks_df.loc[stocks_df["Ticker"] == "RELIANCE", "% Allocation"] = (stocks_df.loc[stocks_df["Ticker"] == "RELIANCE", "Market Value"] / total_market_value ) * 100
stocks_df.loc[stocks_df["Ticker"] == "SBICARD", "% Allocation"] = (stocks_df.loc[stocks_df["Ticker"] == "SBICARD", "Market Value"] / total_market_value ) * 100
print(stocks_df)