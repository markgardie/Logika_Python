# main.py
from client import ChatClient
from ui import MainWindow
import sys
import time

def run_client_app(host=None, port=None, default_name="User"):
    client = ChatClient()
    success = client.connect()
    if not success:
        print("Не вдалося підключитись до сервера.")
        return

    # створюємо UI і прив'язуємо callback для вхідних повідомлень
    app = MainWindow(client, default_username=default_name)

    # передаємо callback, який UI забезпечує безпечне оновлення
    client.start_receiving(app.on_incoming_message)

    # запускаємо UI головним потоком
    app.mainloop()

if __name__ == "__main__":
    # дозволяємо опційно передати ім'я через аргументи командного рядка
    default_name = "User"
    if len(sys.argv) >= 2:
        default_name = sys.argv[1]
    run_client_app(default_name=default_name)
