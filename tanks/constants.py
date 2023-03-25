import os 

WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600

TANK_WIDTH = 40
TANK_HEIGHT = 40

PLAYER_SPEED = 10
ENEMY_SPEED = 5
BULLET_SPEED = 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PROJECT_PATH = os.path.abspath(__file__ + "/..")
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")
TANK1_IMAGE_PATH = os.path.join(RESOURCES_PATH, "tank1.jpg")
TANK2_IMAGE_PATH = os.path.join(RESOURCES_PATH, "tank2.jpg")
ENEMY_IMAGE_PATH = os.path.join(RESOURCES_PATH, "enemy.jpg")
BULLET_IMAGE_PATH = os.path.join(RESOURCES_PATH, "bullet.jpg")

FPS = 60