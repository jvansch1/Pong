from screen import Screen
from ball import Ball
from paddle import Paddle
import sys, pygame

class Game:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.count_down_value = 3

    def handle_key_presses(self, paddle_one, paddle_two):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            paddle_one.decrement_paddle_y()
        elif keys[pygame.K_DOWN]:
            paddle_one.incriment_paddle_y()

        if keys[pygame.K_w]:
            paddle_two.decrement_paddle_y()
        elif keys[pygame.K_s]:
            paddle_two.incriment_paddle_y()

    def run(self):
        entities = self.create_entities()
        paddle_one = entities["paddle_one"]
        paddle_two = entities["paddle_two"]
        ball = entities["ball"]
        count_down_font = entities["count_down_font"]

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            self.handle_key_presses(paddle_one, paddle_two)

            self.game_loop(entities)
            scored = ball.check_out_of_bounds()

            if scored:
                ball.reset_speed()

                if scored == 1:
                    entities["player_one_score"] += 1
                elif scored == 2:
                    entities["player_two_score"] += 1

            pygame.display.update()

            # Place after update so ball can be reset to center and then pause
            if scored:
                original_x_delta = ball.ball_x_delta
                ball.ball_x_delta = 0
                ball.ball_y_delta = 0

                while self.count_down_value > 0:
                    self.handle_point_scored(entities, count_down_font, self.get_width(), self.get_height(), self.count_down_value)
                    self.count_down_value -= 1

                self.count_down_value = 3

                if original_x_delta > 0:
                    ball.ball_x_delta = -15
                else:
                    ball.ball_x_delta = 15

                ball.ball_y_delta = 15

    def game_loop(self, entity_dict):
        self.render_surfaces(entity_dict["screen"], entity_dict["paddle_one"], entity_dict["paddle_two"],
                        entity_dict["ball"], entity_dict["mid_line"], entity_dict["width"])
        self.render_scores(entity_dict["screen"], entity_dict["player_one_score"], entity_dict["player_two_score"])
        self.check_for_collision(entity_dict["paddle_one"], entity_dict["paddle_two"], entity_dict["ball"])

    def render_surfaces(self, screen, paddle_one, paddle_two, ball, mid_line, width):
        screen.fill_screen((0, 0, 0))
        screen.add_with_blit(mid_line, width / 2, 0)
        paddle_one.draw_paddle()
        paddle_two.draw_paddle()
        ball.draw_ball()

    def render_scores(self, screen, player_one_score, player_two_score):
        score_font = pygame.font.SysFont("Comic Sans MS", 30)

        player_one_score_surface = score_font.render("{player_one_score}".format(player_one_score=player_one_score),
                                                     False, (255, 255, 255))
        player_two_score_surface = score_font.render("{player_two_score}".format(player_two_score=player_two_score),
                                                     False, (255, 255, 255))

        screen.add_with_blit(player_one_score_surface, 10, 10)
        screen.add_with_blit(player_two_score_surface, 975, 10)

    def check_for_collision(self, paddle_one, paddle_two, ball):
        ball_x = ball.x_value()
        ball_y = ball.y_value()

        if paddle_one.check_for_collision(ball_x, ball_y, "paddle_one",
                                          ball.ball_x_delta) or paddle_two.check_for_collision(ball_x, ball_y,
                                                                                               "paddle_two",
                                                                                               ball.ball_x_delta):
            ball.invert_x_delta()
            ball.increase_speed()

    def handle_point_scored(self, entities, count_down_font, width, height, count_down_value):
        self.render_surfaces(entities["screen"], entities["paddle_one"], entities["paddle_two"], entities["ball"],
                        entities["mid_line"], entities["width"])
        self.render_scores(entities["screen"], entities["player_one_score"], entities["player_two_score"])
        count_down_surface = self.render_countdown(count_down_font, count_down_value)
        entities["screen"].add_with_blit(count_down_surface, width / 2, height / 2)
        pygame.display.update()
        pygame.time.delay(1000)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def render_countdown(self, font, value):
        return font.render(
            "{count_down_value}".format(count_down_value=value),
            False, (255, 255, 255))

    def create_entities(self):
        screen = Screen(self.get_width(), self.get_height())
        screen.fill_screen((0, 0, 0))

        mid_line = pygame.Surface((5, self.get_height()))
        mid_line.fill((255, 255, 255))

        count_down_font = pygame.font.SysFont("Comic Sans MS", 100)
        player_one_score = 0
        player_two_score = 0

        screen = Screen(self.get_width(), self.get_height())
        screen.fill_screen((0, 0, 0))

        mid_line = pygame.Surface((5, self.get_height()))
        mid_line.fill((255, 255, 255))

        ball = Ball(screen.screen, 10)

        paddle_one = Paddle(screen, 20, 50)
        paddle_two = Paddle(screen, 960, 50)

        entities = {
            "screen": screen,
            "paddle_one": paddle_one,
            "paddle_two": paddle_two,
            "ball": ball,
            "player_one_score": player_one_score,
            "player_two_score": player_two_score,
            "mid_line": mid_line,
            "width": self.get_width(),
            "height": self.get_height(),
            "count_down_font": count_down_font
        }

        return entities






