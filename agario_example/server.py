# server.py

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time


class GameServer:
    
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.socket.setblocking(False)
        
        self.players = {}  # {conn: {'id': int, 'x': int, 'y': int, 'r': int}}
        self.conn_ids = {}  # {conn: id}
        self.id_counter = 0
        self.running = False
    
    def accept_connections(self):
        """Приймає нові підключення від клієнтів"""
        while self.running:
            try:
                conn, addr = self.socket.accept()
                conn.setblocking(False)
                
                self.id_counter += 1
                player_id = self.id_counter
                
                # Створюємо нового гравця
                self.players[conn] = {
                    'id': player_id,
                    'x': 0,
                    'y': 0,
                    'r': 20
                }
                self.conn_ids[conn] = player_id
                
                # Відправляємо початкові дані клієнту
                initial_data = f"{player_id},0,0,20"
                conn.send(initial_data.encode())
                
                print(f"Гравець {player_id} підключився з {addr}")
            except:
                pass
            
            time.sleep(0.01)
    
    def receive_player_data(self):
        """Отримує дані від всіх клієнтів"""
        player_data = {}
        
        for conn in list(self.players.keys()):
            try:
                data = conn.recv(64).decode().strip()
                
                if ',' in data:
                    parts = data.split(',')
                    if len(parts) == 4:
                        pid, x, y, r = map(int, parts)
                        self.players[conn] = {'id': pid, 'x': x, 'y': y, 'r': r}
                        player_data[conn] = self.players[conn]
            except:
                continue
        
        return player_data
    
    def check_player_collisions(self, player_data):
        """Перевіряє колізії між гравцями"""
        eliminated = []
        
        for conn1 in player_data:
            if conn1 in eliminated:
                continue
            
            p1 = player_data[conn1]
            
            for conn2 in player_data:
                if conn1 == conn2 or conn2 in eliminated:
                    continue
                
                p2 = player_data[conn2]
                
                # Розрахунок відстані
                dx = p1['x'] - p2['x']
                dy = p1['y'] - p2['y']
                distance = (dx**2 + dy**2)**0.5
                
                # Перевірка колізії (більший гравець з'їдає меншого)
                if distance < p1['r'] + p2['r'] and p1['r'] > p2['r'] * 1.1:
                    # p1 з'їв p2
                    p1['r'] += int(p2['r'] * 0.5)
                    self.players[conn1] = p1
                    eliminated.append(conn2)
        
        return eliminated
    
    def send_data_to_clients(self, eliminated):
        """Відправляє дані всім клієнтам"""
        to_remove = []
        
        for conn in list(self.players.keys()):
            # Повідомляємо елімінованих гравців
            if conn in eliminated:
                try:
                    conn.send("LOSE".encode())
                except:
                    pass
                to_remove.append(conn)
                continue
            
            # Відправляємо дані інших гравців
            try:
                # Формуємо пакет з даними всіх інших гравців
                other_players = [
                    f"{p['id']},{p['x']},{p['y']},{p['r']}"
                    for c, p in self.players.items()
                    if c != conn and c not in eliminated
                ]
                
                packet = '|'.join(other_players) + '|'
                conn.send(packet.encode())
            except:
                to_remove.append(conn)
        
        # Видаляємо відключених гравців
        for conn in to_remove:
            player_id = self.conn_ids.get(conn, 'Unknown')
            self.players.pop(conn, None)
            self.conn_ids.pop(conn, None)
            print(f"Гравець {player_id} відключився")
    
    def game_loop(self):
        """Основний ігровий цикл сервера"""
        while self.running:
            time.sleep(0.01)
            
            # Отримуємо дані від клієнтів
            player_data = self.receive_player_data()
            
            # Перевіряємо колізії
            eliminated = self.check_player_collisions(player_data)
            
            # Відправляємо дані клієнтам
            self.send_data_to_clients(eliminated)
    
    def start(self):
        """Запускає сервер"""
        self.running = True
        
        # Запускаємо потік для прийняття підключень
        accept_thread = Thread(target=self.accept_connections, daemon=True)
        accept_thread.start()
        
        # Запускаємо потік для ігрової логіки
        game_thread = Thread(target=self.game_loop, daemon=True)
        game_thread.start()
        
        print(f"Сервер запущено на {self.host}:{self.port}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nЗупинка сервера...")
            self.running = False


if __name__ == "__main__":
    server = GameServer()
    server.start()