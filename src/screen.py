import sys, pygame

class Screen():

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.width, self.height))

    def fill_screen(self, color):
        self.screen.fill(color)

    def add_with_blit(self, surface, x, y):
        self.screen.blit(surface, (x, y))

