"""
Author: Andrew Fantino

"""

# Imports
import socket
import numpy as np

# Global Constants
HOST = "127.0.0.1" # This is the loop-back interface
PORT = 65432

def init_client_connection():
    """ Init the client connection """
    return


if __name__ == "__main__":
    # Create a np array of ones that is 256x256 bytes of '0xA'

    n_arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    # See this link for correct compression: 
    # https://stackoverflow.com/questions/26377023/send-a-multidimensional-numpy-array-over-a-socket  
 
    # Just the sample echo client and server from  https://realpython.com/python-sockets/
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello World")
        data = s.recv(1024)

    print(f"Received {data!r}")
