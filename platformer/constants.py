import os

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

PLATFORM_WIDTH = 150
PLATFORM_HEIGHT = 30

COIN_WIDTH = 30
COIN_HEIGHT = 30

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10

BLUE = (6, 87, 180)
BLACK = (0, 0, 0)

PROJECT_PATH = os.path.abspath(__file__ + "/..")
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")
PLATFORM_IMAGE_PATH = os.path.join(RESOURCES_PATH, "platform.jpg")
COIN_IMAGE_PATH = os.path.join(RESOURCES_PATH, "coin.jpg")
PLAYER_IMAGE_PATH = os.path.join(RESOURCES_PATH, "player.jpg")

CAPTION = "Platformer"