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
    pygame.font.init()

    score_font = pygame.font.SysFont("Comic Sans MS", 30)
    player_one_score = 0
    player_two_score = 0

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

        # Handle drawing all elements to the screen and detecting collision
        player_one_score_surface = score_font.render("{player_one_score}".format(player_one_score=player_one_score),
                                                     False, (255, 255, 255))
        player_two_score_surface = score_font.render("{player_two_score}".format(player_two_score=player_two_score),
                                                     False, (255, 255, 255))
        screen.fill_screen(black)
        paddle_one.draw_paddle()
        paddle_two.draw_paddle()
        screen.add_with_blit(surface, width / 2, 0)
        screen.add_with_blit(player_one_score_surface, 10, 10)
        screen.add_with_blit(player_two_score_surface, width - 25, 10)
        ball.draw_ball()
        check_for_collision(paddle_one, paddle_two, ball)
        scored = ball.check_out_of_bounds()
        if scored == 1:
            player_one_score += 1
        elif scored == 2:
            player_two_score += 1
        pygame.display.update()

main()