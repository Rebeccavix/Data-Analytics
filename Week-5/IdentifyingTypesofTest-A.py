import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given values
mu = 1/8  # Hypothesized proportion (mean)
sigma = 0.02  # Example standard deviation (adjust as needed)
alpha = 0.05  # Significance level for left-tailed test

# Calculate the critical value for the left-tailed test
z_alpha = norm.ppf(alpha)
critical_value = mu + z_alpha * sigma

# Generate x values for the normal distribution
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
y = norm.pdf(x, loc=mu, scale=sigma)

# Plot the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Normal Distribution", color="blue")
plt.axvline(mu, color="black", linestyle="--", label="Mean (μ)")
plt.axvline(critical_value, color="red",
            linestyle="--", label="Critical Value")
plt.fill_between(x, y, where=(x < critical_value), color="red",
                 alpha=0.3, label="Rejection Region")
plt.fill_between(x, y, where=(x >= critical_value),
                 color="green", alpha=0.3, label="Acceptance Region")

# Add labels and title
plt.title("Left-Tailed Test: Normal Distribution with Rejection Region")
plt.xlabel("Proportion")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()
