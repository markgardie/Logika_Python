# server.py
import socket
import threading

HOST = '0.0.0.0'  # слухає всі інтерфейси
PORT = 8080

clients_lock = threading.Lock()
clients = []  # список клієнтських сокетів

def broadcast(data: bytes, exclude_socket=None):
    """Надсилає байти всім клієнтам, крім exclude_socket."""
    with clients_lock:
        for client in list(clients):
            if client is exclude_socket:
                continue
            try:
                client.sendall(data)
            except Exception:
                # при помилці закриваємо і прибираємо клієнта
                try:
                    client.shutdown(socket.SHUT_RDWR)
                except Exception:
                    pass
                try:
                    client.close()
                except Exception:
                    pass
                if client in clients:
                    clients.remove(client)

def handle_client(client_socket: socket.socket, addr):
    """Обробка одного клієнта: ретрансляція отриманих даних іншим."""
    try:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            # Проста валідація: переконаємось, що дані закінчуються '\n' або містять
            # хоча б один повний рядок; ми просто ретрансльовуємо як є.
            broadcast(data, exclude_socket=client_socket)
    except Exception:
        pass
    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        try:
            client_socket.close()
        except Exception:
            pass
        print(f"Клієнт {addr} відключився")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print(f"Сервер запущено на {HOST}:{PORT}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Підключився клієнт: {addr}")
            with clients_lock:
                clients.append(client_socket)
            t = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("Зупинка сервера...")
    finally:
        with clients_lock:
            for c in clients:
                try:
                    c.shutdown(socket.SHUT_RDWR)
                except Exception:
                    pass
                try:
                    c.close()
                except Exception:
                    pass
            clients.clear()
        try:
            server_socket.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
