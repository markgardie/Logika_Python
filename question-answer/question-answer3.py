from turtle import width
import pygame
from random import randint
pygame.init()

#--------Constants
BLACK = (0, 0, 0)
PURPLE = (164, 0, 163)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

#--------Create and configure window
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Question and Answer Game")
window.fill(WHITE)
fps = pygame.time.Clock()    


#--------Button class
class Button():

    def __init__(self, x, y, width, heigth, bgcolor):
        self.rect = pygame.Rect(x, y, width, heigth)
        self.bgcolor = bgcolor
        
    def set_text(self, text, text_color, font_size, font):
        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        pygame.draw.rect(window, self.bgcolor, self.rect)
        window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))

#--------Create buttons
quest_button = Button(120,100,290,70, PURPLE)
ans_button = Button(120,240,290,70, PURPLE)

#Set buttons` start text
quest_button.set_text("Питання", WHITE, 75, None)
ans_button.set_text("Відповідь", WHITE, 75, None)

#Draw Buttons` start text
quest_button.draw(10, 10)
ans_button.draw(10, 10)

#--------Game cycle
game = True

while game:

    #Udpate window
    fps.tick(60)
    pygame.display.flip()

    #Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint (1,3)
                if num == 1:
                    quest_button.set_text('Що вивчаєш в Логіці?', WHITE, 25, None)
                if num ==2:
                    quest_button.set_text('Якою мовою говорять у Франції?', WHITE, 25, None)
                if num ==3:
                    quest_button.set_text('Що росте на яблуні?', WHITE,35, None)
                quest_button.draw(10,25)
 
            if event.key == pygame.K_a:
                num = randint (1,3)
                if num ==1:
                    ans_button.set_text('Python', WHITE,35, None)
                if num ==2:
                    ans_button.set_text('Французька', WHITE,35, None)
                if num ==3:
                    ans_button.set_text('Яблука', WHITE,35, None)
                ans_button.draw(10,25)





