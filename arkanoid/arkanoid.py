import pygame
pygame.init() #підключаємо всі можливості бібліотеки pygame
window = pygame.display.set_mode((600,600)) #задаємо розмір екрану
pygame.display.set_caption("Арканоїд") #задання заголовку вікна
background = pygame.transform.scale(pygame.image.load("fon.jpeg"),(600,600))
'''завантажуємо картинку (pygame.image.load) та підганяємо 
під розміри екрану (pygame.transform.scale) і зберігаємо в 
змінну background'''

clock = pygame.time.Clock()

rocket_x = 200
rocket_y = 550
#місцерозташування ракетки
game_over = False
#змінна, що відповідає за завершення гри
class GameSprite(pygame.sprite.Sprite): #клас для всіх обʼєктів гри
    def __init__(self,image,player_x,player_y, width, height, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image),(width,height))
        self.player_x = player_x
        self.player_y = player_y
        self.player_speed = player_speed

        # перший спосіб створення хітбокса
        self.hitbox = pygame.Rect(player_x, player_y, width, height)

        # другий спосіб створення хітбокса
        # обрати один спосіб
        self.hitbox2 = self.image.get_rect()


class Rocket(GameSprite):

    def controls(self, left, right):

        keys = pygame.key.get_pressed()

        # збільшити цифру до 5-10
        if keys[left] and self.hitbox.x > 0:
            self.hitbox.x -= self.player_speed

        if keys[right] and self.hitbox.x < 600:
            self.hitbox.x += self.player_speed

class Ball(GameSprite):

    def move(self, dir_x, dir_y):
        self.hitbox.x += self.player_speed * dir_x
        self.hitbox.y += self.player_speed * dir_y