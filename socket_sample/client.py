"""
Author: Andrew Fantino

"""

# Imports
import numpy as np
from numpysocket import NumpySocket
from time import sleep

# Global Constants
HOST = "127.0.0.1" # This is the loop-back interface
PORT = 9999

if __name__ == "__main__":
    # Create a np array of ones that is 256x256 bytes of '0xA'
    n_arr = np.array([[1, 2, 3], [4, 5, 6]]) # <- is not ^ (yet)

    npSocket = NumpySocket()

    while(True):
        try: 
            npSocket.startClient(HOST, PORT)
            break
        except:
            print('Connection failed')
            sleep(1)
            continue

    npSocket.send(n_arr)
    print('sent arr')
    
    npSocket.close()
