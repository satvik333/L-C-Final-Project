import socket
import json

def perform_action(action, input_file, output_file):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 3000)
    client_socket.connect(server_address)

    with open(input_file, "r") as f:
        data = json.load(f)

    data["action"] = action

    message = json.dumps(data).encode()

    client_socket.sendall(message)

    data = client_socket.recv(1024)

    client_socket.close()

    response = json.loads(data.decode())
    with open(output_file, "w") as f:
        json.dump(response, f)

    print('Received:', response)

perform_action("create_team", "C:/Users/satvik.ms/Desktop/L-C-Final-Project/FixtureInput.json", "C:/Users/satvik.ms/Desktop/L-C-Final-Project/teams-response.json")

perform_action("create_fixture", "C:/Users/satvik.ms/Desktop/L-C-Final-Project/TeamsInput.json", "C:/Users/satvik.ms/Desktop/L-C-Final-Project/fixtures-response.json")
