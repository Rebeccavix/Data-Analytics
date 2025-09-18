import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
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
    X = zone_data[['TrafficVolume']]  # Feature
    y = zone_data['DelayMinutes']  # Target

    # Create a Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X, y)

    # Predict delays
    y_pred = model.predict(X)

    # Calculate the regression line
    regression_line = model.coef_[0] * X + model.intercept_

    # Display the regression coefficient, intercept, and average predicted delay
    print(f"Regression Coefficient: {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")
    average_delay = np.mean(y_pred)
    print(
        f"Average Predicted Delay for Zone {zone}: {average_delay:.2f} minutes")

    # Add data and regression line to the plot
    plt.scatter(X, y, label=f'Actual Data (Zone {zone})')
    plt.plot(X, regression_line, label=f'Regression Line (Zone {zone})')

# Customize the plot
plt.xlabel('Traffic Volume')
plt.ylabel('Delay (Minutes)')
plt.title('Traffic Volume vs Delay Regression (All Zones)')
plt.legend()
plt.show()
