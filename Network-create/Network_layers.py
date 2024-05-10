import numpy as np
import math
class network_layer:
    def __init__(self,inp_size,layer_size,act="none",lo=-10,hi=10):
        self.shape_weight = (inp_size,layer_size)
        self.shape = (1,layer_size)
        self.W = np.random.randint(low=lo,high=hi,size=self.shape_weight)
        self.b = np.random.randint(low=lo,high=hi,size=self.shape_weight[1])
        self.z = np.random.randint(2,size=self.shape)
        self.a = self.z
        self.inp = np.random.randint(2,size=inp_size)
        self.func = act
    # Forward propogation
    def act_func(self):
        self.a = self.z
        if self.func == "none":
            pass
        elif self.func == "relu":
            for i in range(len(self.a)):
                if (self.a[i] < 0):
                    self.a[i] = 0
        elif self.func == "tanh":
            for i in range(len(self.a)):
                self.a[i] = math.tanh(self.a[i])
        elif self.func =="softmax":
            sum = 0
            for i in range(len(self.a)):
                self.a[i] = math.exp(self.a[i])
                sum += self.a[i]
            self.a = self.a/sum
        else:
            raise Exception("unrecognised funciton keyword")
    def calculate(self,inp):
        self.inp = inp
        self.z = (inp @ self.W) + self.b
        self.act_func()
        return self.a

def init_network(no_of_layers,layer_data,inp_size):
    # layer data = [[layer_size,act_func],...]
    network = []
    network.append(network_layer(inp_size,layer_data[0][0],act= layer_data[0][1]))
    for i in range(1,no_of_layers):
        network.append(network_layer(layer_data[i-1][0],layer_data[i][0],layer_data[i][1]))
    return network
def predict(inp,network):
    prev_out = inp
    for i in len(network):
        current_layer = network[i]
        prev_out = current_layer.calculate(prev_out)
    return prev_out
