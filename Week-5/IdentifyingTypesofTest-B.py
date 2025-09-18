import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given values
mu = 8  # Hypothesized mean (average length of phone call)
sigma = 0.5  # Example standard deviation (adjust as needed)
alpha = 0.05  # Significance level for two-tailed test

# Calculate the critical values for the two-tailed test
z_alpha_half = norm.ppf(1 - alpha / 2)  # Upper critical z-value
critical_value_upper = mu + z_alpha_half * sigma
critical_value_lower = mu - z_alpha_half * sigma

# Generate x values for the normal distribution
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
y = norm.pdf(x, loc=mu, scale=sigma)

# Plot the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Normal Distribution", color="blue")
plt.axvline(mu, color="black", linestyle="--", label="Mean (μ)")
plt.axvline(critical_value_upper, color="red",
            linestyle="--", label="Upper Critical Value")
plt.axvline(critical_value_lower, color="red",
            linestyle="--", label="Lower Critical Value")
plt.fill_between(x, y, where=(x < critical_value_lower),
                 color="red", alpha=0.3, label="Rejection Region (Left)")
plt.fill_between(x, y, where=(x > critical_value_upper),
                 color="red", alpha=0.3, label="Rejection Region (Right)")
plt.fill_between(x, y, where=(x >= critical_value_lower) & (x <= critical_value_upper),
                 color="green", alpha=0.3, label="Acceptance Region")

# Add labels and title
plt.title("Two-Tailed Test: Normal Distribution with Rejection Regions")
plt.xlabel("Average Length of Phone Call (minutes)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()
