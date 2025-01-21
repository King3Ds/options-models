import binomial_model
import black_scholes_model

import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

def main():
    ticker = yf.Ticker("TSLA")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=252)
    hist = ticker.history(start=start_date, end=end_date)
    s = hist['Close'].iloc[-1]
    k = s
    t = 30 / 252
    r = .0436
    sigma = hist['Close'].pct_change().std() * np.sqrt(252)
    print(black_scholes_model.black_scholes(s, k, t, r, sigma))

if __name__ == "__main__":
    main()