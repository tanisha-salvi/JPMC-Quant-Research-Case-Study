import numpy as np
import matplotlib.pyplot as plt

def call_payoff(sT, strike_price, premium):
    return np.maximum(sT - strike_price, 0) - premium

# Assume expiration date is in 1 year
expiration_date = 1

# Assume underlying asset price starts at $50
s0 = 50

# Assume the strike prices of the call options are $45, $50 and $55
strike_prices = np.array([40, 60, 80])

# Assume the premiums for the call options are $2, $1, and $2 respectively
premiums = np.array([2, 1, 2])

# Create a range of stock prices at expiration date
sT = np.arange(0, 2 * s0, 5)

# Calculate the payoffs of each call option at expiration
payoff_long_ITM = call_payoff(sT, strike_prices[0], premiums[0])
payoff_long_OTM = call_payoff(sT, strike_prices[2], premiums[2])
payoff_short_ATM1 = -call_payoff(sT, strike_prices[1], premiums[1])
payoff_short_ATM2 = -call_payoff(sT, strike_prices[1], premiums[1])

# Calculate the combined payoffs of the trade
payoff_combined = payoff_long_ITM + payoff_long_OTM + payoff_short_ATM1 + payoff_short_ATM2

# Plot the payoffs
plt.plot(sT, payoff_long_ITM, '-', label='Long ITM Call', color='r')
plt.plot(sT, payoff_long_OTM, '-', label='Long OTM Call', color='b')
plt.plot(sT, payoff_short_ATM1, '--', label='Short ATM Call 1', color='g')
plt.plot(sT, payoff_short_ATM2, '--', label='Short ATM Call 2', color='g')
plt.plot(sT, payoff_combined, '-', label='Combined Payoff', color='black', linewidth = 2.0)
plt.legend()
plt.xlabel('Stock Price at Expiration')
plt.ylabel('Payoff')
# plt.title('Payoff of Long ITM Call + Long OTM Call + Short 2 ATM Calls')
plt.grid()
plt.show()
