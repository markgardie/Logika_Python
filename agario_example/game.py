# game.py

import pygame
from pygame import K_w, K_s, K_a, K_d, QUIT
from window import Window
from player import Player
from food import Food
from network import Network
from constants import *


class Game:
    
    def __init__(self):
        pygame.init()
        self.window = Window()
        self.network = Network()
        self.font = pygame.font.Font(None, FONT_SIZE)
        
        self.my_player = None
        self.other_players = []
        self.foods = []
        self.running = False
    
    def create_foods(self):
        """Створює їжу на карті"""
        for _ in range(FOOD_COUNT):
            food = Food.generate_random()
            self.foods.append(food)
    
    def connect_to_server(self):
        """Підключається до сервера і створює свого гравця"""
        player_data = self.network.connect()
        
        if player_data is None:
            print("Не вдалося підключитись до сервера!")
            return False
        
        # Створюємо свого гравця
        x, y, radius = player_data
        self.my_player = Player(self.network.my_id, x, y, radius, is_self=True)
        
        # Запускаємо отримання даних від сервера
        self.network.start_receiving()
        
        return True
    
    def calculate_scale(self):
        """Розраховує масштаб камери залежно від розміру гравця"""
        scale = SCALE_FACTOR / self.my_player.radius
        return max(SCALE_MIN, min(scale, SCALE_MAX))
    
    def update_other_players(self):
        """Оновлює список інших гравців з даних сервера"""
        players_data = self.network.get_other_players()
        self.other_players.clear()
        
        for data in players_data:
            if len(data) == 4:
                player_id, x, y, radius = data
                if player_id != self.network.my_id:
                    player = Player(player_id, x, y, radius, is_self=False)
                    self.other_players.append(player)
    
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
    
    def draw_other_players(self, scale):
        """Малює інших гравців"""
        for player in self.other_players:
            player.draw(self.window.surface, self.my_player.x, self.my_player.y, scale)
    
    def draw_my_player(self, scale):
        """Малює свого гравця (завжди в центрі екрану)"""
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2
        scaled_radius = int(self.my_player.radius * scale)
        
        pygame.draw.circle(
            self.window.surface, 
            self.my_player.color, 
            (center_x, center_y), 
            scaled_radius
        )
    
    def draw_foods(self, scale):
        """Малює їжу"""
        for food in self.foods:
            food.draw(self.window.surface, self.my_player.x, self.my_player.y, scale)
    
    def draw_lose_message(self):
        """Малює повідомлення про програш"""
        text = self.font.render(LOSE_TEXT, True, LOSE_TEXT_COLOR)
        self.window.surface.blit(text, LOSE_TEXT_POS)
    
    def handle_events(self):
        """Обробляє події pygame"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    
    def handle_controls(self):
        """Обробляє управління гравцем"""
        if not self.network.check_lose():
            self.my_player.controls(K_w, K_s, K_a, K_d)
    
    def send_player_state(self):
        """Відправляє стан гравця на сервер"""
        if not self.network.check_lose():
            data_string = self.my_player.get_data_string()
            self.network.send_player_data(data_string)
    
    def gameloop(self):
        """Основний ігровий цикл"""
        # Підключення до сервера
        if not self.connect_to_server():
            return
        
        # Створення їжі
        self.create_foods()
        
        self.running = True
        
        while self.running:
            # Обробка подій
            self.handle_events()
            
            # Очищення екрану
            self.window.fill()
            
            # Оновлення даних
            self.update_other_players()
            scale = self.calculate_scale()
            
            # Малювання
            self.draw_other_players(scale)
            self.draw_my_player(scale)
            self.draw_foods(scale)
            
            # Перевірка програшу
            if self.network.check_lose():
                self.draw_lose_message()
            else:
                # Управління та колізії тільки якщо не програли
                self.handle_controls()
                self.handle_food_collisions()
                self.send_player_state()
            
            # Оновлення екрану
            self.window.update()
        
        # Відключення від сервера
        self.network.disconnect()
        pygame.quit()