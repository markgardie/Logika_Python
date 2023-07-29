import pygame as pg
from random import randint

# запускається модуль зі шрифтами
pg.font.init()

BLACK = (0, 0, 0)
PURPLE = (164, 0, 163)
WHITE = (255, 255, 255)

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
BUTTON_WIDTH = 290
BUTTON_HEIGHT = 70

BUTTON_X = 120
BUTTON1_Y = 100
BUTTON2_Y = 240

SHIFT_X = 10
SHIFT_Y = 10

QUESTION_TITLES = ["Питання", "Франції", "Програмування"]
ANS_TITLES = ["Відповідь", "Париж", "Python"]
CAPTION = "Question-Answer"
FONT = None
TEXT_SIZE = 60

FPS = 60

class Window():
    
    def __init__(self, width, heigth, caption, bg_color):

        size = (width, heigth)

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)

        self.screen.fill(bg_color)

        self.clock = pg.time.Clock()

class Button():

    def __init__(self, width, height, x, y, color, text, text_size, font, text_color):

        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color

        self.font = pg.font.Font(font, text_size)
        self.text = self.font.render(text, True, text_color)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

        x = self.rect.x + SHIFT_X
        y = self.rect.y + SHIFT_Y

        screen.blit(self.text, (x, y))

    def set_text(self, text):
        self.text = self.font.render(text, True, self.text_color)

class Game():

    def __init__(self):
        self.create_objects()
        self.draw_objects()
        self.game_loop()

    def create_objects(self):
        self.window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, WHITE)

        self.question_button = Button(
            BUTTON_WIDTH, BUTTON_HEIGHT,
            BUTTON_X, BUTTON1_Y,
            PURPLE,
            QUESTION_TITLES[0], TEXT_SIZE, FONT, BLACK
        )


        self.answer_button = Button(
            BUTTON_WIDTH, BUTTON_HEIGHT,
            BUTTON_X, BUTTON2_Y,
            PURPLE,
            ANS_TITLES[0], TEXT_SIZE, FONT, BLACK
        )

    def draw_objects(self):
        self.question_button.draw(self.window.screen)
        self.answer_button.draw(self.window.screen)

    def event_listener(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game = False
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                num = randint(0, len(QUESTION_TITLES) - 1)
                text = QUESTION_TITLES[num]
                self.question_button.set_text(text)

            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                num = randint(0, len(QUESTION_TITLES) - 1)
                text = ANS_TITLES[num]
                self.answer_button.set_text(text)
        

    def update_window(self):
        self.window.clock.tick(FPS)
        pg.display.flip()

    def game_loop(self):
        self.game = True
        
        while self.game:
            self.event_listener()
            self.draw_objects()
            self.update_window()


game = Game()
