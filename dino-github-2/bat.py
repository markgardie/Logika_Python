import pygame

from load_sprites import load_image

# спадкується від встроєного в пайгейм класу Спрайт
# треба для додавання в групу
# група дозволяє запускати рух, малювання об'єктів однією строкою для всіх 
# об'єктів в групі 
class Bat(pygame.sprite.Sprite):

    def __init__(self, x=600, y=180):
        super(Bat, self).__init__()

        # зображення для анімації руху кажана
        self.images = [
            load_image('bat1.png'),
            load_image('bat2.png')
        ]
        # номер зображення
        self.index = 0
        # отримання зображення по номеру
        self.image = self.images[self.index]

        # швидкість кажана
        # від'ємна, оскільки він рухається вліво
        self.speed_x = -10
        self.speed_y = 0

        # координати
        self.x = x
        self.y = y

        # хітбокс
        self.rect = pygame.rect.Rect(self.x, self.y, 43, 34)

    # функція руху кажана
    def update(self):
        # переміщення хітбокса
        self.rect.move_ip(self.speed_x, self.speed_y)
        
        # якщо кажан виходить за ліву межу
        # то повертаємо його назад
        if self.rect.left < -10:
            self.rect = pygame.rect.Rect(self.x, self.y, 43, 34)

        # анімація руху
        # якщо швидкість не нульова
        if(self.speed_x != 0):
            # перемикаємось на наступне зображення
            self.index += 1
            # якщо на останньому зображенні
            if self.index == len(self.images):
                # починаємо заново з першого зображення
                self.index = 0
            self.image = self.images[self.index]

    # зупинка руху
    def stop(self):
        # швидкість нульова
        self.speed_x = 0
        # перше зображення
        self.index = 0
        self.image = self.images[self.index]