import socket
from aes import AES


def start_client():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    message = input("Enter a message: ")
    master_key = 0x2B7E151628AED2A6ABF7158809CF4F3C
    aes = AES(master_key)
    plaintext = message
    plaintext_hex = plaintext.encode().hex()
    message = aes.encrypt(int(plaintext_hex, 16))
    print("\nEncrypted message: " + hex(message))

    message = str(message)
    client.sendall(message.encode())
    data = client.recv(1024)
    print(f"\n---------{data.decode()}---------")

    client.close()


if __name__ == "__main__":
    start_client()
