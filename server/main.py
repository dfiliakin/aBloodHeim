import pygame

pygame.init()

import logging

from game import Game

logging.basicConfig(level=logging.DEBUG)

screen = pygame.display.set_mode((800, 600))


def main():
    Game(screen)
    pygame.quit()


if __name__ == "__main__":
    main()
