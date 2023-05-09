import os
from random import randint

# розміри вікна
WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600

# розміри змійки
SNAKE_WIDTH = 50
SNAKE_HEIGHT = 50

# розміри їжі
FOOD_WIDTH = 50
FOOD_HEIGHT = 50

# початкові координати змійки
# напочатку гри з'являється посередині
# тому ми ділимо розміри вікна на 2
SNAKE_X = WINDOW_WIDTH / 2 - SNAKE_WIDTH / 2
SNAKE_Y = WINDOW_HEIGHT / 2 - SNAKE_HEIGHT / 2

# початкові координати їжі будуть випадкові
FOOD_X = randint(10, WINDOW_WIDTH - 10)
FOOD_Y = randint(10, WINDOW_HEIGHT - 10)

# швидкості
SNAKE_SPEED = 5
FOOD_SPEED = 0

# кольори
BLUE = (200, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 190, 0)
RED = (190, 0, 0)

# шлях до папки з проектом
PROJECT_PATH = os.path.abspath(__file__ + "/..")
# шлях до папки із зображеннями
IMAGES_PATH = os.path.join(PROJECT_PATH, "images")

# шляхи до зображень спрайтів
SNAKE_IMAGE = os.path.join(IMAGES_PATH, "snake.png")
FOOD_IMAGE = os.path.join(IMAGES_PATH, "food.png")

# надпис вікна
CAPTION = "Snake"

# скільки треба з'їсти їжі
WIN_SCORE = 5
# фінальні тексти
WIN_TEXT = "Перемога"
LOSE_TEXT = "Поразка"

FPS = 60

# бали
# напочатку 0 балів
scores = [0]