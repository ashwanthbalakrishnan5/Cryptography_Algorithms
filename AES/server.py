import socket
from aes import AES


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server started. Waiting for connections...")

    client, address = server.accept()
    print(f"Client connected with address: {address}")
    master_key = 0x2B7E151628AED2A6ABF7158809CF4F3C
    aes = AES(master_key)
    while True:
        data = client.recv(1024)
        if not data:
            break
        encrypted_data = data.decode()
        print(f"Received encrypted data: {hex(int(encrypted_data))}\n")
        ciphertext = encrypted_data
        decrypted = aes.decrypt(int(ciphertext))
        decrypted_string = bytes.fromhex(hex(decrypted)[2:]).decode()
        print("\nDecrypted message: " + decrypted_string)
        print("\n")
        client.sendall("Closing connection".encode())
    client.close()


if __name__ == "__main__":
    start_server()
