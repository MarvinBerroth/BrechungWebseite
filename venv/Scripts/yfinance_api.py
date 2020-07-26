import yfinance as yf
from yahooquery import Ticker


# return marketcap of a company

def get_marketcap(symbol):
    return round(float(Ticker(symbol).price[symbol]['marketCap']) / 1000000, 2)

# example
# print(get_marketcap("ADMS"))
# print(yf.Ticker('ADMS').info)


def get_EV(symbol):
    if get_marketcap(symbol) != None and get_debt(symbol) != None and get_cash(symbol) != None:
        return round(get_marketcap(symbol)+get_debt(symbol)-get_cash(symbol),2)
    else:
        return round(float(Ticker(symbol).key_stats[symbol]['enterpriseValue']) / 1000000, 2)

# print(yf.Ticker('ADMS').financials)


# get reported amount of cash of the company
def get_cash(ticker):
    try:
        return round(float(Ticker(ticker).balance_sheet('q')['CashCashEquivalentsAndShortTermInvestments'].iloc[-1] )/ 1000000, 2)
    except:
        return None

def get_debt(ticker):
    try:
        return round(float(Ticker(ticker).balance_sheet('q')['TotalDebt'].iloc[-1])/ 1000000, 2)
    except:
        return None

def get_balance(ticker):
    try:
        return Ticker(ticker).balance_sheet('q')
    except:
        return None

# get historical market data, last 6 months and 1 week interval
# return a data frame containing highest stock price


def return_date_stock(symbol):
    return yf.Ticker(symbol).history(period="6mo", interval="1wk")['High'].index.tolist()


def return_price_stock(symbol):
    return yf.Ticker(symbol).history(period="6mo", interval="1wk")['High'].tolist()


def get_hist(symbol):
    yf.Ticker(symbol).history(period="6mo", interval="1wk")


#Example code

#print(yf.Ticker('PSM.DE').history(period="6mo", interval="1wk")['High'])
#print(Ticker('PSM.DE').key_stats)

print(Ticker('AAPL').balance_sheet())

print(yf.Ticker('AAPL').quote_type('EQUITY'))


#print(get_balance('PSM.DE').iloc[0])

#print(yf.Ticker('PSM.DE').history(period="6mo", interval="1wk")['High'].index.tolist())
#print(yf.Ticker(symbol).key_stats[symbol]['enterpriseValue'])
