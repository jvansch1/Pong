import sys, pygame
from screen import Screen
from ball import Ball
from paddle import Paddle

def check_for_collision(paddle_one, paddle_two, ball):
    ball_x = ball.x_value()
    ball_y = ball.y_value()

    if paddle_one.check_for_collision(ball_x, ball_y, "paddle_one") or paddle_two.check_for_collision(ball_x, ball_y, "paddle_two"):
        ball.invert_x_delta()

def handle_key_presses(paddle_one, paddle_two):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        paddle_one.decrement_paddle_y()
    elif keys[pygame.K_DOWN]:
        paddle_one.incriment_paddle_y()

    if keys[pygame.K_w]:
        paddle_two.decrement_paddle_y()
    elif keys[pygame.K_s]:
        paddle_two.incriment_paddle_y()

def main():
    width = 1000
    height = 800
    size = width, height
    pygame.init()
    black = 0,0,0
    white = 255,255,255

    screen = Screen(width, height)
    screen.fill_screen(black)

    surface = pygame.Surface((5, height))
    surface.fill(white)

    ball = Ball(screen.screen, 10)

    paddle_one = Paddle(screen, 100, 50)
    paddle_two = Paddle(screen, 900, 50)

    screen.add_with_blit(surface, width / 2, 0)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        handle_key_presses(paddle_one, paddle_two)

        screen.fill_screen(black)
        paddle_one.draw_paddle()
        paddle_two.draw_paddle()
        screen.add_with_blit(surface, width / 2, 0)

        ball.draw_ball()
        check_for_collision(paddle_one, paddle_two, ball)
        pygame.display.update()

main()