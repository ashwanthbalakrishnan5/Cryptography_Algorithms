import socket
from pyDes import *


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server started. Waiting for connections...")

    client, address = server.accept()
    print(f"Client connected with address: {address}")
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0")
    while True:
        data = client.recv(1024)
        if not data:
            break

        print(f"\nReceived encrypted data: {data}\n")
        d = data
        d = k.decrypt(d)
        print("\nDecrypted: %r" % d)
        print("\n")
        client.sendall("Closing connection".encode())
    client.close()


if __name__ == "__main__":
    start_server()
