import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('Data_Set_Assignmnet_1.csv', skiprows=1)

# Extract relevant columns and remove rows with missing values
fish_population_data = df[["Site ID", "Species", "Count"]].dropna()

# Group the data by Site ID and Species, and calculate the total fish count
grouped_data = fish_population_data.groupby(
    ["Site ID", "Species"]).sum().reset_index()

# Pivot the data to prepare for plotting
pivot_data = grouped_data.pivot(
    index="Species", columns="Site ID", values="Count")

# Plot the grouped bar chart
pivot_data.plot(kind="bar", figsize=(10, 6))

plt.xlabel("Species")
plt.ylabel("Total Fish Count")
plt.title("Total Fish Count for Each Species Across Sites")
plt.legend(title="Site ID")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
