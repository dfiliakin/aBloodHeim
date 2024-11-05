import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from scenes import GuildScene, MainMenuScene

if TYPE_CHECKING:
    from toolbox.scene import Status as SceneStatus


class GameState(ABC):
    def __init__(self):
        self.game = None
        self.scene = None

    def run(self) -> "SceneStatus":
        return self.scene.run()

    @abstractmethod
    def main_menu(self, game):
        pass

    @abstractmethod
    def go_guild(self, game):
        pass

    @abstractmethod
    def go_bloodheim(self, game):
        pass

    @abstractmethod
    def start_fight(self, hero, enemies, game):
        pass


class MainMenuState(GameState):
    logger = logging.getLogger("MainMenuScene")

    def __init__(self, game):
        self.game = game
        self.scene = MainMenuScene(self.game)

    def main_menu(self, game):
        self.logger.info("Already in the main menu.")

    def go_guild(self, game):
        return GuildState(game)

    def go_bloodheim(self, game):
        return BloodheimState(game)

    def start_fight(self, hero, enemies, game):
        self.logger.info("Cannot get into the fight form the menu.")


class GuildState(GameState):
    logger = logging.getLogger("GuildState")

    def __init__(self, game):
        self.game = game
        self.scene = GuildScene(self.game)

    def main_menu(self, game):
        return MainMenuState()

    def go_guild(self, game):
        self.logger.info("Already in the Guild.")

    def go_bloodheim(self, game):
        return BloodheimState()

    def start_fight(self, hero, enemies, game):
        self.logger.info("Cannot get into the fight directly from the Guild.")


class BloodheimState(GameState):
    logger = logging.getLogger("BloodheimState")

    def __init__(self, game):
        self.game = game
        self.scene = None

    def main_menu(self, game):
        return MainMenuState(game)

    def go_guild(self, game):
        return GuildState(game)

    def go_bloodheim(self, game):
        self.logger.info("Already in the bloodheim.")

    def start_fight(self, hero, enemies, game):
        self.logger.info("Starting the fight...")
        self.logger.info(f"    - Hero: {hero}")
        self.logger.info(f"    - Enemies: {enemies}")
        FightState(hero, enemies, game)


class FightState(GameState):
    logger = logging.getLogger("FightState")

    def __init__(self, hero, enemies, game):
        self.game = game
        self.scene = None

        self.hero = hero
        self.enemies = enemies

    def main_menu(self, game):
        self.logger.info("Cannot leave the fight.")

    def go_guild(self, game):
        self.logger.info("Cannot leave the fight.")

    def go_bloodheim(self, game):
        BloodheimState()

    def start_fight(self, hero, enemies, game):
        self.logger.info("Already in the fight.")
