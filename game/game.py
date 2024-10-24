import logging

from scenes import MainMenuScene


class Game:

    def __init__(self, screen):
        main_menu = MainMenuScene(screen)
        main_menu.run()
