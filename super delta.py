import numpy as np
 
inputs = np.array([[0,0],[0,1],[1,0],[1,1]], float)
targets = np.array([0,1,1,1], float)
weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1
 
for epoch in range(20):
    total_error = 0
    for i in range(len(inputs)):
        net_input = np.dot(inputs[i], weights) + bias
        error = targets[i] - net_input
        weights += learning_rate * error * inputs[i]
        bias += learning_rate * error
        total_error += error ** 2
    print("Epoch:", epoch + 1, "Weights:", weights,
          "Bias:", round(bias, 3), "Error:", round(total_error, 3))
 
print("\nFinal Weights:", weights)
print("Final Bias:", bias)
print("\nTesting Delta Rule:")
for input_data in inputs:
    net_input = np.dot(input_data, weights) + bias
    output = 0
    if net_input >= 0.5:
        output = 1
    print("Input:", input_data, "Output:", output)