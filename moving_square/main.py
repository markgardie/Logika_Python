"""
Moving Square — базовий шаблон Pygame-гри.

Охоплює: константи, вікно, прямокутники, рух, колізії,
ігровий цикл, події клавіш/кліку, меню, екрани виграшу/програшу.
"""

import sys
import pygame


# ─────────────────────────── КОНСТАНТИ ────────────────────────────

TITLE = "Moving Square"
FPS = 60

# Розміри вікна
WIN_W, WIN_H = 800, 600

# Кольори
C_BG         = (15,  15,  25)
C_PLAYER     = (80,  160, 255)
C_WIN_RECT   = (80,  220, 120)
C_LOSE_RECT  = (220, 70,  70)
C_TEXT       = (230, 230, 230)
C_SUBTEXT    = (150, 150, 160)
C_BTN        = (40,  40,  60)
C_BTN_HOVER  = (65,  65,  95)
C_BTN_BORDER = (100, 100, 140)

# Швидкість гравця (пікселів/кадр)
PLAYER_SPEED = 4

# Розміри об'єктів
PLAYER_SIZE = 40
TARGET_SIZE = 60


# ─────────────────────────── ДОПОМІЖНІ КЛАСИ ──────────────────────

class Button:
    """Проста кнопка з текстом; підтримує hover та клік."""

    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font):
        self.rect  = rect
        self.text  = text
        self.font  = font
        self._hovered = False

    def draw(self, surface: pygame.Surface) -> None:
        color = C_BTN_HOVER if self._hovered else C_BTN
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, C_BTN_BORDER, self.rect, width=2, border_radius=8)
        label = self.font.render(self.text, True, C_TEXT)
        lx = self.rect.centerx - label.get_width() // 2
        ly = self.rect.centery - label.get_height() // 2
        surface.blit(label, (lx, ly))

    def update(self, mouse_pos: tuple[int, int]) -> None:
        self._hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


class Player:
    """Гравець — синій квадрат, яким керують стрілками / WASD."""

    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)

    def handle_keys(self, keys: pygame.key.ScancodeWrapper) -> None:
        dx = dy = 0
        if keys[pygame.K_LEFT]  or keys[pygame.K_a]: dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += PLAYER_SPEED
        if keys[pygame.K_UP]    or keys[pygame.K_w]: dy -= PLAYER_SPEED
        if keys[pygame.K_DOWN]  or keys[pygame.K_s]: dy += PLAYER_SPEED

        self.rect.x = max(0, min(WIN_W - PLAYER_SIZE, self.rect.x + dx))
        self.rect.y = max(0, min(WIN_H - PLAYER_SIZE, self.rect.y + dy))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, C_PLAYER, self.rect, border_radius=6)
        # Невеликий блик зверху
        shine = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 12, 5)
        pygame.draw.rect(surface, (180, 210, 255), shine, border_radius=3)

    def collides_with(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)


class StaticRect:
    """Нерухомий прямокутник-ціль (виграш або програш)."""

    def __init__(self, x: int, y: int, color: tuple[int, int, int], label: str,
                 font: pygame.font.Font):
        self.rect  = pygame.Rect(x, y, TARGET_SIZE, TARGET_SIZE)
        self.color = color
        self.label = label
        self.font  = font

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        text = self.font.render(self.label, True, C_TEXT)
        tx = self.rect.centerx - text.get_width() // 2
        ty = self.rect.bottom + 6
        surface.blit(text, (tx, ty))


# ─────────────────────────── СЦЕНИ ───────────────────────────────

class Scene:
    """Базовий клас сцени. Кожна сцена — окремий «екран» гри."""

    def handle_event(self, event: pygame.event.Event) -> "Scene | None":
        """Повертає нову сцену або None (залишитись у поточній)."""
        return None

    def update(self) -> "Scene | None":
        """Логіка кадру. Повертає нову сцену або None."""
        return None

    def draw(self, surface: pygame.Surface) -> None:
        pass


