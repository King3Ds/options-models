import numpy as np

def monte_carlo(s: float, k: float, t: float, r: float, sigma: float, n: int, option_type: str = 'C'):
    """
    :param s: initial stock price
    :param k: strike price
    :param t: time to expiration
    :param r: risk-free rate
    :param sigma: volatility of underlying asset
    :param option_type: type of the option w/ call option as default
    :return: fair value of the premium for the options contract
    """
    z = np.random.standard_normal(n)
    s_t = s*np.exp((r-(sigma**2)/2)*t + sigma*np.sqrt(t)*z)
    payoff = np.zeros(n)

    if (option_type == 'C'):
        payoff = np.maximum(s_t - k, 0)
    elif (option_type == 'P'):
        payoff = np.maximum(k - s_t, 0)

    return np.exp(-r*t)*np.mean(payoff)

