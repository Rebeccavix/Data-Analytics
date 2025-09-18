import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "Data_Set_Assignmnet_1.csv"
data = pd.read_csv(file_path, skiprows=1)

# Extract relevant columns and remove rows with missing values
fish_population_data = data[["Temperature (°C)", "Species", "Count"]].dropna()

# Rename columns for easier access
fish_population_data.columns = ["Temperature_C", "Species", "Count"]

# Plot the graph
plt.figure(figsize=(8, 5))

# Group by species and plot each species
for species in fish_population_data["Species"].unique():
    subset = fish_population_data[fish_population_data["Species"] == species]
    plt.scatter(subset["Temperature_C"], subset["Count"],
                label=species, alpha=0.7)

plt.xlabel("Water Temperature (°C)")
plt.ylabel("Fish Count")
plt.title("Fish Species Distribution by Temperature")
plt.legend()
plt.grid(True)
plt.show()
