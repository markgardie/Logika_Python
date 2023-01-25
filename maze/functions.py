import pygame
from constants import*

pygame.init()


def draw_sprites(player, wall1, wall2, wall3, enemy, goal, window):
    window.display.blit(window.bg_image, (0,0))

   

    window.display.blit(player.image, (player.rect.x, player.rect.y))
    window.display.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
    window.display.blit(goal.image, (goal.rect.x, goal.rect.y))

    window.display.blit(wall1.image, (wall1.rect.x, wall1.rect.y))
    window.display.blit(wall2.image, (wall2.rect.x, wall2.rect.y))
    window.display.blit(wall3.image, (wall3.rect.x, wall3.rect.y))

def win_lose(player, wall1, wall2, wall3, enemy, goal, window):

    font = pygame.font.Font(None, 70)
    win_text = font.render('YOU WIN!', True, (255, 215, 0))
    lose_text = font.render('YOU LOSE!', True, (180, 0, 0))

    money = pygame.mixer.Sound(r'C:\Users\Марк\Desktop\Logika_Python\maze\resources\money.ogg')
    kick = pygame.mixer.Sound(r'C:\Users\Марк\Desktop\Logika_Python\maze\resources\kick.ogg')

    if (pygame.sprite.collide_rect(player, enemy) 
    or pygame.sprite.collide_rect(player, wall1) 
    or pygame.sprite.collide_rect(player, wall2)
    or pygame.sprite.collide_rect(player, wall3)):
        window.blit(lose_text, (200, 200))
        kick.play()
        return True

    elif pygame.sprite.collide_rect(player, goal):
        window.blit(win_text, (200, 200))
        money.play()
        return True

    else:
        return False


