import socket

target_host = '127.0.0.1'
target_port = 80

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target server
client.connect((target_host, target_port))

# Send some data (encode to bytes)
client.send(b"AABBCC")

# Receive some data
response = client.recv(4096)  # Read up to 4096 bytes

# Print the received data
print(response.decode(errors="ignore"))

# Close the socket
client.close()
