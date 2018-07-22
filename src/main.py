import pygame
from src.game import Game

def main():
    pygame.init()
    pygame.font.init()

    width = 1000
    height = 800

    game = Game(width, height)
    game.run()

main()