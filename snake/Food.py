from Sprite import*
from random import*
from constants import*

# клас їжа
# спадкується від Sprite
# копіює хітбокс і картинку
class Food(Sprite):

    # випадково переміщує їжу
    # після торкання зі змійкою
    def move(self):
        # генеруються випадкові координати
        # відступи в 50 пікселей
        self.hitbox.x = randint(50, WINDOW_WIDTH - 50)
        self.hitbox.y = randint(50, WINDOW_HEIGHT - 50)

    