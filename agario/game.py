from window import Window
from player import Player
from image_sprite import Image_Sprite
from food import Food

from random import randint
import pygame

class Game():

    def __init__(self):
        self.foods = []
        self.players = []

    def create_food(self, amount):
        for i in range(amount):
            x = randint(20, WINDOW_WIDTH - 20)
            y = randint(20, WINDOW_HEIGHT - 20)
            food = Food(x, y, FOOD_RADIUS, FOOD_COLOR)
            self.foods.append(food)

    def create_players(self, amount):
        for i in range(amount):
            x = randint(20, WINDOW_WIDTH - 20)
            y = randint(20, WINDOW_HEIGHT - 20)
            player = Player(x, y, WIDTH_PLAYER, HEIGHT_PLAYER, PLAYER_IMAGE_PATH)
            self.players.append(player)


    def create_objects(self):
        self.create_food(100)
        self.create_players(2)
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BG_IMAGE_PATH, FPS)

    def draw_foods(self):
        for food in self.foods:
            food.draw(self.window.surface)

    def draw_players(self):
        for player in self.players:
            player.draw(self.window.surface)
    
    def draw_objects(self):
        self.window.draw()
        self.draw_foods()
        self.draw_players()

    def move_objects(self):
        for player in self.players:
            player.controls(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

    def collisions(self):
        pass

    def win_lose(self):
        pass

    def gameloop(self):
        pass
