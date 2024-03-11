import socket
from pyDes import *


def start_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    message = input("Enter a message: ")
    data = message
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0")
    d = k.encrypt(data)
    print("Encrypted: %r" % d)

    client.sendall(d)
    data = client.recv(1024)
    print(f"\n---------{data.decode()}---------")

    client.close()


if __name__ == "__main__":
    start_client()
