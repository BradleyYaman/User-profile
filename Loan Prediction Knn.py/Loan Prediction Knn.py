from sklearn.neighbors import KNeighborsClassifier

# Training data (Age, Credit Rating, Loan Value)
X_train = [
    [40, 5, 60], 
    [50, 7, 60], 
    [50, 7, 40], 
    [70, 7, 60], 
    [70, 4, 60], 
    [60, 7, 60]
]

# Corresponding labels (Accepted or Denied)
y_train = ['DENIED', 'ACCEPT', 'ACCEPT', 'ACCEPT', 'DENIED', 'ACCEPT']

# Initialize the KNN model with the number of neighbors (n_neighbors) of 2
knn_2 = KNeighborsClassifier(n_neighbors=2)

# Train the model using training data
knn_2.fit(X_train, y_train)

# Test data (New loan application: Age=50, Credit Rating=3, Loan Value=40)
X_test = [[50, 3, 40]]

# Predict using the trained model
predictions_2 = knn_2.predict(X_test)

# Display prediction results
print("Prediction Result for K=2:")
for i, pred in enumerate(predictions_2):
    print(f"Test Data {i+1}: Predicted Class = {pred}")

# Initialize the KNN model with the number of neighbors (n_neighbors) of 5
knn_5 = KNeighborsClassifier(n_neighbors=5)

# Train the model using training data
knn_5.fit(X_train, y_train)

# Predict using the trained model
predictions_5 = knn_5.predict(X_test)

# Display prediction results
print("\nPrediction Result for K=5:")
for i, pred in enumerate(predictions_5):
    print(f"Test Data {i+1}: Predicted Class = {pred}")
