import logging

import pygame

from scenes import MainMenuScene
from toolbox.button import Button



class Game:

    SCENES = {
        MainMenuScene.NAME: MainMenuScene,
    }

    def __init__(self, screen):
        self.done = False
        self.clock = pygame.time.Clock()
        self.screen = screen

        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pygame.sprite.Group()
        self.all_buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()

        self.menu_button = Button(
            pos=pygame.Vector2(300, 500),
            size=pygame.Vector2(170, 65),
            callback=MainMenuScene.load,
            text="The",
            text_color=(255, 255, 255),
        )

        self.quit_button = Button(
            pos=pygame.Vector2(320, 240),
            size=pygame.Vector2(170, 65),
            callback=self.quit_game,
            text="Quit",
            text_color=(255, 255, 255),
        )

        # Add the button sprites to the sprite group.
        self.all_buttons.add(self.menu_button, self.quit_button)
        self.all_sprites.add(self.menu_button, self.quit_button)

    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for button in self.all_buttons:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
