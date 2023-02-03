import socket
from .createTeam import createTeam

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 3000)
server_socket.bind(server_address)

server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    data = client_connection.recv(1024)

    response = createTeam(data)
    client_connection.sendall(response)

    client_connection.close()
