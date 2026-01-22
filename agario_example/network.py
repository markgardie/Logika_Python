# network.py

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from constants import SERVER_HOST, SERVER_PORT, BUFFER_SIZE


class Network:
    
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.connected = False
        self.my_id = None
        self.all_players_data = []
        self.is_lost = False
        self.receiving = False
    
    def connect(self):
        """Підключається до сервера і отримує початкові дані"""
        try:
            self.socket.connect((SERVER_HOST, SERVER_PORT))
            self.connected = True
            
            # Отримуємо початкові дані: ID, x, y, radius
            initial_data = self.socket.recv(64).decode().strip().split(',')
            self.my_id = int(initial_data[0])
            player_data = list(map(int, initial_data[1:]))
            
            self.socket.setblocking(False)
            return player_data  # [x, y, radius]
        except Exception as e:
            print(f"Помилка підключення: {e}")
            self.connected = False
            return None
    
    def start_receiving(self):
        """Запускає потік для отримання даних від сервера"""
        if not self.connected:
            return
        
        self.receiving = True
        thread = Thread(target=self._receive_data, daemon=True)
        thread.start()
    
    def _receive_data(self):
        """Отримує дані від сервера в окремому потоці"""
        while self.receiving:
            try:
                data = self.socket.recv(BUFFER_SIZE).decode().strip()
                
                if data == "LOSE":
                    self.is_lost = True
                elif data:
                    # Парсимо дані всіх гравців: "id,x,y,r|id,x,y,r|"
                    parts = data.strip('|').split('|')
                    self.all_players_data = [
                        list(map(int, p.split(','))) 
                        for p in parts 
                        if len(p.split(',')) == 4
                    ]
            except:
                pass
    
    def send_player_data(self, player_data_string):
        """Відправляє дані гравця на сервер"""
        if not self.connected:
            return
        
        try:
            self.socket.send(player_data_string.encode())
        except:
            pass
    
    def get_other_players(self):
        """Повертає дані всіх інших гравців"""
        return self.all_players_data
    
    def check_lose(self):
        """Перевіряє, чи гравець програв"""
        return self.is_lost
    
    def disconnect(self):
        """Закриває з'єднання"""
        self.receiving = False
        if self.connected:
            try:
                self.socket.close()
            except:
                pass
        self.connected = False