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

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.left = max(0, self.rect.left - PLAYER_SPEED)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.left = min(WIN_W - self.rect.width,
                                  self.rect.left + PLAYER_SPEED)

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self._in_air:
            self._velocity  = JUMP_VELOCITY
            self._in_air    = True
            self._image     = self._images["jump"]
            self._anim_counter = 0

    def _apply_gravity(self) -> None:
        if not self._in_air:
            return
        self.rect.top -= int(self._velocity)
        self._velocity -= GRAVITY
        if self.rect.top >= self._ground_y:
            self.rect.top = self._ground_y
            self._in_air  = False

    def _animate(self) -> None:
        if self._in_air:
            return
        self._anim_counter += 1
        if self._anim_counter >= self._ANIM_DELAY:
            self._anim_counter = 0
            self._anim_frame   = 1 - self._anim_frame   # перемикання 0↔1
            key = "run1" if self._anim_frame == 0 else "run2"
            self._image = self._images[key]


# ──────────────────────────── КАКТУС ──────────────────────────────

class Cactus:
    """Один кактус — рухається ліворуч зі сталою швидкістю."""

    def __init__(self, x: int, y: int, image: pygame.Surface):
        self._image = image
        self.rect   = pygame.Rect(x, y, image.get_width(), image.get_height())

    def update(self) -> None:
        self.rect.left -= SCROLL_SPEED

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image, self.rect.topleft)


# ──────────────────────────── ХМАРА ───────────────────────────────

class Cloud:
    """Декоративна хмара, що дрейфує ліворуч."""

    _SPEED = 2

    def __init__(self, image: pygame.Surface):
        self._image = image
        self.rect   = pygame.Rect(
            WIN_W, randint(20, 150),
            image.get_width(), image.get_height(),
        )

    def update(self) -> None:
        self.rect.left -= self._SPEED

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image, self.rect.topleft)

    @property
    def is_offscreen(self) -> bool:
        return self.rect.right < 0


# ──────────────────────────── ОТОЧЕННЯ ────────────────────────────

class Environment:
    """
    Фон: нескінченний трек + динамічні хмари.
    Не взаємодіє з гравцем — лише візуальний шар.
    """

    _CLOUD_INTERVAL_MIN = 80
    _CLOUD_INTERVAL_MAX = 200

    def __init__(self, ground_image: pygame.Surface, cloud_image: pygame.Surface,
                 x: int, y: int):
        self._ground_image = ground_image
        self._cloud_image  = cloud_image
        self._rect         = pygame.Rect(x, y,
                                         ground_image.get_width(),
                                         ground_image.get_height())
        self._scroll_counter = 0
        self._clouds: list[Cloud] = []
        self._cloud_timer     = 0
        self._cloud_interval  = randint(self._CLOUD_INTERVAL_MIN,
                                        self._CLOUD_INTERVAL_MAX)

    def update(self) -> None:
        self._scroll_ground()
        self._update_clouds()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._ground_image, (self._rect.left, self._rect.top))

        surface.blit(
            self._ground_image,
            (self._rect.left + self._ground_image.get_width(),
            self._rect.top)
        )

        for cloud in self._clouds:
            cloud.draw(surface)

    # ── внутрішнє ─────────────────────────────────────────────────

    def _scroll_ground(self) -> None:
        self._rect.left -= SCROLL_SPEED

        if self._rect.right <= 0:
            self._rect.left = 0

    def _update_clouds(self) -> None:
        self._cloud_timer += 1
        if self._cloud_timer >= self._cloud_interval:
            self._cloud_timer    = 0
            self._cloud_interval = randint(self._CLOUD_INTERVAL_MIN,
                                           self._CLOUD_INTERVAL_MAX)
            self._clouds.append(Cloud(self._cloud_image))

        for cloud in self._clouds[:]:
            cloud.update()
            if cloud.is_offscreen:
                self._clouds.remove(cloud)


# ──────────────────────────── ГРУПА КАКТУСІВ ──────────────────────

class CactusGroup:
    """
    Керує появою, рухом і підрахунком очок за кактуси.

    Параметри:
        cactus_image — зображення одного кактуса.
        score_label  — Label для відображення рахунку.
    """

    _SPAWN_MIN = 150
    _SPAWN_MAX = 300

    def __init__(self, cactus_image: pygame.Surface, score_label: Label):
        self._image       = cactus_image
        self._label       = score_label
        self._obstacles: list[Cactus] = []
        self._timer       = 0
        self._timer_max   = randint(self._SPAWN_MIN, self._SPAWN_MAX)
        self.score        = 0

    def update(self) -> None:
        self._spawn_tick()
        for cactus in self._obstacles[:]:
            cactus.update()
            if cactus.rect.right < 0:
                self._obstacles.remove(cactus)
                self.score += SCORE_PER_CACTUS
                self._label.set_text(f"Score: {self.score}")

    def draw(self, surface: pygame.Surface) -> None:
        for cactus in self._obstacles:
            cactus.draw(surface)

    def collides_with(self, player_rect: pygame.Rect) -> bool:
        return any(c.rect.colliderect(player_rect) for c in self._obstacles)

    # ── внутрішнє ─────────────────────────────────────────────────

    def _spawn_tick(self) -> None:
        self._timer += 1
        if self._timer >= self._timer_max:
            self._timer     = 0
            self._timer_max = randint(self._SPAWN_MIN, self._SPAWN_MAX)
            self._obstacles.append(
                Cactus(WIN_W, GROUND_Y - self._image.get_height() + 10,
                       self._image)
            )