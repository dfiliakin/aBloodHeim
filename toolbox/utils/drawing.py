import pygame


def hue_image(
    image: pygame.Surface,
    color: pygame.Color,
):

    hue_surf = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    hue_surf.fill(color)

    hued_image = image.copy()
    hued_image.blit(hue_surf, (0, 0))

    return hued_image
