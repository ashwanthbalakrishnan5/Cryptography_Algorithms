import socket
import ssl

# Client settings
host = "127.0.0.1"
port = 5000

# Load SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("server.crt")  # Load server certificate

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Create a socket and wrap it in SSL/TLS
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=host) as secure_socket:
        secure_socket.connect((host, port))
        print("Connected to the server")

        # Client communication
        while True:
            message = input("Enter message: ")
            secure_socket.sendall(message.encode())
            data = secure_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
            if message.lower() == "quit":
                break
