import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import numpy as np

# Load the dataset
data = pd.read_csv(
    r'c:\Users\VK\Documents\MSE-Courses\MSE806-Intelligent Transportation Systems\Week 6\ITS_ML_dataset_Mukesh.csv')

# Inspect the dataset
print("Dataset Head:")
print(data.head())

# Group data by Zone
zones = data['Zone'].unique()

# Initialize the plot
plt.figure(figsize=(10, 6))

for zone in zones:
    print(f"\nZone: {zone}")
    zone_data = data[data['Zone'] == zone]

    # Extract features and target
    X = zone_data[['TrafficVolume', 'Accidents', 'BusRidership']]  # Features
    y = zone_data['DelayMinutes']  # Target

    # Create an SVM model for regression
    model = SVR(kernel='linear')  # Using a linear kernel for simplicity

    # Train the model
    model.fit(X, y)

    # Predict delays
    y_pred = model.predict(X)

    # Display average predicted delay
    average_delay = np.mean(y_pred)
    print(
        f"Average Predicted Delay for Zone {zone}: {average_delay:.6f} minutes")

    # Display the contribution of features (cause of delay)
    print(f"Features contributing to delay in Zone {zone}:")
    print(f"Traffic Volume: {zone_data['TrafficVolume'].mean():.6f}")
    print(f"Accidents: {zone_data['Accidents'].mean():.6f}")
    print(f"Bus Ridership: {zone_data['BusRidership'].mean():.6f}")

    # Add data and predictions to the plot
    plt.scatter(zone_data['TrafficVolume'], y,
                label=f'Actual Data (Zone {zone})')
    plt.plot(zone_data['TrafficVolume'], y_pred,
             label=f'Predicted Data (Zone {zone})')

# Customize the plot
plt.xlabel('Traffic Volume')
plt.ylabel('Delay (Minutes)')
plt.title('Traffic Volume vs Delay Regression (All Zones - SVM)')
plt.legend()
plt.show()
