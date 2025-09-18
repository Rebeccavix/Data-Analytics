import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data_Set_Assignmnet_1.csv', skiprows=1)

# Remove rows where Site ID is nan
df = df.dropna(subset=["Site ID"])

# Extract relevant columns for plotting
dissolved_oxygen = df["Dissolved Oxygen (mg/L)"]
fish_count = df["Count"]
site_id = df["Site ID"]

# Plot the graph
plt.figure(figsize=(8, 5))

# Assign different colors for each Site ID
for site in site_id.unique():
    subset = df[df["Site ID"] == site]
    plt.scatter(subset["Dissolved Oxygen (mg/L)"],
                subset["Count"], label=f"Site {site}", alpha=0.7)

plt.xlabel("Dissolved Oxygen (mg/L)")
plt.ylabel("Fish Count")
plt.title("Relationship between Dissolved Oxygen and Fish Count by Site")
plt.legend(title="Site ID")
plt.grid(True)
plt.show()
