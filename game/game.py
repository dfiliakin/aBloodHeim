import logging
from typing import TYPE_CHECKING, Optional

import pygame

if TYPE_CHECKING:
    from objects.guild.guild import Guild


class Game:
    logger = logging.getLogger("Game")

    def __init__(self, screen: pygame.Surface):
        # Lazy import to avoid circular import
        from .game_state_manager import GameStateManager

        self.screen = screen
        self.state_manager = GameStateManager(game=self)
        self.guild: Optional["Guild"] = None

    def run(self):
        # Lazy import to avoid circular import
        from scenes.constants import Action

        while True:
            self.logger.info("=" * 50)
            current_scene = self.state_manager.current_state.scene
            self.logger.info(f"Running {current_scene.NAME} ...")

            end_scene_status = current_scene.run()
            self.logger.info(end_scene_status)

            if not end_scene_status.success:
                self.logger.error(end_scene_status.msg)
                break

            if end_scene_status.action == Action.QUIT_GAME:
                self.logger.info(f"Quiting {current_scene.NAME} ...")
                break

            if end_scene_status.action == Action.NEW_GAME:
                self.state_manager.go_guild(game=self)

            else:
                self.logger.error(f"Unexpected action: {end_scene_status.action}")
