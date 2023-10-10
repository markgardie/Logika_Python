import pygame

from load_sprites import load_image

# спадкується від встроєного в пайгейм класу Спрайт
# треба для додавання в групу
# група дозволяє запускати рух, малювання об'єктів однією строкою для всіх 
# об'єктів в групі 
class Dino(pygame.sprite.Sprite):

    # початкові координати динозаврика, 200, 200
     def __init__(self, x=200, y=200):
         
         super(Dino, self).__init__()

        # список зображень
        # складається із 3 внутрішніх списків-наборів
         self.images = [
             # перший набір відповідає за стоячого динозаврика
             [
                 load_image('dino1.png'),
                 load_image('dino2.png'),
                 load_image('dino3.png')
             ],
             # другий набір - за динозаврика, який присідає
             [
                 load_image('dino4.png'),
                 load_image('dino5.png')
             ],
             # третій набр - анімація смерті
             [
                 load_image('dead_dino.png')
             ]
         ]
         # номер набору, який зараз показується на екрані
         # одночасно вказує на стан динозаврика: стоїть, присідає, помер
         self.set = 0
         # номер конкретного зображення із набору
         self.index = 0
         # отримуємо по номерам вище зображення
         self.image = self.images[0][self.index]

        # швидкість руху
         self.speed_x = 0
         self.speed_y = 0
        
        # координати
         self.x = x
         self.y = y

        # хітбокс
         self.rect = pygame.rect.Rect(self.x, self.y, 44, 47)

        # чи живий динозаврик
         self.is_alive = True

    # функція для руху динозавра
     def update(self):
         # рухаємось в певну точку з певною швидкістю
         # рухаємо хітбокс
         self.rect.move_ip(self.speed_x, self.speed_y)

        # анімація руху
        # якщо швидкість не нульова (динозавр рухається)
         if(self.speed_x != 0):
             # перемикаємось на наступне зображення
             self.index += 1
             # якщо вже на останньому зображені
             if self.index == len(self.images[self.set]):
                # повертаємось назад до першого
                 self.index = 0
             self.image = self.images[self.set][self.index]

    # зупинка дій динозавра (руху, присідання)
     def stop(self):
         # швидкість нульова, припиняємо рух
         self.speed_x = 0

        # якщо другий набір (динозавр присідає)
         if self.set == 1:
             # повертаємо хітбокс вертикально, аби динозавр стояв
             x = self.rect.left
             y = self.rect.top - 17
             self.rect = pygame.rect.Rect(x, y, 44, 27)

        # повертаємось до першого набору (динозавр стоїть)
         self.index = 0
         self.set = 0
         self.image = self.images[self.set][self.index]

     def collision(self, sprite: pygame.sprite.Sprite):
         return self.rect.colliderect(sprite.rect)

    # анімація смерті
     def animate_death(self):
         # при загибелі, динозавр не рухається
         self.speed_x = 0
         # третій набір із картинкою поразки
         self.set = 2
         self.index = 0
         self.image = self.images[self.set][self.index]

    # присідання
     def crouch(self):
         # повертаємо хітбокс горизонтально, аби персонаж присідав
         x = self.rect.left
         y = self.rect.top + 17
         # перемикаємось на 2 набір із картинками присідання
         self.set = 1
         self.index = 0
         self.rect = pygame.rect.Rect(x, y, 59, 30)
         self.image = self.images[self.set][self.index]