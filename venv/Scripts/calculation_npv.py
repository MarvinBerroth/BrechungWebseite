import numpy_financial as np
from .yfinance_api import *

stock_price_euro(year)
shares_mio(year)
currencys
year_newest_report
year_oldest_report
equity_mio(year)
divident(year)


def potential(stock_valuation_euro , stock_price_euro):
    return round(((stock_valuation_euro / stock_price_euro)-1),2)

def stock_valuation_euro():
    return round(((company_valuation_mio_euro / shares_mio)),2)

def company_valuation_mio_euro():
    return round((company_valuation_mio * currency),0)

def company_valuation_mio():
    return round((growth_year_average * 0.04),0)

def growth_year_average():
    return round((growth_total/((year_latest_report - 1) - year_oldest_report)),0)

def growth_total():
    groth = 0
    year = 0
    n = reports_amount()
    while n < 0:
        groth = (groth (equity_mio(year + 1) - equity_mio(year)) + divident(year + 1) - equity_difference(year + 1))
        year + 1
        n + 1

    return round(groth)

def equity_difference(year):
    equity_dif = 0
    n = reports_amount()
    while n < 0:
        equity_dif = (equity_dif (equity_mio(year) - equity_mio(year+1)) + divident(year) - equity_difference(year))
        year + 1
        n + 1

    return round(equity_dif)



