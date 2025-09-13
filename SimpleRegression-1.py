import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(
    r'c:\Users\VK\Documents\MSE-Courses\MSE806-Intelligent Transportation Systems\Week 6\ITS_ML_dataset_Mukesh.csv')

# Inspect the dataset
print("Dataset Head:")
print(data.head())

# Assuming the dataset has columns 'TrafficVolume' and 'DelayMinutes'
X = data[['TrafficVolume']]  # Feature
y = data['DelayMinutes']  # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Calculate and display the average predicted delay
average_delay = np.mean(y_pred)
print(f"Average Predicted Delay: {average_delay:.2f} minutes")

# Calculate the regression line
regression_line = model.coef_[0] * X_test + model.intercept_

# Visualize the regression line
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, regression_line, color='red', label='Regression Line')
plt.xlabel('Traffic Volume')
plt.ylabel('Delay (Minutes)')
plt.title('Traffic Volume vs Delay Regression')
plt.legend()
plt.show()
