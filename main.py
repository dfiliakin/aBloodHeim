import pygame

pygame.init()

import logging

from game import Game

logging.basicConfig(level=logging.INFO)

screen = pygame.display.set_mode((800, 600))


def main():
    pygame.init()

    Game(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
