import sys, pygame
from screen import Screen
from ball import Ball
from paddle import Paddle

def game_loop(entity_dict):
    render_surfaces(entity_dict["screen"], entity_dict["paddle_one"], entity_dict["paddle_two"], entity_dict["ball"], entity_dict["mid_line"], entity_dict["width"])
    render_scores(entity_dict["screen"], entity_dict["player_one_score"], entity_dict["player_two_score"])
    check_for_collision(entity_dict["paddle_one"], entity_dict["paddle_two"], entity_dict["ball"])

def render_scores(screen, player_one_score, player_two_score):
    score_font = pygame.font.SysFont("Comic Sans MS", 30)

    player_one_score_surface = score_font.render("{player_one_score}".format(player_one_score=player_one_score),
                                                 False, (255, 255, 255))
    player_two_score_surface = score_font.render("{player_two_score}".format(player_two_score=player_two_score),
                                                 False, (255, 255, 255))

    screen.add_with_blit(player_one_score_surface, 10, 10)
    screen.add_with_blit(player_two_score_surface, 975, 10)

def render_surfaces(screen, paddle_one, paddle_two, ball, mid_line, width):
    screen.fill_screen((0,0,0))
    screen.add_with_blit(mid_line, width / 2, 0)
    paddle_one.draw_paddle()
    paddle_two.draw_paddle()
    ball.draw_ball()

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
    pygame.init()
    pygame.font.init()

    count_down_font = pygame.font.SysFont("Comic Sans MS", 30)
    player_one_score = 0
    player_two_score = 0

    count_down = True
    count_down_value = 3

    screen = Screen(width, height)
    screen.fill_screen((0, 0, 0))

    mid_line = pygame.Surface((5, height))
    mid_line.fill((255, 255, 255))

    ball = Ball(screen.screen, 10)

    paddle_one = Paddle(screen, 100, 50)
    paddle_two = Paddle(screen, 900, 50)

    entities = {
        "screen": screen,
        "paddle_one": paddle_one,
        "paddle_two": paddle_two,
        "ball": ball,
        "player_one_score": player_one_score,
        "player_two_score": player_two_score,
        "mid_line": mid_line,
        "width": width,
        "height": height
    }

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        handle_key_presses(paddle_one, paddle_two)

        game_loop(entities)
        scored = ball.check_out_of_bounds()

        if scored == 1:
            player_one_score += 1
        elif scored == 2:
            player_two_score += 1

        pygame.display.update()

        # Place after update so ball can be reset to center and then pause
        # if scored:
            # pygame.time.delay(1000)


main()