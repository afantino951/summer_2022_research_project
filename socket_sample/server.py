"""
Author: Andrew Fantino

"""

# Imports
import numpy as np
from numpysocket import NumpySocket

# Global Variables
HOST = "127.0.0.1" # Should add this to a globals files
PORT = 9999 

if __name__ == "__main__":
    npSocket = NumpySocket()
    npSocket.startServer(PORT)

    data_recv = npSocket.recieve(20)
    print(data_recv)
    
    try: 
        npSocket.close()
    except:
        print('socket already closed')
