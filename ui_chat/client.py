# client.py
import socket
import threading
import traceback

HOST = "127.0.0.1"
PORT = 8080

ENC = "utf-8"
LINE_DELIM = "\n"

class ChatClient:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.sock = None
        self.recv_thread = None
        self.running = False

    def connect(self) -> bool:
        """Підключається до сервера. Повертає True при успіху."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self.running = True
            return True
        except Exception:
            traceback.print_exc()
            self.running = False
            self.sock = None
            return False

    def start_receiving(self, on_message_callback):
        """
        Починає потік, який читає з сокета.
        on_message_callback приймає два аргументи: author (str), message (str).
        """
        if not self.sock:
            raise RuntimeError("Socket не підключений")

        def _recv_loop():
            buffer = ""
            try:
                while self.running:
                    chunk = self.sock.recv(4096)
                    if not chunk:
                        break
                    try:
                        buffer += chunk.decode(ENC, errors="ignore")
                    except Exception:
                        # у рідкісних випадках декодування може падати
                        buffer += chunk.decode(ENC, errors="replace")

                    while LINE_DELIM in buffer:
                        line, buffer = buffer.split(LINE_DELIM, 1)
                        line = line.strip()
                        if not line:
                            continue
                        # Очікуємо формат: TEXT@username@message
                        parts = line.split("@", 2)
                        if len(parts) >= 3 and parts[0] == "TEXT":
                            author = parts[1]
                            message = parts[2]
                            try:
                                on_message_callback(author, message)
                            except Exception:
                                # колбек на UI може падати; лог
                                traceback.print_exc()
                        else:
                            # якщо формат незрозумілий — надсилаємо як повідомлення від сервера
                            try:
                                on_message_callback("SERVER", line)
                            except Exception:
                                traceback.print_exc()
            except Exception:
                traceback.print_exc()
            finally:
                self.running = False
                try:
                    self.sock.shutdown(socket.SHUT_RDWR)
                except Exception:
                    pass
                try:
                    self.sock.close()
                except Exception:
                    pass

        self.recv_thread = threading.Thread(target=_recv_loop, daemon=True)
        self.recv_thread.start()

    def send_text(self, username: str, message: str):
        """Надсилає текстове повідомлення у форматі протоколу."""
        if not self.sock or not self.running:
            raise RuntimeError("Не підключено до сервера")
        if not message:
            return
        # Формуємо пакет і відправляємо байти з '\n' як роздільником
        payload = f"TEXT@{username}@{message}{LINE_DELIM}".encode(ENC)
        try:
            self.sock.sendall(payload)
        except Exception:
            # при помилці відключаємось
            self.running = False
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
            try:
                self.sock.close()
            except Exception:
                pass

    def close(self):
        """Граціозне завершення."""
        self.running = False
        try:
            if self.sock:
                self.sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
