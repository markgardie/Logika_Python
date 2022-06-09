
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
ICON_PATH = os.path.join(PROJECT_PATH, "images/icon.jpg")
FONT_PATH = os.path.join(PROJECT_PATH, "font/dialog.otf")
FONT_SIZE = 60
BLACK =  (255,255,255)
SIZE = 10
DICT_WARRIOR = {
                    "HP": 9,
                    "Attack": 3,
                    "Defense": 5,
                    "Crystal": 5
                }


#------Create window

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Card Game")
icon = pygame.image.load(ICON_PATH)
pygame.display.set_icon(icon)

fps = pygame.time.Clock()


#------Card class

class Card():

    def __init__(self, 
                    x,
                    y, 
                    width, 
                    height, 
                    image_name,
                    crystal= None, 
                    defense = None,
                    attack = None,
                    hp = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_name = image_name
        self.image = None
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.num = None
        self.key_pressed = False 
        self.impact_time = 0 
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)

        self.load_image()

        self.crystal = self.create_text(crystal)
        self.defense = self.create_text(defense)
        self.attack = self.create_text(attack)
        self.hp = self.create_text(hp)


    def load_image(self):
        image_path = os.path.join(PROJECT_PATH, self.image_name)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def create_text(self, card_text):
        text = self.font.render(str(card_text), True, BLACK)
        return text   

    def card_blit(self, window, enemy = None):
        window.blit(self.image, (self.X, self.Y))
        window.blit(self.crystal, (self.X + 12, self.Y + 5))
        window.blit(self.defense, (self.X + 12, self.Y + CARD_HEIGHT - 65))
        window.blit(self.attack, (self.X + CARD_WIDTH - 35, self.Y + CARD_HEIGHT - 65))


#------Create Player Cards
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
                    "images/" + str(i+1) + ".jpg",
                    crystal= DICT_WARRIOR["Crystal"],
                    defense= DICT_WARRIOR["Defense"],
                    hp= DICT_WARRIOR["HP"],
                    attack= DICT_WARRIOR["Attack"])

        cards_list.append(card)
        card.num = i + 1
        x += CARD_WIDTH + 10

create_cards(big_cards)
create_cards(small_cards, SIZE)


#------Create Enemy Card
enemy = Card(
        width=CARD_WIDTH + 40, 
        height=CARD_HEIGHT + 30, 
        x = WINDOW_WIDTH//2 - CARD_WIDTH//2,
        y = WINDOW_HEIGHT//2 - CARD_HEIGHT,
        image_name="images/6.png"
        )

#------Click on card 
def onclick_card(x,y, enemy):

    for card in big_cards:
        if card.rect.collidepoint(x, y) and enemy.impact_time <= 0:
            for el in big_cards:
                el.key_pressed = True
            print(f"Card {card.num} has been clicked")
            card.key_pressed = True
            return card.num

#------Enemy touched
def enemy_touched(x,y, enemy):
    if  enemy.rect.collidepoint(x, y) and enemy.impact_time <= 0:
                    enemy.key_pressed = True 
                    for card in big_cards:
                        if card.key_pressed:
                            enemy.impact_time = 60

#------Player`s Cards Movement
def move_card(enemy, clicked_card_num):

    if enemy.impact_time > 0:
        big_cards[clicked_card_num - 1].key_pressed = False           
        big_cards[clicked_card_num - 1].x = enemy.x - 40
        big_cards[clicked_card_num - 1].y = enemy.y + 50            
        enemy.impact_time -= 1
        
    if enemy.impact_time <= 0:
        enemy.key_pressed = False
        big_cards[clicked_card_num - 1].x = big_cards[clicked_card_num - 1].rect.x
        big_cards[clicked_card_num - 1].y = big_cards[clicked_card_num - 1].rect.y  

#------Game Cycle
game = True
flag = 0
clicked_card_num = 0
 
while game:

    #------Draw Enemy Card
    window.blit(enemy.image, (enemy.x, enemy.y))

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            clicked_card_num = onclick_card(x,y,enemy)
            flag = 10
            enemy_touched(x,y, enemy)

    
    #------Player`s Cards Movement
    move_card(enemy, clicked_card_num)
    

    fps.tick(60)
    pygame.display.flip()
    window.fill(LEMON)
    
   
    
