import socket
from dss import dss
import json
import gmpy2


def start_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12348))

    message = input("Enter a message: ")

    list = dss(message)
    message = str(list)

    client.sendall(message.encode())
    data = client.recv(1024)
    print(f"\n---------{data.decode()}---------")

    client.close()


if __name__ == "__main__":
    start_client()
