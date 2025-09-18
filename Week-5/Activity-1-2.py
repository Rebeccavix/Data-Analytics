import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given values
mu = 10          # Population mean under H0
sigma = 0.12     # Population standard deviation
n = 10           # Sample size
alpha = 0.05     # Significance level

# Step 1: Find z_alpha for one-tailed test
z_alpha = norm.ppf(1 - alpha)

# Step 2: Calculate critical value
critical_value = mu + z_alpha * (sigma / math.sqrt(n))

# Step 3: Print results
print(f"Z-critical value (z_alpha): {z_alpha:.4f}")
print(f"Critical value for rejection region: {critical_value:.4f}")

# Step 4: Plot the normal distribution
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma / math.sqrt(n))

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sampling Distribution', color='blue')

# Shade rejection region
x_reject = np.linspace(critical_value, mu + 4*sigma, 300)
y_reject = norm.pdf(x_reject, mu, sigma / math.sqrt(n))
plt.fill_between(x_reject, y_reject, color='red',
                 alpha=0.5, label='Rejection Region')

# Add critical value line
plt.axvline(critical_value, color='black', linestyle='--',
            label=f'Critical Value = {critical_value:.4f}')

# Labels and legend
plt.title('One-Tailed Hypothesis Test (Right Tail)')
plt.xlabel('Sample Mean')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
