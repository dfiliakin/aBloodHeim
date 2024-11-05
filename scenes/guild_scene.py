import logging
from pathlib import Path

import pygame

from config import SPRITES_FOLDER
from game.game import Game
from toolbox.ui.button import Button
from toolbox.ui.image import Image
from toolbox.ui.textbox import Textbox
from toolbox.ui.window.window import Window
from toolbox.utils.debugging import create_test_button

from .quitable_scene import QuitableScene


class GuildScene(QuitableScene):
    NAME = "Guild"
    logger = logging.getLogger("GuildScene")

    INDICATOR_SCALE = 0.2
    SPACING = 20  # px

    def __init__(self, game: Game):
        super().__init__(game)

        # TITLE
        self._make_guild_title_sprite()
        self.all_sprites.add(self.guild_title_sprite)

        # GUILD
        self._make_guild_sprite()
        self.all_sprites.add(self.guild_sprite)

        indicators_center_pos = self.guild_sprite.pos + (
            self.guild_sprite.size.x // 5 - 30,
            -self.guild_sprite.size.y // 5,
        )

        # GOLD, MANA, MATERIALS indicators
        self._make_indicators(indicators_center_pos)
        self.all_sprites.add(
            self.gold_indicator, self.mana_indicator, self.materials_indicator
        )

        # TEST button
        # self.test_button = create_test_button(
        #     pos=self.screen_center,
        #     callback=self._test,
        # )

        # self.all_buttons.add(self.test_button)
        # self.all_sprites.add(self.test_button)

        # MARKET, HIRE, STORAGE Windows
        self._make_windows()
        self.all_windows.extend(
            [self.market_window, self.hire_window, self.storage_window],
        )

        # MARKET, HIRE, STORAGE Buttons
        self._make_buttons()
        self.all_buttons.add(self.market_button, self.hire_button, self.storage_button)
        self.all_sprites.add(self.market_button, self.hire_button, self.storage_button)

    def _test(self):
        self.game.guild.resources.gold += 1
        self.gold_indicator.text = self.game.guild.resources.gold
        self.logger.debug(f"New Gold: {self.game.guild.resources.gold}")

    def _make_guild_title_sprite(self) -> Image:
        guild_title_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "flag_sprite.png")
        ).convert_alpha()

        guild_title_size = pygame.Vector2(600, 300)
        guild_title_offset = (
            20 + guild_title_size.x // 2,
            20 + guild_title_size.y // 2,
        )
        self.guild_title_sprite = Textbox(
            image=guild_title_image,
            size=guild_title_size,
            pos=self.screen_top_left_corner + guild_title_offset,
            text=self.game.guild.name,
            text_offset=pygame.Vector2(0, -50),
            font=pygame.font.SysFont("Comic Sans MS", 60),
        )

        return self.guild_title_sprite

    def _make_guild_sprite(self) -> Image:
        guild_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "guild_sprite.png")
        ).convert_alpha()

        guild_size = pygame.Vector2(guild_image.get_size())
        guild_offset = (
            self.SPACING + guild_size.x // 2,
            -self.SPACING - guild_size.y // 2,
        )
        self.guild_sprite = Image(
            image=guild_image,
            pos=self.screen_bottom_left_corner + guild_offset,
        )

        return self.guild_sprite

    def _make_indicators(self, indicators_center_pos) -> list[Image]:
        # Gold (on the left)
        self.gold_indicator = self._make_indicator(
            filepath="gold_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(-200, 0),
        )
        self.gold_indicator.text = self.game.guild.resources.gold

        # Mana (on top)
        self.mana_indicator = self._make_indicator(
            filepath="mana_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(0, -150),
        )
        self.mana_indicator.text = self.game.guild.resources.mana

        # Materials (on the right)
        self.materials_indicator = self._make_indicator(
            filepath="materials_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(200, 0),
        )
        self.materials_indicator.text = self.game.guild.resources.materials

    def _make_indicator(self, filepath, indicators_center_pos, offset):
        image_png = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, filepath)
        ).convert_alpha()
        indicator_sprite = Textbox(
            image=image_png,
            pos=indicators_center_pos + offset,
            size=pygame.Vector2(image_png.get_size()) * self.INDICATOR_SCALE,
        )

        return indicator_sprite

    def _make_windows(self):
        """Makes MARKET, HIRE, STORAGE Windows"""

        pop_up_window_pos = self.screen_center + pygame.Vector2(100, -100)

        self.market_window = self._make_pop_up_window("Market", pop_up_window_pos)
        self.hire_window = self._make_pop_up_window("Hire", pop_up_window_pos)
        self.storage_window = self._make_pop_up_window("Storage", pop_up_window_pos)

    def _make_buttons(self):
        """Makes MARKET, HIRE, STORAGE Buttons"""

        button_size = pygame.Vector2(150, 75)

        buttons_center = self.screen_bottom_center + pygame.Vector2(
            0,
            -button_size.y // 2 - self.SPACING,
        )

        button_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "button_sprite.png")
        ).convert_alpha()

        self.market_button = Button(
            image=button_image.copy(),
            pos=buttons_center
            + pygame.Vector2(
                -button_size.x - self.SPACING,
                0,
            ),
            size=button_size,
            callback=self.market_window.activate,
            text="Market",
        )

        self.hire_button = Button(
            image=button_image.copy(),
            pos=buttons_center,
            size=button_size,
            callback=self.hire_window.activate,
            text="Hire",
        )

        self.storage_button = Button(
            image=button_image.copy(),
            pos=buttons_center
            + pygame.Vector2(
                button_size.x + self.SPACING,
                0,
            ),
            size=button_size,
            callback=self.storage_window.activate,
            text="Storage",
        )

    def _button_stab(self):
        self.logger.debug("Button pressed")
        self.test_window.active = True

        self.all_windows.append(self.test_window)
