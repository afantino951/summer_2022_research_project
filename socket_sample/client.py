"""
Author: Andrew Fantino

"""

# Imports
import socket

# Global Constants
HOST = "127.0.0.1" # This is the loop-back interface
PORT = 65432

def init_connection():
    pass


if __name__ == "__main__":
    
    # Just the sample echo client and server from  https://realpython.com/python-sockets/
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST, PORT))
        s.sendall(b"Hello World")
        data = s.recv(1024)

    print(f"Received {data!r}")
    
