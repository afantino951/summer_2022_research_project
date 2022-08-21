# File Imports 
from fashion_mnist_example.network import Network
from fashion_mnist_example.runner import RunBuilder, RunManager

# Torch Imports 
import torch
import torch.nn as nn

#Numpy Imports
import numpy as np
from NumpySocket.numpysocket import NumpySocket

class Flatten(nn.Flatten):
    def __init__(self, start_dim: int = 1, end_dim: int = -1) -> None:
        super(Flatten, self).__init__(start_dim, end_dim)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        return x

original_model = Network(pretrained=True)

# TODO Change this to use our custom pretrained model
class ServerNetwork(nn.Module):

    def __init__(self) -> None:
        super(Network, self).__init__()
        self.features =  nn.Sequential(
            # TODO update the following line with correct info
 		    *(list(original_model.features.children())[-3:] + [nn.AvgPool2d(1), Flatten()] + list(original_model.classifier.children()))
        )

    def forward(self, x):
        x = self.features(x)
        return x


if __name__ == '__main__':
    # Constants related to the network for the TCP socket
    TCP_IP1 ='129.32.94.251'
    TCP_PORT1 = 5006
    BUFFER_SIZE = 4096

    # Create the numpy socket object
    np_socket = NumpySocket()

    # Create the server portion of the network
    server_model = ServerNetwork()

    # Wait for receiving data from the client
    print('Waiting for Raspi to respond')
    np_socket.startServer(TCP_PORT1)
    data_recv = np_socket.recieve(BUFFER_SIZE)

    print(data_recv)

    # TODO Pass raw data recv to the rest of the custom model


    # TODO Print the prediction stats and accuracy information

    
    # TODO Send model output through a new socket