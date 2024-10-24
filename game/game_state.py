import logging
from abc import ABC, abstractmethod

from scenes import LocustGuildScene, MainMenuScene
from toolbox.scene import Status as SceneStatus


class GameState(ABC):
    def __init__(self):
        self.screen = None
        self.scene = None

    def run(self) -> SceneStatus:
        return self.scene.run()

    @abstractmethod
    def main_menu(self, screen):
        pass

    @abstractmethod
    def locust_guild(self, screen):
        pass

    @abstractmethod
    def bloodheim(self, screen):
        pass

    @abstractmethod
    def fight(self, hero, enemies, screen):
        pass


class MainMenuState(GameState):
    logger = logging.getLogger("MainMenuScene")

    def __init__(self, screen):
        self.screen = screen
        self.scene = MainMenuScene(self.screen)

    def main_menu(self, screen):
        self.logger.info("Already in the main menu.")

    def locust_guild(self, screen):
        return LocustGuildState(screen)

    def bloodheim(self, screen):
        return BloodheimState(screen)

    def fight(self, hero, enemies, screen):
        self.logger.info("Cannot get into the fight form the menu.")


class LocustGuildState(GameState):
    logger = logging.getLogger("LocustGuildState")

    def __init__(self, screen):
        self.screen = screen
        self.scene = LocustGuildScene(self.screen)

    def main_menu(self, screen):
        return MainMenuState()

    def locust_guild(self, screen):
        self.logger.info("Already in the locust guild.")

    def bloodheim(self, screen):
        return BloodheimState()

    def fight(self, hero, enemies, screen):
        self.logger.info("Cannot get into the fight directly from the locust guild.")


class BloodheimState(GameState):
    logger = logging.getLogger("BloodheimState")

    def __init__(self, screen):
        self.screen = screen
        self.scene = None

    def main_menu(self, screen):
        return MainMenuState(screen)

    def locust_guild(self, screen):
        return LocustGuildState(screen)

    def bloodheim(self, screen):
        self.logger.info("Already in the bloodheim.")

    def fight(self, hero, enemies, screen):
        self.logger.info("Starting the fight...")
        self.logger.info(f"    - Hero: {hero}")
        self.logger.info(f"    - Enemies: {enemies}")
        FightState(hero, enemies, screen)


class FightState(GameState):
    logger = logging.getLogger("FightState")

    def __init__(self, hero, enemies, screen):
        self.screen = screen
        self.scene = None

        self.hero = hero
        self.enemies = enemies

    def main_menu(self, screen):
        self.logger.info("Cannot leave the fight.")

    def locust_guild(self, screen):
        self.logger.info("Cannot leave the fight.")

    def bloodheim(self, screen):
        BloodheimState()

    def fight(self, hero, enemies, screen):
        self.logger.info("Already in the fight.")
