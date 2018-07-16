import sys, pygame

class Paddle():

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y


    def draw_paddle(self):
        surface = pygame.Surface((20, 100))
        surface.fill((255, 255, 255))
        self.screen.add_with_blit(surface, self.x, self.y)

    def decrement_paddle_y(self):
        self.y -= 20

    def incriment_paddle_y(self):
        self.y += 20