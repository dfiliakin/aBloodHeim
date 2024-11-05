import logging
from typing import TYPE_CHECKING, Optional

import pygame

from config import DEFAULT_FONT, DEFAULT_TEXT_COLOR
from toolbox.ui.button import Button
from toolbox.utils.patterns import cached

if TYPE_CHECKING:
    from toolbox.scene import Scene
    from toolbox.ui.image import Image


class Window:

    logger = logging.getLogger("Scene")

    def __init__(
        self,
        scene: "Scene",
        background: "Image",
        name: Optional[str] = None,
        name_font: Optional[pygame.font.Font] = None,
        name_color: Optional[pygame.color.Color] = None,
    ):
        self.all_sprites = pygame.sprite.Group()
        self.all_buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()

        self.background = background

        self.name = name
        if self.name:
            name_font = name_font if name_font else DEFAULT_FONT
            name_color = name_color if name_color else DEFAULT_TEXT_COLOR
            self._set_name(name_font, name_color)

        self.all_sprites.add(self.background)

        # Contains all sprites. Also put the button sprites into a separate group.
        self.close_button = self._make_close_button()
        self.all_buttons.add(self.close_button)
        self.all_sprites.add(self.close_button)

        self.scene = scene
        self.logger.info(f"Opening '{self.scene.NAME}'s pop-up window '{self.name}'...")

        self._active = False

    def _set_name(
        self, name_font: pygame.font.Font, name_color: pygame.color.Color
    ) -> None:
        """Adds name to a background image."""

        # To center the text rect.
        image_center = self.background.image.get_rect().center
        text_surf = name_font.render(self.name, True, name_color)
        text_rect = text_surf.get_rect(center=image_center)

        # Blit the text onto the base_image.
        self.background.image.blit(text_surf, text_rect)

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value):
        self.logger.debug(f"Setting Window.active to {value}")
        self._active = bool(value)

    @property
    @cached()
    def center(self):
        return self.background.pos

    @property
    @cached()
    def top_center(self):
        x = self.background.pos.x
        y = self.background.pos.y - self.background.size.y // 2
        return pygame.Vector2(x, y)

    @property
    @cached()
    def top_right_corner(self):
        x = self.center.x + self.background.size.x // 2
        y = self.center.y - self.background.size.y // 2
        return pygame.Vector2(x, y)

    def update(self, dt):
        super().update()
        self.all_sprites.update(dt)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.active = False

            for button in self.all_buttons:
                button.handle_event(event)

    def draw(self, screen):
        self.all_sprites.draw(screen)

    def activate(self):
        """Callback method to open the window."""
        self.active = True

    def deactivate(self):
        """Callback method to close the window."""
        self.active = False

    def _make_close_button(self):
        quit_button_size = pygame.Vector2(30, 30)
        return Button(
            pos=self.top_right_corner,
            size=quit_button_size,
            callback=self.deactivate,
            text="x",
        )
