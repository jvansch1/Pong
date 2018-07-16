import sys, pygame

class Ball():

    def __init__(self, surface, radius):
        self.radius = radius
        self.surface = surface
        self.x = 500
        self.y = 500
        self.ball_x_delta = 20
        self.ball_y_delta = 20


    def draw_ball(self):
        self.handle_x_pos()
        self.handle_y_pos()
        pygame.draw.circle(self.surface, (255,255,255), (self.x, self.y), 10)

    def handle_x_pos(self):
        if self.x > (980):
            self.ball_x_delta = -20

        if self.x < 20:
            self.ball_x_delta += 20

        self.x += self.ball_x_delta

    def handle_y_pos(self):
        if self.y > (780):
            self.ball_y_delta = -20

        if self.y < 20:
            self.ball_y_delta += 20

        self.y += self.ball_y_delta

    def y_value(self):
        return self.y

    def x_value(self):
        return self.x

    def invert_x_delta(self):
        self.ball_x_delta = -self.ball_x_delta