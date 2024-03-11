import socket


def start_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 23456))

    print("Connected to Bob.\n")

    q = 157
    alpha = 5

    AlicePrivateKey = 27
    AlicePublicKey = pow(alpha, AlicePrivateKey, q)

    print("Generated Alice's public key: ", AlicePublicKey)

    data = client.recv(1024)
    client.sendall(str(AlicePublicKey).encode())

    BOBPublicKey = int(data.decode())
    sharedSecret = pow(BOBPublicKey, AlicePrivateKey, q)
    print("Recieved public Key from BOB: ", BOBPublicKey)
    print("Shared secret with BOB:", sharedSecret)

    client.sendall(str(sharedSecret).encode())
    if int(client.recv(1024).decode()) == sharedSecret:
        print("Shared secret verified.")
    client.close()


if __name__ == "__main__":
    start_client()
