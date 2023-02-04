import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 3000)
client_socket.connect(server_address)

with open("C:/Users/satvik.ms/Desktop/L-C-Final-Project/TeamsInputJSON.json", "r") as f:
    data = json.load(f)
message = json.dumps(data).encode()
client_socket.sendall(message)

data = client_socket.recv(1024)
client_socket.close()

print('Received:', data.decode())
