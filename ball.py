import sys, pygame

class Ball():

    def __init__(self, surface, radius):
        self.radius = radius
        self.surface = surface

    def draw_ball(self, x, y):
        pygame.draw.circle(self.surface, (255,255,255), (x, y), 10)