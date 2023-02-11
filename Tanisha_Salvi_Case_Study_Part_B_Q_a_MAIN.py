import matplotlib.pyplot as plt
import numpy as np

# Define the strike price, premium, and underlying asset price range
strike = 1000
premium_call = 50
premium_put = 100
S = np.arange(800, 1200, 25)

# Calculate the payoffs for the call and put options
payoff_call = np.maximum(S - strike, 0) - premium_call
payoff_put = np.maximum(strike - S, 0) - premium_put
payoff_total = np.maximum(S - strike, 0) - premium_call + np.maximum(strike - S, 0) - premium_put

# Plot the payoffs
plt.plot(S, payoff_call, label='Call Option')
plt.plot(S, payoff_put, label='Put Option')
plt.plot(S, payoff_total, label='Total', linewidth = 3.0)

# Add labels and a legend
plt.xlabel('Underlying Asset Price')
plt.ylabel('Payoff')
plt.legend()
plt.grid()

# Show the plot
plt.show()