"""
objects.py — ігрові об'єкти: гравець, перешкоди, оточення.
Кожен клас відповідає лише за свою логіку та відмальовку.
"""

from __future__ import annotations
from random import randint

import pygame
from constants import (
    WIN_W, GROUND_Y, GRAVITY, JUMP_VELOCITY,
    PLAYER_SPEED, SCROLL_SPEED,
    SCORE_PER_CACTUS,
)
from ui import Label


# ──────────────────────────── ГРАВЕЦЬ ─────────────────────────────

class Player:
    """
    Діно-гравець: анімований біг + стрибок + горизонтальний рух.

    Параметри:
        x, y    — початкова позиція (лівий верхній кут).
        images  — словник {'run1', 'run2', 'jump'} з pygame.Surface.
    """

    _ANIM_DELAY = 15   # кадрів між зміною кадрів анімації бігу

    def __init__(self, x: int, y: int, images: dict[str, pygame.Surface]):
        self._images = images
        self._image  = images["run1"]

        self._anim_counter   = 0
        self._anim_frame     = 0          # 0 або 1 (run1 / run2)

        self._ground_y = y                # y-рівень землі для гравця
        self.rect      = pygame.Rect(x, y, self._image.get_width(),
                                     self._image.get_height())
        self._velocity = 0.0
        self._in_air   = False

    # ── публічне API ──────────────────────────────────────────────

    def update(self) -> None:
        self._handle_input()
        self._apply_gravity()
        self._animate()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image, self.rect.topleft)

    # ── внутрішнє ─────────────────────────────────────────────────

    def _handle_input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.left = max(0, self.rect.left - PLAYER_SPEED)
        if keys[pygame.K_RIGHT]:
            self.rect.left = min(WIN_W - self.rect.width, 
                                 self.rect.left + PLAYER_SPEED)
        
        if keys[pygame.K_SPACE] and not self._in_air:
            self._velocity = JUMP_VELOCITY
            self._in_air = True
            self._image = self._images["jump"]
            self._anim_counter = 0


    def _apply_gravity(self) -> None:
       pass

    def _animate(self) -> None:
        pass
