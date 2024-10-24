import collections
import pygame
from config import DEFAULT_FONT
from toolbox.utils.drawing import hue_image


# Button is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Button(pygame.sprite.Sprite):

    # Default button images/pygame.Surfaces.
    DEFAULT_IMAGE = pygame.Surface((100, 32))
    DEFAULT_IMAGE.fill(pygame.Color("dodgerblue1"))

    def __init__(
        self,
        pos: pygame.Vector2,
        size: pygame.Vector2,
        callback: collections.abc.Callable,
        font=DEFAULT_FONT,
        text=None,
        text_color=(0, 0, 0),
        image=None,
    ):
        super().__init__()
        # Scale the images to the desired size (doesn't modify the originals).
        self.image_normal = image if image else self.DEFAULT_IMAGE
        self.image_normal = pygame.transform.scale(self.image_normal, size)

        # lighter image
        self.image_hover = hue_image(
            image=self.image_normal,
            color=(255, 255, 255, 100),
        )

        # darker image
        self.image_down = hue_image(
            image=self.image_normal,
            color=(0, 0, 0, 100),
        )

        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect(center=pos)

        if text:
            # To center the text rect.
            image_center = self.image.get_rect().center
            text_surf = font.render(text, True, text_color)
            text_rect = text_surf.get_rect(center=image_center)

            # Blit the text onto the images.
            for image in (self.image_normal, self.image_hover, self.image_down):
                image.blit(text_surf, text_rect)

        # This function will be called when the button gets pressed.
        self.callback = callback
        self.button_down = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            # If the rect collides with the mouse pos.
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()  # Call the function.
                self.image = self.image_hover
            self.button_down = False

        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal
