import sys, pygame
from screen import Screen
from ball import Ball
from paddle import Paddle

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

    ball_x = int(width / 2)
    ball_y = int(height / 2)
    ball_x_delta = 20
    ball_y_delta = 15

    ball = Ball(screen.screen, 10)

    paddle_one = Paddle(screen, 20, paddle_one_y)
    paddle_two = Paddle(screen, 960, paddle_two_y)

    screen.add_with_blit(surface, width / 2, 0)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        handle_key_presses(paddle_one, paddle_two)

        screen.fill_screen(black)
        paddle_one.draw_paddle()
        paddle_two.draw_paddle()
        screen.add_with_blit(surface, width / 2, 0)
        ball_x += ball_x_delta
        ball_y += ball_y_delta

        if ball_x > (width - 20):
            ball_x_delta = -20

        if ball_x < 20:
            ball_x_delta = 20

        if ball_y > (height - 20):
            ball_y_delta = -15

        if ball_y < 20:
            ball_y_delta = 15

        ball.draw_ball(ball_x, ball_y)
        pygame.display.update()

main()