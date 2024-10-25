import logging
from abc import abstractmethod

import pygame

from game.game import Game
from toolbox.button.button import Button
from toolbox.utils.patterns import cached

from .status import Status


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
        self.all_buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()

        self.status = Status(self.NAME)

    @property
    @cached()
    def screen_bottom_right_corner(self):
        return self.game.screen.get_size()

    @property
    @cached()
    def screen_top_right_corner(self):
        x, _ = self.screen_bottom_right_corner
        return x, 0

    @property
    @cached()
    def screen_center(self):
        x, y = self.screen_bottom_right_corner
        return x // 2, y // 2

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError()

    def run(self) -> Status:
        while not self.status.done:
            self.dt = self.clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

        return self.status

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            for button in self.all_buttons:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.game.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.game.screen)
        pygame.display.flip()
