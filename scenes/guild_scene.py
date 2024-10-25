from .quitable_scene import QuitableScene
from toolbox.button.button import Button
from toolbox.scene import Scene
import logging
import pygame
from config import SPRITES_FOLDER
from pathlib import Path

from objects.guild import Guild


class GuildScene(QuitableScene):
    NAME = "Guild"
    logger = logging.getLogger("GuildScene")

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add()
        self.all_sprites.add()
