import numpy as np
 
inputs = np.array([[1,1],[1,-1],[-1,1],[-1,-1]], float)
weights = np.zeros((2,2))
learning_rate = 0.1
 
for input_data in inputs:
    weights += learning_rate * np.outer(input_data, input_data)
    print("\nInput:", input_data)
    print("Updated Weight Matrix:\n", weights)
 
print("\nFinal Hebbian Weight Matrix:\n", weights)