import sys, pygame
from game import Game

def main():
    pygame.init()
    pygame.font.init()

    width = 1000
    height = 800

    game = Game(width, height)
    game.run()

main()