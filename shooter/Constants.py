import os
import pygame as pg

pg.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80
PLAYER_SPEED = 5

PLAYER_X = WINDOW_WIDTH / 2
PLAYER_Y = WINDOW_HEIGHT - 80

ENEMY_WIDTH = 80
ENEMY_HEGHT = 50
ENEMY_Y = -40
# крайня ліва точка для спавну ворогів
ENEMY_X_START = 80
# крайня права точка для спавну ворогів
ENEMY_X_END = WINDOW_WIDTH - ENEMY_X_START

BULLET_SPEED = 15
BULLET_WIDTH = 15
BULLET_HEIGHT = 20

# шлях до папки з проектом
PROJECT_PATH = os.path.abspath(__file__ + "/..")
# шлях до папки з ресурсами: зображення, звуки
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")

# шлях до зображення фона
BACKGROUND_IMAGE_PATH = os.path.join(RESOURCES_PATH, "galaxy.jpg")
# шлях до зображення гравця
PLAYER_IMAGE_PATH = os.path.join(RESOURCES_PATH, "rocket.png")
# шлях до зображення ворога
ENEMY_IMAGE_PATH = os.path.join(RESOURCES_PATH, "ufo.png")
# шлях до зображення кулі
BULLET_IMAGE_PATH = os.path.join(RESOURCES_PATH, "bullet.png")
# шлях до фонового звуку
BACKGROUND_SOUND_PATH = os.path.join(RESOURCES_PATH, "space.ogg")
# шлях до звуку пострілу
FIRE_SOUND_PATH = os.path.join(RESOURCES_PATH, "fire.ogg")

CAPTION = 'SHOOTER'

FPS = 60

ENEMY_NUMBER = 5

# шрифт-заготовка
FONT = pg.font.Font(None, 36)

MISS_TEXT = "Пропущено:"
SCORES_TEXT = "Рахунок:"
WIN_TEXT = "Перемога"
LOSE_TEXT = "Поразка"
# чорний колір
BLACK = (255, 255, 255)

# координати лічильника пропущених ворогів
MISS_TEXT_COR = (10, 50)

# координати лічильника балів
SCORES_TEXT_COR = (10, 20)

# скільки треба попасти
GOAL = 5
# скільки пропусків до програшу
MAX_MISS = 7

# звук фону
BACKGROUND_SOUND = pg.mixer.Sound(BACKGROUND_SOUND_PATH)
# звук пострілу
FIRE_SOUND = pg.mixer.Sound(FIRE_SOUND_PATH)