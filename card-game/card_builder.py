from card import*
from constants import*


class CardBuilder():

    def __init__(self, amount, size = 0):

        x = 10
        self.card_list = []

        for i in range(amount):
        
            card = Card(x,
                        WINDOW_HEIGHT - CARD_HEIGHT - 10,
                        CARD_WIDTH - size,
                        CARD_HEIGHT - size,
                        str(i+1) + ".jpg")

            card.num = i + 1
            card.load_image()
            self.card_list.append(card)
            x += CARD_WIDTH + 10
        
    def get_list(self):
        return self.card_list


class EnemyCardBuilder():

    def __init__(self):

        
        self.enemy = Card(
                    width=CARD_WIDTH + 40, 
                    height=CARD_HEIGHT + 30, 
                    x = WINDOW_WIDTH//2 - CARD_WIDTH//2,
                    y = WINDOW_HEIGHT//2 - CARD_HEIGHT,
                    img_name="6.png")

            
        self.enemy.load_image()
        
    def get_enemy(self):
        return self.enemy
            