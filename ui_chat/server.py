import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

clients = []

def broadcast():
    pass

def handle_clients():
    pass

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущено на {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Підключився клієнт: {addr}")
        clients.append(client_socket)

        t = threading.Thread(target=handle_clients, args = (client_socket,))
        t.start()

if __name__ == "__main__":
    main()