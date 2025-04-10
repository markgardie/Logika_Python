import os


WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 30
PLATFORM_WIDTH = 150
PLATFORM_HEIGHT = 70
BALL_WIDTH = 30
BALL_HEIGHT = 30
BLUE = (200, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 60


PROJECT_PATH = os.path.abspath(__file__ + "/..")
IMAGES_PATH = os.path.join(PROJECT_PATH, "images")

BLOCK_IMAGE_PATH = os.path.join(IMAGES_PATH, "block.png")
BALL_IMAGE_PATH = os.path.join(IMAGES_PATH, "ball.png")
PLATFORM_IMAGE_PATH = os.path.join(IMAGES_PATH, "platform.png")

MAP = ["1111111111",
        "0001111000",
        "1111111111",
        "0001111000",
        ]

CAPTION = "Arkanoid"
WIN_TEXT = "Перемога"
LOSE_TEXT =  "Поразка"