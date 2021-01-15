import numpy as np

class NeuralNetwork():

    def __init__(self):

        np.random.seed(1)
        self.synaptic_Weights = 2 * np.random.random((3,1)) - 1

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

 # formulation of sigmoid sigmoidDerivative
    def sigmoidDerivative(self, x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def training(self, training_Inputs, training_Outputs, training_Iterations):
        for iteration in range(training_Iterations):
            outputs = self.think(training_Inputs)
            error = training_Outputs - outputs
            adjustment_Error = np.dot(training_Inputs.T, error * self.sigmoidDerivative(outputs))
            self.synaptic_Weights += adjustment_Error
    
    def think(self, inputs):
        inputs = inputs.astype(float)
        z = np.dot(inputs, self.synaptic_Weights)
        output = self.sigmoid(z)
        return output


if __name__ == "__main__":

    neural_Network = NeuralNetwork()
    print("Randon Synaptic Weights :")
    print(neural_Network.synaptic_Weights)
    

    # Training of perceptron
    training_Inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1], 
                            [0,1,1]])

    training_Outputs = np.array([[0,1,1,0]]).T  

    neural_Network.training(training_Inputs, training_Outputs, 1000)

    print("Synaptic Weights after training:")
    print(neural_Network.synaptic_Weights)

    #Input Feeding

    A = str(input("Input 1:"))
    B = str(input("Input 2:"))
    C = str(input("Input 3:"))

    print("Output Data for New Inputs:")
    print(neural_Network.think(np.array([A,B,C])))