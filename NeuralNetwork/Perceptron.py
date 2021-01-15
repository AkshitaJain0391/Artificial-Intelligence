# \\ Perceptron without hidden layer
# \\ Inputs ---synapses----> Main Neuron ---> Output


import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

 # formulation of sigmoid sigmoidDerivative
def sigmoidDerivative(x):
    return sigmoid(x)*(1-sigmoid(x))

training_Inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1], 
                            [0,1,1]])

training_Outputs = np.array([[0,1,1,0]]).T

np.random.seed(1) 

# Let's say 'random.seed' gives a value to random value generator ('random.randint()') 
# which generates these values on the basis of this seed. One of the must properties of 
# random numbers is that they should be reproducible. When you put same seed, you get the 
# same pattern of random numbers. This way you are generating them right from the start. 
# You give a different seed- it starts with a different initial

synaptic_Weights = 2 * np.random.random((3,1)) - 1

print('Random Starting Synaptic Weights:')
print(synaptic_Weights)

for iteration in range(1000):
    input_Layer = training_Inputs
    outputs = sigmoid(np.dot(input_Layer, synaptic_Weights))
    error = training_Outputs - outputs
    error_Adjustment = error * sigmoidDerivative(outputs)
    synaptic_Weights += np.dot(input_Layer.T, error_Adjustment)

#print(error_Adjustment)

print('Updated Outputs :') 
print(outputs)



