import base64
import io
import threading
from socket import socket, AF_INET, SOCK_STREAM
from PIL import Image
from server import HOST, PORT

def send_message(client_socket, message, username):
    if message:
        data = f"TEXT@{username}@{message}"
        try:
            client_socket.sendall(data)
        except:
            pass

def recv_message(client_socket):
    buffer = ""
    while True:
        try:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            buffer += chunk.decode("utf-8", errors="ignore")

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                handle_code(line.strip())
        except:
            break

    client_socket.close()

def handle_code():
    pass

def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    t = threading.Thread(target=recv_message, daemon=True)
    t.run()

