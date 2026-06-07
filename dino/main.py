"""
main.py — точка входу Chrome Dino.

Запуск:  python main.py

Архітектура: Scene Manager.
Game керує циклом і делегує всю логіку поточній сцені.
"""

import sys
import pygame

from constants import TITLE, WIN_W, WIN_H, FPS, load_images
from scenes import MenuScene, Scene


class Game:
    """
    Ігровий рушій: вікно, годинник, цикл, перемикання сцен.
    Не містить ігрової логіки — лише інфраструктуру.
    """

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption(TITLE)
        self._clock = pygame.time.Clock()

        images = load_images()
        self._scene: Scene = MenuScene(images)

    # ── головний цикл ──────────────────────────────────────────────

    def run(self) -> None:
        while True:
            self._process_events()
            self._update()
            self._draw()
            self._switch()

    # ── приватні методи ────────────────────────────────────────────

    def _process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._quit()
            self._switch(self._scene.handle_event(event))

    def _update(self) -> None:
        self._switch(self._scene.update())

    def _draw(self) -> None:
        self._scene.draw(self._screen)
        pygame.display.flip()

    def _switch(self, new_scene: Scene | None) -> None:
        if new_scene is not None:
            self._scene = new_scene

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()