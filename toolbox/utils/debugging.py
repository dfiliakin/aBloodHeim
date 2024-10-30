import logging
import pygame


logger = logging.getLogger("Degugging")


def create_test_button(pos, callback):
    from ..ui.button.button import Button

    logger.debug("Making test button...")
    new_game_button_size = pygame.Vector2(100, 100)
    return Button(
        pos=pos,
        size=new_game_button_size,
        callback=callback,
        text="TEST",
    )
