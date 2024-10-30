from game.game import Game
from toolbox.ui.image.image import Image
from toolbox.ui.textbox.textbox import Textbox
from toolbox.utils.debugging import create_test_button
from .quitable_scene import QuitableScene
import logging
import pygame
from config import SPRITES_FOLDER
from pathlib import Path


class GuildScene(QuitableScene):
    NAME = "Guild"
    logger = logging.getLogger("GuildScene")

    INDICATOR_SCALE = 0.2

    def __init__(self, game: Game):
        super().__init__(game)

        # GUILD
        self.guild_sprite = self._create_guild_sprite()
        self.all_sprites.add(self.guild_sprite)

        indicators_center_pos = self.guild_sprite.pos + (
            self.guild_sprite.size.x // 5 - 30,
            -self.guild_sprite.size.y // 5,
        )

        # GOLD, MANA, MATERIALS indicators
        self._create_indicators(indicators_center_pos)
        self.all_sprites.add(
            self.gold_indicator, self.mana_indicator, self.materials_indicator
        )

        self.test_button = create_test_button(
            pos=self.screen_center,
            callback=self._test,
        )

        self.all_buttons.add(self.test_button)
        self.all_sprites.add(self.test_button)

    def _test(self):
        self.game.guild.resources.gold += 1
        self.gold_indicator.text = self.game.guild.resources.gold
        self.logger.debug(f"New Gold: {self.game.guild.resources.gold}")

    def _create_guild_sprite(self) -> Image:
        guild_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "guild_sprite.png")
        ).convert_alpha()

        guild_size = pygame.Vector2(guild_image.get_size())
        guild_offset = (20 + guild_size.x // 2, -20 - guild_size.y // 2)
        guild_sprite = Image(
            image=pygame.image.load(
                Path.joinpath(SPRITES_FOLDER, "guild_sprite.png")
            ).convert_alpha(),
            pos=self.screen_bottom_left_corner + guild_offset,
        )

        return guild_sprite

    def _create_indicators(self, indicators_center_pos) -> list[Image]:
        # Gold (on the left)
        self.gold_indicator = self._create_indicator(
            filepath="gold_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(-200, 0),
        )
        self.gold_indicator.text = self.game.guild.resources.gold

        # Mana (on top)
        self.mana_indicator = self._create_indicator(
            filepath="mana_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(0, -150),
        )
        self.mana_indicator.text = self.game.guild.resources.mana

        # Materials (on the right)
        self.materials_indicator = self._create_indicator(
            filepath="materials_sprite.png",
            indicators_center_pos=indicators_center_pos,
            offset=pygame.Vector2(200, 0),
        )
        self.materials_indicator.text = self.game.guild.resources.materials

    def _create_indicator(self, filepath, indicators_center_pos, offset):
        image_png = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, filepath)
        ).convert_alpha()
        indicator_sprite = Textbox(
            image=image_png,
            pos=indicators_center_pos + offset,
            size=pygame.Vector2(image_png.get_size()) * self.INDICATOR_SCALE,
        )

        return indicator_sprite
