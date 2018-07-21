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
        if self.y <= 0:
            pass
        else:
            self.y -= 25

    def incriment_paddle_y(self):
        if self.y >= self.screen.height - 100:
            pass
        else:
            self.y += 25

    def y_value(self):
        return self.y

    def x_value(self):
        return self.x

    def check_for_collision(self, ball_x, ball_y, paddle, ball_x_delta):
        if (paddle == "paddle_one" and (ball_x <= self.x + 20  + (-ball_x_delta / 2)) and (ball_y <= self.y + 100 and ball_y >= self.y)):
            return True
        elif (paddle == "paddle_two" and (ball_x >= self.x - (ball_x_delta / 2)) and (ball_y < self.y + 100 and ball_y >= self.y)):
            return True

