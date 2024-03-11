import socket


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server started. Waiting for connections...")

    q = 157
    alpha = 5

    BOBPrivateKey = 15
    BOBPublicKey = pow(alpha, BOBPrivateKey, q)
    print("Generated public key for Bob: ", BOBPublicKey)

    client, address = server.accept()
    print(f"\nClient connected with address: {address}")
    client.sendall(str(BOBPublicKey).encode())
    data = client.recv(1024)
    alicePublicKey = int(data.decode())
    sharedSecret = pow(alicePublicKey, BOBPrivateKey, q)
    print("Recieved public Key from alice: ", alicePublicKey)
    print("Shared secret with Alice:", sharedSecret)

    client.sendall(str(sharedSecret).encode())
    if int(client.recv(1024).decode()) == sharedSecret:
        print("\nShared secret verified.")
    client.close()


if __name__ == "__main__":
    start_server()
