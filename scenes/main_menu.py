from toolbox.button.button import Button
from toolbox.scene import Scene
import logging
import pygame
from config import SPRITES_FOLDER
from pathlib import Path


class MainMenuScene(Scene):
    NAME = "Main Menu"

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        quit_button_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "quit_button.png")
        ).convert_alpha()
        quit_button_size = pygame.Vector2(50, 50)
        self.quit_button = Button(
            pos=self.top_right_corner
            + pygame.Vector2(-10, 10)
            + pygame.Vector2(-quit_button_size.x, quit_button_size.y),
            size=quit_button_size,
            callback=self.quit_game,
            image=quit_button_image,
        )

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add(self.quit_button)
        self.all_sprites.add(self.quit_button)

    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True
