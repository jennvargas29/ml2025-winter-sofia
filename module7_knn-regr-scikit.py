#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# User input for N and k
N = int(input("Enter the number of data points (N): "))
k = int(input("Enter the number of neighbors (k): "))

if k > N:
    raise ValueError("Error: k cannot be greater than N")

# Initialize arrays for user input
X_train = np.empty((N, 1))  
Y_train = np.empty(N)       

# Read N data points from user
print("Enter data points (x y):")
for i in range(N):
    x, y = map(float, input(f"Point {i+1}: ").split())
    X_train[i] = x
    Y_train[i] = y

# Compute and print variance of Y values
variance_y = np.var(Y_train)
print(f"Variance of training labels: {variance_y:.4f}")

# User input for test X value
X_test = np.array([[float(input("Enter X value for prediction: "))]])

# Train k-NN Regressor
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train, Y_train)

# Predict and print output
Y_pred = knn.predict(X_test)
print(f"Predicted Y value for X={X_test[0][0]}: {Y_pred[0]:.4f}")


# In[ ]:





# In[ ]:




