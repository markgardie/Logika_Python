from Sprite import Sprite
from Constants import*

class Enemy(Sprite):

    # рух ворога
    def move(self):

        # ворог рухається вліво або вправо
        # є крайня ліва та права точки, між якими він рухається
        # перевіряючи положення ворога відносно цих точок
        # ми можемо зрозуміти напрямок руху
        if self.rect.x <= MONSTER_RIGHT_POINT:
            self.direction = "right"
        if self.rect.x >= MONSTER_LEFT_POINT:
            self.direction = "left"


        # в залежності від напрямку рухаємось в різні сторони
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed