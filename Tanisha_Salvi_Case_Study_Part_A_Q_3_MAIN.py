import matplotlib.pyplot as plt
import numpy as np

# Futures price, strike price and premium
F = 1000
K = 1000
premium = 100

# Generate price of the asset
x = np.linspace(600, 1400, 100)

# Payoff for the short futures contract
payoff_futures = F - x

# Payoff for the put option
payoff_option = np.maximum(K - x, 0) - premium

plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

# Plot the payoffs
plt.plot(x, payoff_futures, label='Short Futures', linewidth=3.0, color = 'red')
plt.plot(x, payoff_option, label='Put Option', linewidth=3.0, color = 'blue')

# Mark the regions where the futures contract and the put option outperform each other
plt.fill_between(x, payoff_futures, payoff_option, where=(payoff_futures > payoff_option), color='yellow', alpha=0.5, label='Futures Outperforms')
plt.fill_between(x, payoff_futures, payoff_option, where=(payoff_option > payoff_futures), color='pink', alpha=0.5, label='Put Outperforms')

# Add labels and show the plot
plt.xlabel('Payoff of Short Futures vs Long Put Option')
plt.ylabel('Payoff')
plt.title("Payoff vs Price of Asset")
plt.legend()
plt.axhline(y=0, color='black')
plt.axvline(x=K, color='green', linestyle='--', label='Strike of the Option')
plt.axvline(x=F, color='green', linestyle='--', label='Futures Price')
plt.axhline(y=-premium,  xmax=0.5, color='orange', linestyle='--')
plt.text(K, -50, 'Strike of the option', rotation=0)
plt.text(F, +50, 'Futures Price', rotation=0)
plt.text(600, -premium, 'Premium', rotation=0)
plt.grid()
plt.show()
