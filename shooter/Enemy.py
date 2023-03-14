from Sprite import*
from constants import*
from random import randint

# ворог являється спрайтом, тому спадкується від нього
class Enemy(Sprite):

    # рух ворога, називається update, оскільки група ворогів бачить лише методи, які називається update
    def update(self):
        # рух вниз (y+) на певну швидкість
        self.rect.y += self.speed

        # якщо ворог досягає нижньої межі (координата нижньої межі дорівнює висоті вікна)
        if self.rect.y > WINDOW_HEIGHT:
            
            # це означає, що ми пропустили, тому збільшуємо лічильник
            miss[0] += 1
            # генеруємо випадковий x для спавну
            self.rect.x = randint(80, WINDOW_WIDTH - 80)
            # але по висоті ворог буде завжди з'являтись біля верхньої межі
            self.rect.y = 0
        


        
            