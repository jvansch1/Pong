import sys, pygame

class Ball():

    def __init__(self, surface, radius):
        self.radius = radius
        self.surface = surface
        self.x = 500
        self.y = 400
        self.ball_x_delta = 15
        self.ball_y_delta = 15


    def draw_ball(self):
        self.handle_x_pos()
        self.handle_y_pos()
        pygame.draw.circle(self.surface, (255,255,255), (self.x, self.y), 10)

    def handle_x_pos(self):
        self.x += self.ball_x_delta

    def check_out_of_bounds(self):
        # will return the number of the player who has scored
        if self.x > 1000:
            self.x = 500
            self.y = 400
            self.draw_ball()
            return 1
        elif self.x < -10:
            self.x = 500
            self.y = 400
            self.draw_ball()
            return 2


    def handle_y_pos(self):
        if self.y > (780):
            self.ball_y_delta = -15

        if self.y < 20:
            self.ball_y_delta += 15

        self.y += self.ball_y_delta

    def y_value(self):
        return self.y

    def x_value(self):
        return self.x

    def invert_x_delta(self):
        self.ball_x_delta = -self.ball_x_delta

    def incriment_x_delta(self):
        if self.ball_x_delta > 0:
            self.ball_x_delta += 1
        else:
            self.ball_x_delta -= 1

    def incriment_y_delta(self):
        if self.ball_y_delta > 0:
            self.ball_y_delta += 1
        else:
            self.ball_x_delta -= 1

    def increase_speed(self):
        self.incriment_x_delta()
        self.incriment_y_delta()

    def reset_speed(self):
        self.ball_x_delta = 15
        self.ball_y_delta = 15