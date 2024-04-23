# Generate server private key
openssl genrsa -out server.key 2048

# Generate server certificate signing request (CSR)
openssl req -new -key server.key -out server.csr 

# Sign the certificate (self-signed)
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
