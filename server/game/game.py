import logging

from .game_state import MainMenuState
from scenes.constants import Action


class Game:
    logger = logging.getLogger("Game")

    def __init__(self, screen):
        self.current_state = MainMenuState(screen)

        while True:
            self.logger.info("=" * 50)
            end_scene_status = self.current_state.run()
            self.logger.info(end_scene_status)

            if not end_scene_status.success:
                self.logger.error(end_scene_status.msg)
                break

            if end_scene_status.action == Action.QUIT_GAME:
                break

            if end_scene_status.action == Action.NEW_GAME:
                self.locust_guild(screen)

            else:
                self.logger.error(f"Unexpected action: {end_scene_status.action}")

    def main_menu(self, screen):
        self.logger.debug("main_menu")
        self.current_state = self.current_state.main_menu(screen)

    def locust_guild(self, screen):
        self.logger.debug("locust_guild")
        self.current_state = self.current_state.locust_guild(screen)

    def bloodheim(self, screen):
        self.logger.debug("bloodheim")
        self.current_state = self.current_state.bloodheim(screen)

    def fight(self, hero, enemies, screen):
        self.logger.debug("fight")
        self.current_state = self.current_state.fight(hero, enemies, screen)
