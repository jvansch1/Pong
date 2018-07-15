import sys, pygame

class Paddle():

    def __init__(self, screen):
        self.screen = screen


    def draw_paddle(self, x, y):
        surface = pygame.Surface((20, 100))
        surface.fill((255, 255, 255))
        self.screen.add_with_blit(surface, x, y)