class MenuScene(Scene):
    """Головне меню з кнопкою «Почати гру»."""

    def __init__(self, fonts: dict[str, pygame.font.Font]):
        self.fonts  = fonts
        btn_rect    = pygame.Rect(0, 0, 220, 55)
        btn_rect.center = (WIN_W // 2, WIN_H // 2 + 40)
        self.btn_start = Button(btn_rect, "Почати гру", fonts["btn"])

    def handle_event(self, event: pygame.event.Event) -> Scene | None:
        if self.btn_start.is_clicked(event):
            return GameScene(self.fonts)
        return None

    def update(self) -> Scene | None:
        self.btn_start.update(pygame.mouse.get_pos())
        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(C_BG)
        _draw_title(surface, self.fonts["title"], TITLE, WIN_H // 2 - 60)
        sub = self.fonts["sub"].render("Знайди правильний квадрат!", True, C_SUBTEXT)
        surface.blit(sub, (WIN_W // 2 - sub.get_width() // 2, WIN_H // 2 - 10))
        self.btn_start.draw(surface)


class GameScene(Scene):
    """Основна ігрова сцена."""

    def __init__(self, fonts: dict[str, pygame.font.Font]):
        self.fonts  = fonts
        self.player = Player(WIN_W // 2 - PLAYER_SIZE // 2,
                             WIN_H  // 2 - PLAYER_SIZE // 2)
        small_font  = fonts["small"]

        # Квадрат-виграш (зелений, ліворуч)
        self.win_rect  = StaticRect(120, 100, C_WIN_RECT,  "WIN",  small_font)
        # Квадрат-програш (червоний, праворуч)
        self.lose_rect = StaticRect(WIN_W - 180, WIN_H - 200, C_LOSE_RECT, "LOSE", small_font)

        self.hint = fonts["small"].render(
            "Стрілки / WASD — рух", True, C_SUBTEXT
        )

    def handle_event(self, event: pygame.event.Event) -> Scene | None:
        return None  # Клавіатура обробляється в update

    def update(self) -> Scene | None:
        keys = pygame.key.get_pressed()
        self.player.handle_keys(keys)

        if self.player.collides_with(self.win_rect.rect):
            return ResultScene(self.fonts, won=True)
        if self.player.collides_with(self.lose_rect.rect):
            return ResultScene(self.fonts, won=False)
        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(C_BG)
        _draw_grid(surface)              # декоративна сітка
        self.win_rect.draw(surface)
        self.lose_rect.draw(surface)
        self.player.draw(surface)
        surface.blit(self.hint, (10, WIN_H - 30))


class ResultScene(Scene):
    """Екран виграшу або програшу з кнопкою повернення в меню."""

    def __init__(self, fonts: dict[str, pygame.font.Font], won: bool):
        self.fonts = fonts
        self.won   = won

        btn_rect = pygame.Rect(0, 0, 200, 52)
        btn_rect.center = (WIN_W // 2, WIN_H // 2 + 60)
        self.btn_menu = Button(btn_rect, "Меню", fonts["btn"])

    def handle_event(self, event: pygame.event.Event) -> Scene | None:
        if self.btn_menu.is_clicked(event):
            return MenuScene(self.fonts)
        return None

    def update(self) -> Scene | None:
        self.btn_menu.update(pygame.mouse.get_pos())
        return None

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(C_BG)
        if self.won:
            heading = "Перемога! 🎉"
            color   = C_WIN_RECT
            sub_txt = "Ти знайшов правильний квадрат."
        else:
            heading = "Програш 💀"
            color   = C_LOSE_RECT
            sub_txt = "Ти вдарився об небезпечний квадрат."

        title_surf = self.fonts["title"].render(heading, True, color)
        surface.blit(title_surf, (WIN_W // 2 - title_surf.get_width() // 2,
                                   WIN_H // 2 - 80))
        sub_surf = self.fonts["sub"].render(sub_txt, True, C_SUBTEXT)
        surface.blit(sub_surf, (WIN_W // 2 - sub_surf.get_width() // 2,
                                 WIN_H // 2 - 10))
        self.btn_menu.draw(surface)


# ─────────────────────────── ДОПОМІЖНІ ФУНКЦІЇ ────────────────────

def _draw_title(surface: pygame.Surface, font: pygame.font.Font,
                text: str, y: int) -> None:
    surf = font.render(text, True, C_TEXT)
    surface.blit(surf, (WIN_W // 2 - surf.get_width() // 2, y))


def _draw_grid(surface: pygame.Surface) -> None:
    """Ненав'язлива декоративна сітка на тлі ігрової сцени."""
    color = (30, 30, 45)
    step  = 60
    for x in range(0, WIN_W, step):
        pygame.draw.line(surface, color, (x, 0), (x, WIN_H))
    for y in range(0, WIN_H, step):
        pygame.draw.line(surface, color, (0, y), (WIN_W, y))


def build_fonts() -> dict[str, pygame.font.Font]:
    """Створює словник шрифтів різних розмірів."""
    return {
        "title": pygame.font.SysFont("consolas", 52, bold=True),
        "sub":   pygame.font.SysFont("consolas", 20),
        "btn":   pygame.font.SysFont("consolas", 24, bold=True),
        "small": pygame.font.SysFont("consolas", 16),
    }


# ─────────────────────────── ГОЛОВНИЙ КЛАС ────────────────────────

class Game:
    """
    Керує ігровим циклом та переходами між сценами.

    Патерн: Scene Manager — кожна сцена самодостатня,
    Game лише делегує їй події, update та draw.
    """

    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((WIN_W, WIN_H))
        pygame.display.set_caption(TITLE)
        self.clock   = pygame.time.Clock()
        self.fonts   = build_fonts()
        self.scene: Scene = MenuScene(self.fonts)

    def _change_scene(self, new_scene: Scene | None) -> None:
        if new_scene is not None:
            self.scene = new_scene

    def run(self) -> None:
        while True:
            # ── Події ──────────────────────────────────────────
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self._quit()
                result = self.scene.handle_event(event)
                self._change_scene(result)

            # ── Оновлення логіки ───────────────────────────────
            result = self.scene.update()
            self._change_scene(result)

            # ── Відмальовка ────────────────────────────────────
            self.scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

    @staticmethod
    def _quit() -> None:
        pygame.quit()
        sys.exit()


# ─────────────────────────── ТОЧКА ВХОДУ ──────────────────────────

if __name__ == "__main__":
    Game().run()