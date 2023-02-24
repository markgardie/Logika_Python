
import os
import pygame as pg

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80
PLAYER_SPEED = 5

ENEMY_WIDTH = 80
ENEMY_HEGHT = 50
ENEMY_Y = -40

PROJECT_PATH = os.path.abspath(__file__ + "/..")
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")

BACKGROUND_IMAGE_PATH = os.path.join(RESOURCES_PATH, "galaxy.jpg")
PLAYER_IMAGE_PATH = os.path.join(RESOURCES_PATH, "rocket.png")
ENEMY_IMAGE_PATH = os.path.join(RESOURCES_PATH, "ufo.png")

CAPTION = 'SHOOTER'

FPS = 60

ENEMY_NUMBER = 5

FONT = pg.font.Font(None, 36)

MISS_TEXT = "Пропущено:"
SCORES_TEXT = "Рахунок:"
TEXT_COLOR = (255, 255, 255)

MISS_TEXT_COR = (10, 50)

SCORES_TEXT_COR = (10, 20)

scores = [0]
miss = [0]
