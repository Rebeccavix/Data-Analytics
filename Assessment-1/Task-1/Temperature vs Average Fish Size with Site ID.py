import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data_Set_Assignmnet_1.csv', skiprows=1)

# Extract relevant columns and remove rows with missing values
water_quality_data = df[["Site ID",
                         "Temperature (°C)", "Avg. Size (cm)"]].dropna()

# Rename columns for easier access
water_quality_data.columns = ["Site_ID", "Temperature_C", "Avg_Size_cm"]

# Plot the graph
plt.figure(figsize=(8, 5))

# Assign different colors for each Site ID
for site in water_quality_data["Site_ID"].unique():
    subset = water_quality_data[water_quality_data["Site_ID"] == site]
    plt.scatter(subset["Temperature_C"], subset["Avg_Size_cm"],
                label=f"Site {site}", alpha=0.7)

plt.xlabel("Water Temperature (°C)")
plt.ylabel("Average Fish Size (cm)")
plt.title("Impact of Water Temperature on Fish Size by Site")
plt.legend()
plt.grid(True)
plt.show()
