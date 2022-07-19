"""
Author: Andrew Fantino

"""

# Imports
import socket

# Glocal Variables
HOST = "127.0.0.1" # Should add this to a globals files
PORT = 65432 

def begin_server():
    pass


if __name__ == "__main__":

    # Sample application from https://realpython.com/python-sockets/
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

