
import pygame
import os
pygame.init()

#------Constants

WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600
CARD_WIDTH = 200
CARD_HEIGHT = 320
LEMON = (213, 216, 165)
WHITE = (255, 255, 255)
PROJECT_PATH= os.path.abspath(__file__ + "/..")
ICON_PATH = os.path.join(PROJECT_PATH, "images/icon.png")
SIZE = 10

#------Create window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Card Game")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

fps = pygame.time.Clock()


#------Card class

class Card():

 def __init__(self, x, y, width, height, image_name):
  self.x = x
  self.y = y
  self.width = width
  self.height = height
  self.image_name = image_name
  self.image = None
  self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
  self.num = None

 def load_image(self):
  image_path = os.path.join(PROJECT_PATH, self.image_name)
  self.image = pygame.image.load(image_path)
  self.image = pygame.transform.scale(self.image, (self.width, self.height))


#------Create Cards
big_cards = list()
small_cards = list()

def create_cards(cards_list, size = 0):

 x = 10

 for i in range(4):

  card = Card(
  x,
  WINDOW_HEIGHT - CARD_HEIGHT - 10,
  CARD_WIDTH - size,
  CARD_HEIGHT - size,
  "images/" + str(i+1) + ".png")

  cards_list.append(card)
  card.num = i + 1
  card.load_image()
  x += CARD_WIDTH + 10

create_cards(big_cards)
create_cards(small_cards, SIZE)


#------Click on card event
def onclick_card(x,y):

 for card in big_cards:
  if card.rect.collidepoint(x, y):
print(f"Card {card.num} has been clicked")
return card.num

#------Game Cycle
game = True
flag = 0
clicked_card_num = 0
 
while game:

 #------Draw Big Cards

 if flag == 0:
  for card in big_cards:
window.blit(card.image, (card.x, card.y))
 else:
  flag -= 1
  for card in big_cards:
if card.num != clicked_card_num:
 window.blit(card.image, (card.x, card.y))

 #------Draw Small Cards
 if flag > 0:
  for card in small_cards:
if card.num == clicked_card_num:
 window.blit(card.image, (card.x, card.y))


 #------Check events

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
game = False
  if event.type == pygame.MOUSEBUTTONDOWN:
x, y = event.pos
clicked_card_num = onclick_card(x,y)
flag = 10

 

 fps.tick(60)
 pygame.display.flip()
 window.fill(LEMON)
 

 
