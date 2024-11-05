import pygame


# Image is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Image(pygame.sprite.Sprite):

    # Default button images/pygame.Surfaces.
    DEFAULT_IMAGE = pygame.Surface((32, 32))
    DEFAULT_IMAGE.fill(pygame.Color("red"))

    def __init__(
        self,
        pos: pygame.Vector2,
        size: pygame.Vector2 = None,
        image: pygame.Surface = None,
    ):
        super().__init__()

        self.image = image if image else self.DEFAULT_IMAGE

        # Scale the images to the desired size (doesn't modify the originals).
        if size:
            self.image = pygame.transform.scale(self.image, size)

        self.size = pygame.Vector2(self.image.get_size())
        self.pos = pos
        self.rect = self.image.get_rect(center=pos)
