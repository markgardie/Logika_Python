
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (255, 255, 255)

BLACK = (0, 0, 0)

CELL_WIDTH = 100
CELL_HEIGHT = 100

FIRST_CELL_X = 180
FIRST_CELL_Y = 130

X_STEP = CELL_WIDTH + 20
Y_STEP = CELL_HEIGHT + 20

PROJECT_PATH = os.path.abspath(__file__ + "/..")
RESOURCES_PATH = os.path.join(PROJECT_PATH, "resources")

START_IMAGE_PATH = os.path.join(RESOURCES_PATH, "start.png")
CROSS_IMAGE_PATH = os.path.join(RESOURCES_PATH, "cross.png")
ZERO_IMAGE_PATH = os.path.join(RESOURCES_PATH, "zero.png")

CAPTION = 'Tit-tac-toe'

FPS = 60

FONT_SIZE = 60


