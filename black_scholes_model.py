import numpy as np
from scipy.stats import norm

def black_scholes(s: float, k: float, t: float, r: float, sigma: float, option_type: str = 'C') -> float:
    """
    :param s: initial stock price
    :param k: strike price
    :param t: time to expiration
    :param r: risk-free rate
    :param sigma: volatility of underlying asset
    :param option_type: type of the option w/ call option as default
    :return: fair value of the premium for the options contract
    """
    d_1 = (np.log(s/k) + (r + (sigma**2)/2)*t) / (sigma * np.sqrt(t))
    d_2 = d_1 - sigma * np.sqrt(t)

    if (option_type == 'C'):
        n_1 = norm.cdf(d_1)
        n_2 = norm.cdf(d_2)
        return n_1 * s - n_2 * k * np.exp(-r * t)

    elif (option_type == 'P'):
        n_1 = norm.cdf(-d_1)
        n_2 = norm.cdf(-d_2)
        return n_2 * k * np.exp(-r * t) - n_1 * s
