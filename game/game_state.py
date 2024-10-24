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

    def __init__(self, screen):
        self.screen = screen
        self.scene = MainMenuScene(self.screen)

    def main_menu(self, screen):
        logging.info("Already in the main menu.")

    def locust_guild(self, screen):
        logging.info("Loading the 'Locust Guild' state.")
        return LocustGuildState(screen)

    def bloodheim(self, screen):
        logging.info("Loading the 'Bloodheim' state.")
        return BloodheimState(screen)

    def fight(self, hero, enemies, screen):
        logging.info("Cannot get into the fight form the menu.")


class LocustGuildState(GameState):

    def __init__(self, screen):
        self.screen = screen
        self.scene = LocustGuildScene(self.screen)

    def main_menu(self, screen):
        logging.info("Loading the main menu.")
        return MainMenuState()

    def locust_guild(self, screen):
        logging.info("Already in the locust guild.")

    def bloodheim(self, screen):
        logging.info("Loading the 'Bloodheim' state.")
        return BloodheimState()

    def fight(self, hero, enemies, screen):
        logging.info("Cannot get into the fight directly from the locust guild.")


class BloodheimState(GameState):

    def __init__(self, screen):
        self.screen = screen
        self.scene = None

    def main_menu(self, screen):
        logging.info("Loading the main menu.")
        return MainMenuState(screen)

    def locust_guild(self, screen):
        logging.info("Loading the 'Locust Guild' state.")
        return LocustGuildState(screen)

    def bloodheim(self, screen):
        logging.info("Already in the bloodheim.")

    def fight(self, hero, enemies, screen):
        logging.info("Starting the fight...")
        logging.info(f"    - Hero: {hero}")
        logging.info(f"    - Enemies: {enemies}")
        FightState(hero, enemies, screen)


class FightState(GameState):

    def __init__(self, hero, enemies, screen):
        self.screen = screen
        self.scene = None

        self.hero = hero
        self.enemies = enemies

    def main_menu(self, screen):
        logging.info("Cannot leave the fight.")

    def locust_guild(self, screen):
        logging.info("Cannot leave the fight.")

    def bloodheim(self, screen):
        logging.info("The fight is over. Getting back to the Bloodheim.")
        BloodheimState()

    def fight(self, hero, enemies, screen):
        logging.info("Already in the fight.")
