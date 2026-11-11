# game.py

import pygame
from pygame import K_w, K_s, K_a, K_d, QUIT
from window import Window
from player import Player
from food import Food
from network import Network
from constants import *


class Game:

    # dz
    def __init__(self):
        pass

    #dz
    def create_foods(self):
        """Створює їжу на карті"""
        pass
    
    def connect_to_server(self):
        """Підключається до сервера і створює свого гравця"""
        player_data = self.network.connect()

        if player_data is None:
            print("Не вдалося підключитись до сервера")
            return  False

        x, y, radius = player_data
        self.my_player = Player(
            self.network.my_id, 
            x, y, radius, True
            )

        self.network.start_receiving()
        return True
    
    def calculate_scale(self):
        """Розраховує масштаб камери залежно від розміру гравця"""
        scale = SCALE_FACTOR / self.my_player.radius
        return max(SCALE_MIN, min(scale, SCALE_MAX))
    
    def update_other_players(self):
        """Оновлює список інших гравців з даних сервера"""
        pass
    
    def handle_food_collisions(self):
        """Обробляє колізії з їжею"""
        foods_to_remove = []
        
        for food in self.foods:
            if food.check_collision(self.my_player.x, self.my_player.y, self.my_player.radius):
                foods_to_remove.append(food)
                growth = int(food.radius * FOOD_GROWTH_RATE)
                self.my_player.grow(growth)
        
        for food in foods_to_remove:
            self.foods.remove(food)

    #dz
    def draw_other_players(self, scale):
        """Малює інших гравців"""
        pass

    #dz
    def draw_my_player(self, scale):
        """Малює свого гравця (завжди в центрі екрану)"""
        pass

    #dz
    def draw_foods(self, scale):
        """Малює їжу"""
        pass

    #dz
    def draw_lose_message(self):
        """Малює повідомлення про програш"""
        pass

    #dz
    def handle_events(self):
        """Обробляє події pygame"""
        pass
    
    def handle_controls(self):
        """Обробляє управління гравцем"""
        pass
    
    def send_player_state(self):
        """Відправляє стан гравця на сервер"""
        pass
    
    def gameloop(self):
        """Основний ігровий цикл"""
        # Підключення до сервера
        if not self.connect_to_server():
            return
        
        # Створення їжі
        self.create_foods()
        
        self.running = True
        
        while self.running:
            pass
        
        # Відключення від сервера
        self.network.disconnect()
        pygame.quit()