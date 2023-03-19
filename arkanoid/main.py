from constants import*
from Sprite import*
from Window import*
from Platform import*
from functions import*
from Ball import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)
ball = Ball(BALL_WIDTH, BALL_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT, BALL_IMAGE_PATH)
platform = Platform(PLATFORM_WIDTH, 
                    PLATFORM_HEIGHT, 
                    WINDOW_WIDTH / 2, 
                    WINDOW_HEIGHT - 30, 
                    PLATFORM_IMAGE_PATH)

