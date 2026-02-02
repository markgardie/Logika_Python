
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

class GameServer():

    def __init__(self, host = 'localhost', port = 8080):
        self.host = host
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(host, port)
        self.socket.listen(5)
        self.socket.setblocking(False)

        self.players = {}
        self.conn_ids = {}
        self.id_counter = 0
        self.running = False


    def accept_connections(self):
        while self.running:
            try:
                conn, addr = self.socket.accept()
                conn.setblocking(False)

                self.id_counter += 1
                player_id = self.id_counter

                new_player = {
                    "id": player_id,
                    "x": 0,
                    "y": 0,
                    "r": 20,
                }
                self.players[conn] = new_player
                self.conn_ids[conn] = player_id

                initial_data = f"{player_id},0,0,20"
                self.socket.send(initial_data.encode())
                print(f"Гравець {player_id} підключився з {addr}")
            
            except:
                pass

            time.sleep(0.01)

    def receive_player_data(self):
        player_data = {}
        
        for conn in list(self.players.keys()):
            try:
                data = conn.recv(64).decode.strip()
                if "," in data:
                    parts = data.split(",")
                    if len(parts) == 4:
                        pid, x, y, r = map(int, parts)
                        self.players[conn] = {
                            "id": pid,
                            "x": x,
                            "y": y,
                            "r": r
                        }
                        player_data[conn] = self.players[conn]
            except:
                continue

        return player_data

    def send_data_to_clients(self):
        pass

    def check_players_collisions(self):
        pass

    def start(self):
        pass

    def gameloop(self):
        pass