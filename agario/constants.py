# Мережеві налаштування
SERVER_HOST = 'localhost'
SERVER_PORT = 8080
BUFFER_SIZE = 4096

# Налаштування вікна
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FPS = 60

# Налаштування гравця
PLAYER_START_RADIUS = 20
PLAYER_SPEED = 15
PLAYER_COLOR_SELF = (0, 255, 0)  # Зелений для свого гравця
PLAYER_COLOR_OTHER = (255, 0, 0)  # Червоний для інших

# Налаштування їжі
FOOD_COUNT = 300
FOOD_RADIUS = 10
FOOD_GROWTH_RATE = 0.2  # Скільки розміру додається при з'їданні їжі
WORLD_MIN = -2000
WORLD_MAX = 2000

# Налаштування масштабування камери
SCALE_MIN = 0.3
SCALE_MAX = 1.5
SCALE_FACTOR = 50

# Налаштування колізій гравців
COLLISION_SIZE_RATIO = 1.1  # Гравець повинен бути на 10% більшим
PLAYER_GROWTH_FROM_EATING = 0.5  # Скільки розміру отримує гравець від з'їдання іншого

# Текст
FONT_SIZE = 50
LOSE_TEXT = 'U lose!'
LOSE_TEXT_COLOR = (244, 0, 0)
LOSE_TEXT_POS = (400, 500)

# Кольори
COLOR_WHITE = (255, 255, 255)