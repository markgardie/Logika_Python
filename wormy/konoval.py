import pygame
pygame.init()

font1 = pygame.font.SysFont("Times New Roman", 25)

def draw_press_ke_msg():
    key_text = font1.render("Натисніть а, щоб роспочати гру", True,(250,0,250))
    key_text_rect = key_text.get_rect()
    key_text_rect.topleft = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 100)
    window.blit(key_text,key_text_rect)


