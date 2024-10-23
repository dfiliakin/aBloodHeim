from toolbox.scene import Scene
import logging


class MainMenuScene(Scene):
    NAME = "Main Menu"

    @classmethod
    def load(cls):
        logging.info(f"Loading {cls.NAME}")
        return cls()
