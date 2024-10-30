import logging
from typing import Optional
import pygame
from config import DEFAULT_FONT
from ..image.image import Image


# Textbox is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Textbox(Image):
    logger = logging.getLogger("Textbox")

    # Default button images/pygame.Surfaces.
    DEFAULT_IMAGE = pygame.Surface((200, 100))

    def __init__(
        self,
        font=DEFAULT_FONT,
        text: str = None,
        text_color=(0, 0, 0),
        text_offset: Optional[pygame.Vector2] = None,
        image: Optional[pygame.Surface] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            image=image if image else self.DEFAULT_IMAGE,
            *args,
            **kwargs,
        )

        self._text = None
        self._base_image = self.image.copy()

        self.font = font
        self.text_color = text_color
        self.text_offset = text_offset if text_offset else pygame.Vector2(0, 0)

        if text:
            self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self.logger.debug(f"Setting Textbox.text to {value}")
        self._text = str(value)

        # To center the text rect.
        image_center = self._base_image.get_rect().center
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=image_center + self.text_offset)

        # Blit the text onto the base_image.
        self.image = self._base_image.copy()
        self.image.blit(text_surf, text_rect)

    @text.deleter
    def text(self):
        del self.text
        self.image = self._base_image.copy()
