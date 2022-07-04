import numpy as np

class MLP:

    #num_hidden uma camada escondida e os numeros são os neuronios
    #num_outputs e o numero de neuronios de saida

    #esse e o constructor
    def __init__(self,num_inputs=5,num_hidden=[3,5],num_outputs=2):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs
        #internal representation of the layers
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs]


        #iniciate random weights
        self.weights = []
        # creates random arrays, in which have random dimensions
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i],layers[i+1])
            self.weights.append(w)

    def forward_propagate(self,inputs):
        activations = inputs

        for w in self.weights:
            #calculate the net input
            net_inputs = np.dot(activations,w) #matrix multiplication

            #calculate the activations
            activations = self._sigmoid(net_inputs)
        return activations

    def _sigmoid(self, x):
        return 1 / (1+np.exp(-x))

if __name__ == "__main__":
    #create an MLP
    mlp = MLP()
    #create inputs
    inputs = np.random.rand(mlp.num_inputs)
    #perform forward prop
    outputs = mlp.forward_propagate(inputs)
    #print results
    print("the network output in: {}".format(inputs))
    print("the network output in: {}".format(outputs))