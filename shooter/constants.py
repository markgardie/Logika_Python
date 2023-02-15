
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80
PLAYER_SPEED = 5


PROJECT_PATH = os.path.abspath(__file__ + "/..")
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")

BACKGROUND_IMAGE_PATH = os.path.join(RESOURCES_PATH, "galaxy.jpg")
PLAYER_IMAGE_PATH = os.path.join(RESOURCES_PATH, "rocket.png")

CAPTION = 'SHOOTER'

FPS = 60
