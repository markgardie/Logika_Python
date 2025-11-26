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
    #TODO ui.message_entry.delete()

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

def handle_code(line):
    if not line:
        return
    parts = line.split("@", 3)
    msg_type = parts[0]

    if msg_type == "TEXT":
        if len(parts) >= 3:
            author = parts[1]
            message = parts[2]

            #TODO ui.add_message(author + message)
    elif msg_type == "IMAGE":
        if len(parts) >= 4:
            author = parts[1]
            filename = parts[2]

            #TODO ui.add_message(author + filename) + image parser
    else:
        pass
        #TODO ui.add_message(line)

def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    t = threading.Thread(target=recv_message, daemon=True)
    t.run()

