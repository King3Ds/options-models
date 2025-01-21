import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Coss, Ross & Rubinstein Method - recombining tree and same size
def binomial_model(s: float, k: float, t: float, r: float, sigma: float, n: int, option_type: str = 'C') -> float:
    """
    :param s: initial stock price
    :param k: strike price
    :param t: time to expiration
    :param r: risk-free rate
    :param sigma: volatility of underlying asset
    :param n: time interval
    :param option_type: type of the option w/ call option as default
    :return: fair value of the premium for the options contract
    """

    # variables
    dt = t/n # dt: delta-time / step-size in time
    u = np.exp(sigma*np.sqrt(dt)) # u: up-factor
    d = 1/u # down-factor
    q = (np.exp(r*dt) - d) / (u - d) # q: risk-neutral probability (probability of an up move)

    # initialize asset prices at maturity
    asset_prices = np.array([s * u**j * d**(n-j) for j in range(n+1)])

    # initialize option values at maturity
    option_values = 0
    if (option_type == 'C'):
        option_values = np.maximum(asset_prices - k, 0)
    elif (option_type == 'P'):
        option_values = np.maximum(k - asset_prices, 0)

    # backward induction
    for i in range(n-1, -1, -1):
        asset_prices = asset_prices[:-1] / u # slices the latest asset price value from the array
        held_value = (np.exp(-r*dt) * (q * option_values[1:]) + ((1-q) * option_values[:-1]))
        intrinsic_value = 0
        if (option_type == 'C'):
            intrinsic_value = np.maximum(asset_prices - k, 0)
        elif (option_type == 'P'):
            intrinsic_value = np.maximum(k - asset_prices, 0)
        option_values = np.maximum(intrinsic_value, held_value)
    return option_values[0]

def helper_function(s, k, r, q, dt, u, i, option_values, option_type='C') -> float:
    """
    :param s: initial stock price
    :param k: strike price
    :param r: risk-free rate
    :param q: risk-neutral probability
    :param dt: change in time
    :param u: up-factor
    :param i: ith iteration
    :param option_values: option-values array @ ith iteration
    :param option_type: type of option
    :return: fair premium value
    """
    if (i == 0):
        return option_values[0]
    else:
        asset_prices = s * u**np.arange(i, -1, -1) * (1/u)**np.arange(i+1)
        held_value = np.exp(-r*dt) * (q * option_values[1:] + (1-q) * option_values[:-1])
        intrinsic_value = 0
        if (option_type == 'C'):
            intrinsic_value = np.maximum(asset_prices - k, 0)
        elif (option_type == 'P'):
            intrinsic_value = np.maximum(k - asset_prices, 0)
        option_values = np.maximum(intrinsic_value, held_value)
        return helper_function(s, k, r, q, dt, u, i-1, option_values, option_type)

# Version 2 CRR using recursion
def binomial_model_recursive(s: float, k: float, t: float, r: float, sigma: float, n: int, option_type: str = 'C'):
    """
    :param s: initial stock price
    :param k: strike price
    :param t: time to expiration
    :param r: risk-free rate
    :param sigma: volatility of underlying asset
    :param n: time interval
    :param option_type: type of the option w/ call option as default
    :return: fair value of the premium for the options contract
    """

    # variables
    dt = t/n # dt: delta-time / step-size in time
    u = np.exp(sigma*np.sqrt(dt)) # u: up-factor
    d = 1/u # down-factor
    q = (np.exp(r*dt) - d) / (u - d) # q: risk-neutral probability (probability of an up move)

    # initialize asset prices at maturity
    asset_prices = np.array([s * u**j * d**(n-j) for j in range(n+1)], dtype=np.float64)

    # initialize option values at maturity
    option_values = 0
    if (option_type == 'C'):
        option_values = np.maximum(asset_prices - k, 0)
    elif (option_type == 'P'):
        option_values = np.maximum(k - asset_prices, 0)

    # backward induction
    return helper_function(s, k, r, q, dt, u, n-1, option_values, option_type)

def main():
    # attain user's input values
    # print("Please answer the following questions to determine the fair premium value")
    # s = float(input("Initial price of the stock: "))
    # k = float(input("Stick price: "))
    # t = float(input("Time until expiration (in years): "))
    # r = float(input("Risk-free rate (as a decimal): "))
    # sigma = float(input("Volatility (as a decimal): "))
    # n = int(input("Number of time steps: "))
    ticker = yf.Ticker("TSLA")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=252)
    hist = ticker.history(start=start_date, end = end_date)
    s = hist['Close'].iloc[-1]
    k = s
    t = 30 / 252
    r = .0436
    sigma = hist['Close'].pct_change().std() * np.sqrt(252)
    n = 100

    # prints the fair premium value
    print(binomial_model_recursive(s, k, t, r, sigma, n))
    print(binomial_model(s, k, t, r, sigma, n))

if __name__ == "__main__":
    main()