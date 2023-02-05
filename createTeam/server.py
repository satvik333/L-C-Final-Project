import socket
import json
import threading
from CreateTeam import createteam

def handle_client(client_connection, client_address):
    data = client_connection.recv(1024)
    data = json.loads(data.decode())
    response = createteam.createTeam(data)
    response = json.dumps(response).encode()
    client_connection.sendall(response)
    client_connection.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 3000)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_connection, client_address))
    client_thread.start()
