import math
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Given values
mu = 10  # Population mean
sigma = 0.12  # Population standard deviation
n = 10  # Sample size
alpha = 0.05  # Significance level

# Calculate the standard error
sigma_x_bar = sigma / math.sqrt(n)

# Find the z-value for the given alpha (one-tailed test)
z_alpha = norm.ppf(1 - alpha)

# Calculate the critical value
critical_value = mu + (z_alpha * sigma_x_bar)

# Output the results
print(f"Population mean (μ): {mu}")
print(f"Standard error (σ_x̄): {sigma_x_bar:.5f}")
print(f"Z-value (z_α): {z_alpha:.3f}")
print(f"Critical value: {critical_value:.4f}")

# Rejection region
print(f"Rejection region: x > {critical_value:.4f}")

# Plot the graph
x = np.linspace(mu - 4 * sigma_x_bar, mu + 4 * sigma_x_bar, 1000)
y = norm.pdf(x, loc=mu, scale=sigma_x_bar)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Normal Distribution", color="blue")
plt.axvline(mu, color="black", linestyle="--", label="Mean (μ)")
plt.axvline(critical_value, color="red",
            linestyle="--", label="Critical Value")
plt.fill_between(x, y, where=(x > critical_value), color="red",
                 alpha=0.3, label="Rejection Region")
plt.fill_between(x, y, where=(x <= critical_value),
                 color="green", alpha=0.3, label="Acceptance Region")

plt.title("Normal Distribution with Rejection Region")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()
