import socket
import json
from createTeam import CreateTeam
from createFixtures import CreateFixtures

def handle_create_team(data):
    CreateTeam.createteam.createTeam(data)
    return {"status": "success", "message": "Team created successfully"}

def handle_create_fixture(data):
    CreateFixtures.createfixtures.createFixtures(data)
    return {"status": "success", "message": "Fixture created successfully"}

def handle_request(request):
    data = json.loads(request.decode())
    action = data["action"]

    if action == "create_team":
        response = handle_create_team(data)
    elif action == "create_fixture":
        response = handle_create_fixture(data)
    else:
        response = {"status": "error", "message": "Unknown action"}

    return response

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3000))
server_socket.listen(1)

print("Server is listening on localhost:3000")

while True:
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from", client_address)
    request = client_socket.recv(1024)

    response = handle_request(request)
    response_message = json.dumps(response).encode()
    client_socket.sendall(response_message)

    client_socket.close()
