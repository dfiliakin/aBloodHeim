import pygame

pygame.init()

import logging

from game import Game

logging.basicConfig(level=logging.DEBUG)

screen = pygame.display.set_mode((800, 600))


def main():
    the_game = Game(screen)
    the_game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
