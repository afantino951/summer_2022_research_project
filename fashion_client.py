# File Imports 
from fashion_mnist_example.network import Network
from fashion_mnist_example.runner import RunBuilder, RunManager

# Torch Imports 
import torch
import torch.nn as nn

#Numpy Imports
import numpy as np
from NumpySocket.numpysocket import NumpySocket

# Misc Imports
from time import sleep
from timeit import default_timer as timer


original_model = Network(pretrained=True)

# TODO Change this to use our custom pretrained model
class ClientNetwork(nn.Module):

    def __init__(self) -> None:
        super(Network, self).__init__()
        self.features = nn.Sequential(
            # stop at conv4
                    *list(original_model.features.children())[:-3]
        )

    def forward(self, x):
        x = self.features(x)
        return x


if __name__ == '__main__':
    # Constants related to the network for the TCP socket
    TCP_IP1 ='129.32.94.251'
    TCP_PORT1 = 5006
    BUFFER_SIZE = 4096

    # Create the numpy socket objects
    np_socket = NumpySocket()

    # Create the client portion of the network
    # TODO replace input data with correct random mnist test images
    images = torch.zeros(9,3,224,224) 
    client_model = ClientNetwork()
    

    # Connect to server
    print('Connecting to Server')
    while 1:
        try:
            np_socket.startClient(TCP_IP1, TCP_PORT1)
            break
        except:
            print('Connection failed')
            sleep(1)
            continue
    
    # Run Forward Pass through 
    client_results = client_model(images)

    # Send results from client network through the socket
    np_socket.send(client_results)
    print('sent arr')
    np_socket.close()

