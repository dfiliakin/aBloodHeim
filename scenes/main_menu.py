from toolbox.button.button import Button
import logging
import pygame
from .quitable_scene import QuitableScene
from .constants import Action


class MainMenuScene(QuitableScene):
    NAME = "Main Menu"
    logger = logging.getLogger("MainMenuScene")

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.new_game_button = self._make_new_game_button()

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add(self.quit_button, self.new_game_button)
        self.all_sprites.add(self.quit_button, self.new_game_button)

    def new_game(self):
        self.logger.debug("I'm trying to start new game")
        self.status.done = True
        self.status.success = True
        self.status.action = Action.NEW_GAME
        # FIXME: save the status to a log file.

    def _make_new_game_button(self):
        new_game_button_size = pygame.Vector2(200, 70)
        return Button(
            pos=self.screen_center,
            size=new_game_button_size,
            callback=self.new_game,
            text="New Game",
        )
