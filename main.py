import sys, pygame
from screen import Screen
from ball import Ball
from paddle import Paddle

def handle_key_presses(paddle_one_y, paddle_two_y):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        paddle_one_y -= 20
    elif keys[pygame.K_DOWN]:
        paddle_one_y += 20

    if keys[pygame.K_w]:
        paddle_two_y -= 20
    elif keys[pygame.K_s]:
        paddle_two_y += 20

    return (paddle_one_y, paddle_two_y)

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
    paddle_one_y = 50
    paddle_two_y = 50

    ball = Ball(screen.screen, 10)

    paddle_one = Paddle(screen)
    paddle_one = Paddle(screen)

    screen.add_with_blit(surface, width / 2, 0)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        paddle_one_y, paddle_two_y = handle_key_presses(paddle_one_y, paddle_two_y)

        screen.fill_screen(black)
        paddle_one.draw_paddle(20, paddle_one_y)
        paddle_one.draw_paddle(960, paddle_two_y)
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

    print("Running")

main()