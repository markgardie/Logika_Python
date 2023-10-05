import pygame

from load_sprites import load_image

class Dino(pygame.sprite.Sprite):

     def __init__(self, x=200, y=200):
         
         super(Dino, self).__init__()
     
         self.images = [
             [
                 load_image('dino1.png'),
                 load_image('dino2.png'),
                 load_image('dino3.png')
             ],
             [
                 load_image('dino4.png'),
                 load_image('dino5.png')
             ],
             [
                 load_image('dead_dino.png')
             ]
         ]
         self.set = 0
         self.index = 0
         self.image = self.images[0][self.index]

         self.speed_x = 0
         self.speed_y = 0
         self.x = x
         self.y = y
         self.rect = pygame.rect.Rect(self.x, self.y, 44, 47)

         self.is_alive = True
         self.is_jumping = False
         self.is_crouching = False


     def update(self):
         self.rect.move_ip(self.speed_x, self.speed_y)

         if(self.speed_x != 0):
             self.index += 1
             if self.index == len(self.images[self.set]):
                 self.index = 0
             self.image = self.images[self.set][self.index]

     def stop(self):
         self.speed_x = 0

         if self.set == 1:
             x = self.rect.left
             y = self.rect.top - 17
             self.rect = pygame.rect.Rect(x, y, 44, 27)

         self.index = 0
         self.set = 0
         self.image = self.images[self.set][self.index]

     def collision(self, sprite: pygame.sprite.Sprite):
         return self.rect.colliderect(sprite.rect)

     def animate_death(self):
         self.speed_x = 0
         self.set = 2
         self.index = 0
         self.image = self.images[self.set][self.index]

     def crouch(self):
         x = self.rect.left
         y = self.rect.top + 17
         self.set = 1
         self.index = 0
         self.rect = pygame.rect.Rect(x, y, 59, 30)
         self.image = self.images[self.set][self.index]