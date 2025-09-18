import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Data_Set_Assignmnet_1.csv', skiprows=1)

# Extract relevant columns for plotting
dissolved_oxygen = df["Dissolved Oxygen (mg/L)"]
fish_count = df["Count"]

# Plot the graph
plt.figure(figsize=(8, 5))
plt.scatter(dissolved_oxygen, fish_count, alpha=0.7, color="orange")
plt.xlabel("Dissolved Oxygen (mg/L)")
plt.ylabel("Fish Count")
plt.title("Relationship between Dissolved Oxygen and Fish Count")
plt.grid(True)
plt.show()
