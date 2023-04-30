from constants import*
from functions import*
from Window import*
from Boss import*
from Player import*
from Fireball import*

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CAPTION, BLUE)

boss = Boss(BOSS_WIDTH, BOSS_HEIGHT, BOSS_X, BOSS_Y, BOSS_PATH, BOSS_SPEED)
player = Player(PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_X, PLAYER_Y, PLAYER_PATH, PLAYER_SPEED)

fireballs = []

# змінна, яка відповідає за запуск гри
game = True 
# змінна, яка перемикає на екран
finish = False 
# текст на фінальному екрані
text = "" 
font = pygame.font.Font(None, 30)

while game:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    
