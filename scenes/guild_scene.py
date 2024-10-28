from game.game import Game
from toolbox.ui.image.image import Image
from toolbox.ui.textbox.textbox import Textbox
from .quitable_scene import QuitableScene
from toolbox.ui.button import Button
import logging
import pygame
from config import SPRITES_FOLDER
from pathlib import Path

from objects.guild import Guild


class GuildScene(QuitableScene):
    NAME = "Guild"
    logger = logging.getLogger("GuildScene")

    INDICATOR_SCALE = 0.2

    def __init__(self, game: Game):
        super().__init__(game)

        # The Guild
        guild_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "guild_sprite.png")
        ).convert_alpha()

        guild_size = pygame.Vector2(guild_image.get_size())
        guild_offset = (20 + guild_size.x // 2, -20 - guild_size.y // 2)
        self.guild_sprite = Image(
            image=pygame.image.load(
                Path.joinpath(SPRITES_FOLDER, "guild_sprite.png")
            ).convert_alpha(),
            pos=self.screen_bottom_left_corner + guild_offset,
        )

        indicators_center_pos = self.guild_sprite.pos + (
            guild_size.x // 5 - 30,
            -guild_size.y // 5,
        )

        # Gold (on the left)
        gold_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "gold_sprite.png")
        ).convert_alpha()
        gold_size = pygame.Vector2(gold_image.get_size()) * self.INDICATOR_SCALE
        gold_offset = pygame.Vector2(-200, 0)
        self.gold_indicator_sprite = Textbox(
            image=gold_image,
            pos=indicators_center_pos + gold_offset,
            size=gold_size,
            text=game.guild.resources.GOLD,
        )

        # Mana (on top)
        mana_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "mana_sprite.png")
        ).convert_alpha()
        mana_size = pygame.Vector2(mana_image.get_size()) * self.INDICATOR_SCALE
        mana_offset = pygame.Vector2(0, -150)
        self.mana_indicator_sprite = Textbox(
            image=mana_image,
            pos=indicators_center_pos + mana_offset,
            size=mana_size,
            text=game.guild.resources.MANA,
        )

        # Materials (on the right)
        materials_image = pygame.image.load(
            Path.joinpath(SPRITES_FOLDER, "materials_sprite.png")
        ).convert_alpha()
        materials_size = (
            pygame.Vector2(materials_image.get_size()) * self.INDICATOR_SCALE
        )
        materials_offset = pygame.Vector2(200, 0)
        self.materials_indicator_sprite = Textbox(
            image=materials_image,
            pos=indicators_center_pos + materials_offset,
            size=materials_size,
            text=game.guild.resources.MATERIALS,
        )

        # Add the button sprites to the sprite group and button group.
        self.all_buttons.add()
        self.all_sprites.add(
            self.guild_sprite,
            self.gold_indicator_sprite,
            self.mana_indicator_sprite,
            self.materials_indicator_sprite,
        )
