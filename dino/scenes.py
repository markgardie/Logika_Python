"""
scenes.py — ігрові сцени.

Кожна сцена — самодостатній об'єкт із трьома методами:
    handle_event(event) → Scene | None
    update()            → Scene | None
    draw(surface)       → None

Повернення нової сцени = перехід до неї; None = залишитись.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

import pygame

from constants import (
    WIN_W, WIN_H, WHITE, BLACK, RED, GREEN, GROUND_Y,
    VICTORY_SCORE,
)
from ui import Label, Button
from objects import Player, Environment, CactusGroup

if TYPE_CHECKING:
    pass   # уникаємо циклічних імпортів


# ──────────────────────────── BASE ────────────────────────────────

class Scene:
    """Абстрактний базовий клас сцени."""

    def handle_event(self, event: pygame.event.Event) -> "Scene | None":
        return None

    def update(self) -> "Scene | None":
        return None

    def draw(self, surface: pygame.Surface) -> None:
        pass


# ──────────────────────────── MENU ────────────────────────────────

class MenuScene(Scene):
    """Головне меню: заголовок + кнопка «Почати гру»."""

    def __init__(self, images: dict[str, pygame.Surface]):
        self._images = images

        cx = WIN_W // 2 - 150
        self._btn_start = Button(cx, 220, "Почати гру", width=300)
        self._btn_start.onclick(self._on_start)

        font = pygame.font.Font(None, 64)
        self._title = font.render("Chrome Dino", True, BLACK)

        self._next_scene: Scene | None = None

    def _on_start(self) -> None:
        self._next_scene = GameScene(self._images)

    def update(self) -> Scene | None:
        self._btn_start.update()
        scene, self._next_scene = self._next_scene, None
        return scene

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(WHITE)
        surface.blit(self._title, (WIN_W // 2 - self._title.get_width() // 2, 120))
        self._btn_start.draw(surface)


# ──────────────────────────── GAME ────────────────────────────────

class GameScene(Scene):
    """Основна ігрова сцена."""

    def __init__(self, images: dict[str, pygame.Surface]):
        self._images = images

        player_y = GROUND_Y - images["run1"].get_height()
        self._player  = Player(100, player_y, images)
        self._env     = Environment(images["ground"], images["cloud"], 0, GROUND_Y)

        self._score_label = Label(WIN_W - 160, 16, 28, BLACK, "Score: 0")
        self._cactus_group = CactusGroup(images["cactus"], self._score_label)

    def update(self) -> Scene | None:
        self._player.update()
        self._env.update()
        self._cactus_group.update()

        if self._cactus_group.collides_with(self._player.rect):
            return GameOverScene(self._images)

        if self._cactus_group.score >= VICTORY_SCORE:
            return VictoryScene(self._images)

        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(WHITE)
        self._env.draw(surface)
        self._cactus_group.draw(surface)
        self._player.draw(surface)
        self._score_label.draw(surface)


# ──────────────────────────── VICTORY ─────────────────────────────

class VictoryScene(Scene):
    """Екран перемоги."""

    def __init__(self, images: dict[str, pygame.Surface]):
        self._images = images

        font = pygame.font.Font(None, 64)
        self._title = font.render("Перемога!", True, WHITE)

        cx = WIN_W // 2 - 150
        self._btn_menu = Button(cx, 260, "Меню", width=300)
        self._btn_menu.onclick(self._on_menu)

        self._next_scene: Scene | None = None

    def _on_menu(self) -> None:
        self._next_scene = MenuScene(self._images)

    def update(self) -> Scene | None:
        self._btn_menu.update()
        scene, self._next_scene = self._next_scene, None
        return scene

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(GREEN)
        surface.blit(self._title,
                     (WIN_W // 2 - self._title.get_width() // 2, 140))
        self._btn_menu.draw(surface)


# ──────────────────────────── GAME OVER ───────────────────────────

class GameOverScene(Scene):
    """Екран програшу."""

    def __init__(self, images: dict[str, pygame.Surface]):
        self._images = images

        font = pygame.font.Font(None, 64)
        self._title = font.render("Програш!", True, WHITE)

        cx = WIN_W // 2 - 150
        self._btn_menu = Button(cx, 260, "Меню", width=300)
        self._btn_menu.onclick(self._on_menu)

        self._next_scene: Scene | None = None

    def _on_menu(self) -> None:
        self._next_scene = MenuScene(self._images)

    def update(self) -> Scene | None:
        self._btn_menu.update()
        scene, self._next_scene = self._next_scene, None
        return scene

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(RED)
        surface.blit(self._title,
                     (WIN_W // 2 - self._title.get_width() // 2, 140))
        self._btn_menu.draw(surface)
