# Stock Options Pricing Calculator
This Python script provides a user-friendly interface for calculating option prices using three popular pricing models: Binomial, Black-Scholes, and Monte Carlo simulation. The program fetches real-time stock data and allows users to price call or put options for any valid stock ticker.
## Features
- Real-time stock data: Utilizes the yfinance library to fetch current stock prices and historical volatility.
- Multiple pricing models:
  - Binomial model
  - Black-Scholes model
  - Monte Carlo simulation
- User input validation: Ensures valid stock tickers and user choices.
- Flexible option parameters: Allows pricing of both call and put options.
## Prerequisites
Before running the script, make sure you have the following libraries installed:
```
pip install yfinance numpy
```
You'll also need to have the following custom modules in your project directory:
  - binomial_model.py
  - black_scholes_model.py
  - monte_carlo_simulation.py
## Usage
1. Run the script:
```
python main.py
```
2. Enter a valid stock ticker when prompted.
3. Choose a pricing model:
  - bn for Binomial model
  - bs for Black-Scholes model
  - mc for Monte Carlo simulation
4. Select the option type:
  - C for call option
  - P for put option
5. The program will output the calculated option price.
## How it works
1. The script fetches the latest stock price and calculates historical volatility using one year of daily returns.
2. It sets the strike price equal to the current stock price (at-the-money option).
3. The risk-free rate is set to 4.36% (you may want to update this value regularly).
4. The time to expiration is set to 30 days (you can modify this in the t variable).
5. For the Binomial and Monte Carlo models, the number of steps/simulations is set to 1000 for high accuracy (adjustable via the n variable).
## Customization
- You can easily modify the script to change default parameters such as the expiration time, risk-free rate, or number of steps/simulations. Simply adjust the corresponding variables in the main() function.
Contributing
- Feel free to fork this repository and submit pull requests with any improvements or additional features you'd like to see implemented.
