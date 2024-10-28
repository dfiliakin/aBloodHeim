from game.game import Game
from objects.guild.repository.guild_repository import GuildRepository
from toolbox.ui.button import Button
import logging
import pygame
from .quitable_scene import QuitableScene
from .constants import Action


class MainMenuScene(QuitableScene):
    NAME = "Main Menu"
    logger = logging.getLogger("MainMenuScene")

    def __init__(self, game: Game):

        super().__init__(game)

        self.new_game_button = self._make_new_game_button()

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add(self.quit_button, self.new_game_button)
        self.all_sprites.add(self.quit_button, self.new_game_button)

    def new_game(self):
        self.logger.debug("I'm trying to start new game")

        # FIXME: create a new guild here.
        new_guild = GuildRepository.fetch_guild_by_guild_name("test")
        self.game.guild = new_guild

        self.logger.info(f"New guild: {new_guild}")

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
