import pygame

from dino import Dino
from bat import Bat
from load_sprites import load_image

screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("Google Chrome Dino Game")

clock = pygame.time.Clock()
fps = 15

dino = Dino()
dino_sprites = pygame.sprite.Group(dino)

bat = Bat()
bat_sprites = pygame.sprite.Group(bat)

ground = load_image('ground.png')
game_over = load_image('game_over.png')

DIE_EVENT = pygame.USEREVENT + 1

game = True
while game:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             game = False
        
         if event.type == DIE_EVENT:
             dino.is_alive = False

         if dino.is_alive:
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     dino.speed_x = -10
                 if event.key == pygame.K_RIGHT:
                     dino.speed_x = 10
                 if event.key == pygame.K_DOWN:
                     dino.crouch()
             if event.type == pygame.KEYUP:
                 if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN]:
                     dino.stop()


     screen.fill((255,255,255))
     screen.blit(ground, [0,235])

     if dino.collision(bat):
         if dino.is_alive:
             print('GAME OVER')
             dino.animate_death()
             pygame.time.set_timer(DIE_EVENT, 100)
            
     dino_sprites.update()
     dino_sprites.draw(screen)

     if dino.is_alive:
         bat_sprites.update()
         bat_sprites.draw(screen)
     else:
         screen.blit(game_over, [200,100])

     clock.tick(fps)
     pygame.display.flip()

pygame.quit()