import logging
from abc import abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import pygame

from config import FRAME_RATE, SPRITES_FOLDER
from game.game import Game
from toolbox.ui.image import Image
from toolbox.ui.window import Window
from toolbox.utils.patterns import cached

from .status import Status

if TYPE_CHECKING:
    from toolbox.ui.button import Button


class Scene:
    NAME = "Undefined"
    logger = logging.getLogger("Scene")

    def __init__(self, game: Game):
        self.logger.info("Loading...")

        self.game = game

        self.done = False
        self.clock = pygame.time.Clock()

        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pygame.sprite.Group()
        self.all_buttons: pygame.sprite.Group["Button"] = pygame.sprite.Group()
        self.all_windows: list["Window"] = []

        self.status = Status(self.NAME)

    @property
    @cached()
    def screen_bottom_right_corner(self):
        return pygame.Vector2(self.game.screen.get_size())

    @property
    @cached()
    def screen_bottom_left_corner(self):
        _, y = self.screen_bottom_right_corner
        return pygame.Vector2(0, y)

    @property
    @cached()
    def screen_top_left_corner(self):
        return pygame.Vector2(0, 0)

    @property
    @cached()
    def screen_top_right_corner(self):
        x, _ = self.screen_bottom_right_corner
        return pygame.Vector2(x, 0)

    @property
    @cached()
    def screen_center(self):
        x, y = self.screen_bottom_right_corner
        return pygame.Vector2(x // 2, y // 2)

    @property
    @cached()
    def screen_bottom_center(self):
        x, y = self.screen_bottom_right_corner
        return pygame.Vector2(x // 2, y)

    @property
    @cached()
    def screen_top_center(self):
        x, y = self.screen_top_right_corner
        return pygame.Vector2(x // 2, y)

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError()

    def run(self) -> Status:
        while not self.status.done:
            self.dt = self.clock.tick(FRAME_RATE) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

        return self.status

    def handle_events(self):
        events = pygame.event.get()

        for window in self.all_windows:
            window.handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True

            for button in self.all_buttons:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.game.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.game.screen)
        for window in self.all_windows:
            if window.active:
                window.draw(self.game.screen)
        pygame.display.flip()

    def _make_pop_up_window(
        self,
        name: Optional[str] = None,
        pos: Optional[pygame.Vector2] = None,
        background_image: Optional[Image] = None,
    ) -> Window:

        if not background_image:
            background_image = pygame.image.load(
                Path.joinpath(SPRITES_FOLDER, "popup_bckg.png")
            ).convert_alpha()

        background = Image(
            image=background_image,
            pos=pos if pos else self.screen_center,
        )

        window = Window(
            scene=self,
            name=name,
            background=background,
        )
        window.active = False
        return window
