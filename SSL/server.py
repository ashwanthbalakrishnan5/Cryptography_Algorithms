import socket
import ssl

# Server settings
host = '127.0.0.1'  
port = 5000 

# Load SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Create a socket and wrap it in SSL/TLS 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_side=True) as secure_socket:
        secure_socket.bind((host, port))
        secure_socket.listen(1)  # Listen for a single client
        print('Server listening...')

        # Accept a client connection
        client_socket, addr = secure_socket.accept()
        print(f'Connected by {addr}')

        # Handle client communication
        while True:
            data = client_socket.recv(1024)
            if not data: 
                break
            print(f'Received: {data.decode()}')
            client_socket.sendall(data)  # Echo data back 
        
