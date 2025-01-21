import binomial_model
import black_scholes_model
import monte_carlo_simulation

import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

def valid_ticker(symbol: str) -> bool:
    try:
        ticker = yf.Ticker(symbol)
        ticker.info
        return True
    except:
        return False

def main():
    stock = input("Hello, which stock would you like to check today?\n")
    while(valid_ticker(stock) == False):
        stock = input("Invalid stock; try again.\n")
    ticker = yf.Ticker(stock)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=252)
    hist = ticker.history(start=start_date, end=end_date)
    s = hist['Close'].iloc[-1]
    k = s
    t = 30 / 252
    r = .0436
    sigma = hist['Close'].pct_change().std() * np.sqrt(252)
    n = 1000
    option = input("Choose the model you want to use to find the options price:"
                   "\nType bn for binomial model"
                   "\nType bs for black-scholes model"
                   "\nType mc for monte-carlo simulation\n")
    while (option != "bn" and option != "bs" and option != "mc"):
        option = input("Invalid model choice; try again.\n")
    option_type = input("Call or Put Option?"
                   "\nType C for call option"
                   "\nType P for put option\n")
    while (option_type != 'C' and option_type != 'P'):
        option_type = input("Invalid option type; try again.")
    if (option == "bn"):
        print(binomial_model.binomial(s, k, t, r, sigma, n, option_type))
    elif (option == "bs"):
        print(black_scholes_model.black_scholes(s, k, t, r, sigma, option_type))
    elif (option == "mc"):
        print(monte_carlo_simulation.monte_carlo(s, k, t, r, sigma, n, option_type))

if __name__ == "__main__":
    main()