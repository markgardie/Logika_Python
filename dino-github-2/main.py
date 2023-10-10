import pygame

from dino import Dino
from bat import Bat
from load_sprites import load_image

# створення екрану
screen = pygame.display.set_mode((600,300))
# виставлення надпису, заголовка екрана
pygame.display.set_caption("Google Chrome Dino Game")

# годинник для тіків
clock = pygame.time.Clock()
# кількість кадрів в секунду
# кадрів мало для створення ілюзії старої піксельної гри
fps = 15

# створюється динозавр
dino = Dino()
# додаємо його в групу для використання зручніших функції малювання та руху
dino_sprites = pygame.sprite.Group(dino)

# тут так само, але з кажаном
bat = Bat()
bat_sprites = pygame.sprite.Group(bat)

# завантажуємо зображення поверхні і надпис game over
ground = load_image('ground.png')
game_over = load_image('game_over.png')

# створюємо код для власної події смерті
DIE_EVENT = pygame.USEREVENT + 1

# ігровий цикл
# поки змінна game = True гра працює
# інакше закривається вікно і програма
game = True
while game:
     for event in pygame.event.get():
         # подія натискання на крестик
         # зупиняємо гру і закриваємо вікно
         if event.type == pygame.QUIT:
             game = False
        
         # подія смерті динозаврика
         # змінюємо змінну і вказуємо, що динозавр неживий
         if event.type == DIE_EVENT:
             dino.is_alive = False
         
         # якщо динозавр живий
         # то перевіряємо клавіші керування
         if dino.is_alive:
             # якщо натиснуто клавішу
             if event.type == pygame.KEYDOWN:
                 # якщо стрілка вліво
                 if event.key == pygame.K_LEFT:
                     # від'ємна швидкість - рух вліво
                     dino.speed_x = -10
                 # якщо стрілка вправо
                 if event.key == pygame.K_RIGHT:
                     # додатня швидкість - рух вправо
                     dino.speed_x = 10
                 # якщо стрілка вниз
                 if event.key == pygame.K_DOWN:
                     # присідаємо
                     dino.crouch()
             # якщо перестаємо натискати на клавіші
             if event.type == pygame.KEYUP:
                 # і ці клавіші відносяться до керування
                 if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN]:
                     # зупиняємо всі дії динозаврика
                     dino.stop()

     # заповнюємо фон вікна білим кольором
     screen.fill((255,255,255))
     # накладаємо на екран зображення поверхні, землі
     screen.blit(ground, [0,235])
    
     # якщо динозаврик торкається кажана
     if dino.collision(bat):
         if dino.is_alive:
             # показуємо надпис поразки
             print('GAME OVER')
             # анімація смерті
             dino.animate_death()
             # запускаємо подію смерті
             pygame.time.set_timer(DIE_EVENT, 100)
            
     # запускаємо рух динозаврика
     dino_sprites.update()
     # малюємо динозаврика
     dino_sprites.draw(screen)
     
     # якщо динозаврик живий
     if dino.is_alive:
         # рухаємо кажана
         bat_sprites.update()
         # малюємо кажана
         bat_sprites.draw(screen)
     else:
         # якщо динозаврик неживий
         # то малюємо надпис поразки
         screen.blit(game_over, [200,100])
     
     # тіки годинника
     clock.tick(fps)
     # оновлення екрана
     pygame.display.flip()
# закриття гри
pygame.quit()