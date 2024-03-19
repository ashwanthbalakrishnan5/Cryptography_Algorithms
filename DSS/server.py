import socket
import json
from dss import dss_verify
import gmpy2


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12348))
    server.listen(1)
    print("Server started. Waiting for connections...")

    client, address = server.accept()
    print(f"Client connected with address: {address}")
    while True:
        data = client.recv(102400)
        if not data:
            break
        data = data.decode()
        M, r, s, p, q, g, y = eval(data)
        print(f"Received Msg: {M}\n")
        M += b"_modified"
        print(f"Modified Msg: {M}\n")
        dss_verify(M, r, s, p, q, g, y)
        print("\n")
        client.sendall("Closing connection".encode())
    client.close()


if __name__ == "__main__":
    start_server()
