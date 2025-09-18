import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data_Set_Assignmnet_1.csv', skiprows=1)

# Extract relevant columns and remove rows with missing values
water_quality_data = df[["Temperature (°C)", "Avg. Size (cm)"]].dropna()

# Rename columns for easier access
water_quality_data.columns = ["Temperature_C", "Avg_Size_cm"]

# Plot the graph
plt.figure(figsize=(8, 5))
plt.scatter(water_quality_data["Temperature_C"],
            water_quality_data["Avg_Size_cm"], alpha=0.7, c="orange")
plt.xlabel("Water Temperature (°C)")
plt.ylabel("Average Fish Size (cm)")
plt.title("Impact of Water Temperature on Fish Size")
plt.grid(True)
plt.show()
