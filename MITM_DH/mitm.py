import socket


def start_client():

    q = 157
    alpha = 5

    mitmPrivateKey = 10
    mitmPublicKey = pow(alpha, mitmPrivateKey, q)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 23456))
    server.listen(1)

    print("Server started. Waiting for connections...")
    client, address = server.accept()
    print("Generated public key for Mallory: ", mitmPublicKey)
    print(f"\nClient connected with address: {address}")
    client.sendall(str(mitmPublicKey).encode())
    data = client.recv(1024)
    alicePublicKey = int(data.decode())
    sharedSecret = pow(alicePublicKey, mitmPrivateKey, q)
    print("Recieved public Key from alice: ", alicePublicKey)
    print("Shared secret with Alice:", sharedSecret)
    client.sendall(str(sharedSecret).encode())
    if int(client.recv(1024).decode()) == sharedSecret:
        print("\nShared secret verified.")
    client.close()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))
    print("\n\nConnected to Bob as Alice (Mallory)")
    data = client.recv(1024)
    client.sendall(str(mitmPublicKey).encode())
    BOBPublicKey = int(data.decode())
    sharedSecret = pow(BOBPublicKey, mitmPrivateKey, q)
    print("Recieved public Key from BOB: ", BOBPublicKey)
    print("Shared secret with BOB:", sharedSecret)
    client.sendall(str(sharedSecret).encode())
    if int(client.recv(1024).decode()) == sharedSecret:
        print("\nShared secret verified.")

    client.close()


if __name__ == "__main__":
    start_client()
