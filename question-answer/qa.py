import pygame
from random import randint
pygame.init()

#-------Constants
WINDOW_SIZE = (500, 500)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 150)

#-------Create Window
window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(WHITE)
pygame.display.set_caption("Питання та відповідь")
fps = pygame.time.Clock()

#-------Class Button
class Button():

 def __init__(self, x, y, width, height, color):
  self.rect = pygame.rect.Rect(x,y,width,height)
  self.bgcolor = color

 def set_text(self, text, text_color, font_size, font):
  self.font = pygame.font.Font(font, font_size)
  self.text = self.font.render(text, True, text_color)

 def draw(self, shift_x, shift_y):
  pygame.draw.rect(window, self.bgcolor, self.rect)
  self.text.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))

#--------Create buttons
quest_button = Button(120,100,290,70, BLUE)
ans_button = Button(120,240,290,70, BLUE)

#Set buttons` start text
quest_button.set_text("Питання", WHITE, 75, None)
ans_button.set_text("Відповідь", WHITE, 75, None)

#Draw Buttons` start text
quest_button.draw(10, 10)
ans_button.draw(10, 10)


#-------Game Cycle
game = True

while game:

 fps.tick(60)
 pygame.display.flip()

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
game = False
  if event.type == pygame.KEYDOWN:
if event.type == pygame.K_q:
 quest_button.set_text("Яку ти мову вивчаєш в Logika?", WHITE, 35, None)  
if event.type == pygame.K_a:
 ans_button.set_text("Python", WHITE, 35, None)

