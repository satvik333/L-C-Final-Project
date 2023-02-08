import socket
import json

# CommunicationProtocol Class
class CommunicationProtocol:
    def __init__(self):
        self.size = 0
        self.protocol_version = ""
        self.protocol_format = ""
        self.protocol_type = ""
        self.source_ip = ""
        self.source_port = 0
        self.dest_ip = ""
        self.dest_port = 0
        self.headers = {}

# ISCRequest Class
class ISCRequest(CommunicationProtocol):
    def __init__(self):
        super().__init__()
        self.protocol_type = "request"
        self.headers["method"] = ""

# ICSResponse Class
class ICSResponse(CommunicationProtocol):
    def __init__(self):
        super().__init__()
        self.protocol_type = "response"
        self.headers["status"] = ""
        self.headers["error-code"] = ""
        self.headers["error-message"] = ""

    def get_error_message(self):
        return self.headers["error-message"]
    
    def set_error_message(self, message):
        self.headers["error-message"] = message

# DataSerializer Class
class DataSerializer:
    def serialize(self, protocol):
        raise NotImplementedError

    def deserialize(self, data):
        raise NotImplementedError

# JSONSerializer Class
class JSONSerializer(DataSerializer):
    def serialize(self, protocol):
        return json.dumps(protocol.__dict__).encode()

    def deserialize(self, data):
        data_dict = json.loads(data.decode())
        if data_dict["protocol_type"] == "request":
            protocol = ISCRequest()
        else:
            protocol = ICSResponse()
        protocol.__dict__ = data_dict
        return protocol

# DataSerializerFactory Class
class DataSerializerFactory:
    @staticmethod
    def get_serializer(protocol_format):
        if protocol_format.lower() == "json":
            return JSONSerializer()
        else:
            raise ValueError("Invalid DataSerializer Format")

# Client
class Client:
    def __init__(self, host, port, serializer):
        self.host = host
        self.port = port
        self.serializer = serializer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, protocol):
        data = self.serializer.serialize(protocol)
        self.socket.sendall(data)

    def receive(self):
        data = self.socket.recv(1024)
        return self.serializer.deserialize(data)

    def close(self):
        self.socket.close()

# Server
class Server:
    def __init__(self, host, port, serializer):
        self.host = host
        self.port = port
        self
