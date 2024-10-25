import logging

from .game import Game
from .game_state import MainMenuState


class GameStateManager:
    logger = logging.getLogger("Game State Manager")

    def __init__(self, game):
        self.current_state = MainMenuState(game)

    def main_menu(self, game):
        self.logger.debug("main_menu")
        self.current_state = self.current_state.main_menu(game)

    def go_guild(self, game):
        self.logger.debug("go guild")
        self.current_state = self.current_state.go_guild(game)

    def go_bloodheim(self, game):
        self.logger.debug("go bloodheim")
        self.current_state = self.current_state.go_bloodheim(game)

    def start_fight(self, hero, enemies, game):
        self.logger.debug("start fight")
        self.current_state = self.current_state.start_fight(hero, enemies, game)
