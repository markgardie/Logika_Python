import os


WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 30
PLATFORM_WIDTH = 150
PLATFORM_HEIGHT = 30
BALL_WIDTH = 30
BALL_HEIGHT = 30
BLUE = (200, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 60
PROJECT_PATH = os.path.abspath(__file__ + "/..")
IMAGES_PATH = os.path.join(PROJECT_PATH, "images")

BLOCK_IMAGE_PATH = os.path.join(IMAGES_PATH, "block.png")

ICON_PATH = os.path.join(IMAGES_PATH, "icon.png")
FONT_PATH = os.path.join(PROJECT_PATH, "fonts/font.ttf")
PLATFORM_SPEED = 10
BALL_SPEED = 5
MAP = ["1111111111",
        "0001111000",
        "1111111111",
        "0001111000"]


