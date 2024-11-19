import logging
from pathlib import Path

import pygame

from config import SPRITES_FOLDER
from toolbox.button.button import Button
from toolbox.scene import Scene

from .constants import Action


class QuitableScene(Scene):
    logger = logging.getLogger("MainMenuScene")

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.quit_button = self._make_quit_button()

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add(self.quit_button)
        self.all_sprites.add(self.quit_button)

    def quit_game(self):
        """Callback method to quit the game."""
        self.status.done = True
        self.status.success = True
        self.status.action = Action.QUIT_GAME

    def _make_quit_button(self):
        quit_button_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "quit_button.png")
        ).convert_alpha()
        quit_button_size = pygame.Vector2(50, 50)
        return Button(
            pos=self.screen_top_right_corner
            + pygame.Vector2(-10, 10)
            + pygame.Vector2(-quit_button_size.x, quit_button_size.y),
            size=quit_button_size,
            callback=self.quit_game,
            image=quit_button_image,
        )
