from constants import*
from functions import*
from Ball import*
from Platform import*
from Window import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

ball = Ball(BALL_WIDTH, BALL_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, BALL_PATH, BALL_SPEED)

platform1 = Platform(PLATFORM_WIDTH, 
                     PLATFORM_HEIGHT, 
                     PLATFORM_1_X, 
                     PLATFORM_1_Y, 
                     PLATFORM_PATH, 
                     PLATFORM_SPEED)


platform2 = Platform(PLATFORM_WIDTH, 
                     PLATFORM_HEIGHT, 
                     PLATFORM_2_X, 
                     PLATFORM_2_Y, 
                     PLATFORM_PATH, 
                     PLATFORM_SPEED)


game = True
finish = False
text = ""


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    

    