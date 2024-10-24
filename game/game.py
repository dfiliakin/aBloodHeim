import logging

import pygame

from .game_state import MainMenuState
from scenes.constants import Action


class Game:

    def __init__(self, screen):
        self.current_state = MainMenuState(screen)
        end_scene_status = self.current_state.run()

        while end_scene_status.action != Action.QUIT_GAME:

            logging.info("=" * 30)
            logging.info(end_scene_status)

            if not end_scene_status.success:
                logging.error(end_scene_status.msg)
                break

            if end_scene_status.action == Action.NEW_GAME:
                self.locust_guild(screen)

            else:
                logging.error(f"Unexpected action: {end_scene_status.action}")

            end_scene_status = self.current_state.run()

    def main_menu(self, screen):
        logging.info("Game::main_menu")
        self.current_state = self.current_state.main_menu(screen)

    def locust_guild(self, screen):
        logging.info("Game::locust_guild")
        self.current_state = self.current_state.locust_guild(screen)

    def bloodheim(self, screen):
        logging.info("Game::bloodheim")
        self.current_state = self.current_state.bloodheim(screen)

    def fight(self, hero, enemies, screen):
        logging.info("Game::fight")
        self.current_state = self.current_state.fight(hero, enemies, screen)
