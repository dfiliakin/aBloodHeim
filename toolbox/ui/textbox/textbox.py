import collections
import pygame
from config import DEFAULT_FONT
from ..image.image import Image


# Textbox is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Textbox(Image):

    # Default button images/pygame.Surfaces.
    DEFAULT_IMAGE = pygame.Surface((200, 100))

    def __init__(
        self,
        font=DEFAULT_FONT,
        text=None,
        text_color=(0, 0, 0),
        image=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            image=image if image else self.DEFAULT_IMAGE,
            *args,
            **kwargs,
        )

        if text:
            # To center the text rect.
            image_center = self.image.get_rect().center
            text_surf = font.render(str(text), True, text_color)
            text_rect = text_surf.get_rect(center=image_center)

            # Blit the text onto the images.
            self.image.blit(text_surf, text_rect)
