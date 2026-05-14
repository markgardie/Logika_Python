"""
constants.py — глобальні константи та завантаження ресурсів.
Імпортується першим; не містить логіки.
"""

import pygame

# ──────────────────────────── ВІКНО ───────────────────────────────

TITLE   = "Chrome Dino"
WIN_W   = 800
WIN_H   = 400
FPS     = 60

# ──────────────────────────── КОЛЬОРИ ─────────────────────────────

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
RED    = (220, 50,  50)
GREEN  = (50,  180, 80)
BLUE   = (50,  100, 220)
GRAY   = (180, 180, 180)

# ──────────────────────────── ФІЗИКА ──────────────────────────────

GROUND_Y      = 300   # верхня межа землі (y-координата підлоги)
GRAVITY       = 0.7
JUMP_VELOCITY = 15
PLAYER_SPEED  = 5     # горизонтальний рух
SCROLL_SPEED  = 4     # швидкість кактусів та фону

# ──────────────────────────── РАХУНОК ─────────────────────────────

SCORE_PER_CACTUS = 100
VICTORY_SCORE    = 1000

# ──────────────────────────── ЗОБРАЖЕННЯ ──────────────────────────
# Завантажуються один раз після pygame.init(); зберігаються як
# module-level константи, щоб не вантажити з диску щоразу.

def load_images() -> dict[str, pygame.Surface]:
    """Завантажує та повертає словник ігрових зображень."""
    return {
        "run1":   pygame.image.load("images/DinoRun1.png").convert_alpha(),
        "run2":   pygame.image.load("images/DinoRun2.png").convert_alpha(),
        "jump":   pygame.image.load("images/DinoJump.png").convert_alpha(),
        "cactus": pygame.image.load("images/SmallCactus1.png").convert_alpha(),
        "cloud":  pygame.image.load("images/Cloud.png").convert_alpha(),
        "ground": pygame.image.load("images/Track.png").convert_alpha(),
    }
