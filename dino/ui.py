"""
ui.py — перевикористовувані UI-компоненти: Label і Button.
Не залежать від ігрової логіки; можна брати в будь-який проєкт.
"""

import pygame
from constants import WHITE, BLUE, GREEN, RED


class Label:
    """Статичний текстовий напис."""

    def __init__(self, x: int, y: int, size: int,
                 color: tuple = WHITE, text: str = ""):
        self.font   = pygame.font.Font(None, size)
        self.coord  = (x, y)
        self.color  = color
        self.set_text(text)

    def set_text(self, text: str) -> None:
        self.image = self.font.render(text, True, self.color)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.coord)


class Button:
    """
    Кнопка з текстом; підтримує hover-стан та callback onclick.

    Використання:
        btn = Button(x, y, "Текст", width=200)
        btn.onclick(my_function)   # реєструємо callback
        # у циклі:
        btn.update()
        btn.draw(screen)
    """

    HEIGHT = 50

    def __init__(self, x: int, y: int, text: str, width: int = 200):
        self.rect = pygame.Rect(x, y, width, self.HEIGHT)

        # поверхні кнопки (нормальна та hover)
        self._surface_normal = self._make_surface(width, BLUE)
        self._surface_hover  = self._make_surface(width, GREEN)

        font = pygame.font.Font(None, 32)
        self._text_image = font.render(text, True, RED)
        self._text_pos   = (x + 20, y + 10)

        self._hovered = False
        self._fn      = None

    # ── публічне API ──────────────────────────────────────────────

    def onclick(self, fn) -> None:
        """Реєструє функцію, яка викликається при кліку."""
        self._fn = fn

    def update(self) -> None:
        """Оновлює hover-стан та опрацьовує клік."""
        mouse_pos = pygame.mouse.get_pos()
        self._hovered = self.rect.collidepoint(mouse_pos)
        if self._hovered and pygame.mouse.get_pressed()[0] and self._fn:
            self._fn()

    def draw(self, surface: pygame.Surface) -> None:
        img = self._surface_hover if self._hovered else self._surface_normal
        surface.blit(img, self.rect.topleft)
        surface.blit(self._text_image, self._text_pos)

    # ── внутрішнє ─────────────────────────────────────────────────

    @staticmethod
    def _make_surface(width: int, color: tuple) -> pygame.Surface:
        surf = pygame.Surface((width, Button.HEIGHT))
        surf.fill(color)
        return surf
