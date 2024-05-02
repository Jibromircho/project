import sys
import pygame

from settings import Settings
from player import PlayerBar
from bricks import Bricks
from ball import Ball
from game_stats import GameStats
from game_text import GameText
from scoreboard import Scoreboard

class Pongle:
    """The class for the main game"""

    def __init__(self):
        """Initializing the game and creating recourses and assets"""
        pygame.init()
        #getting the game settings and setting up the game screen and resolution etc.
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_hight = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Pongle")
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.player = PlayerBar(self)
        self.ball = Ball(self)
        self.bricks = pygame.sprite.Group()
        self._spawn_bricks()
        self.play_text = GameText(self, "Press SPACE to launch ball")
        self.game_over = GameText(self, "Game Over")
        self.game_active = True
        #on first game start
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_balls()



    def run_game(self):
        """Main game loop"""
        while True:
            self._check_events()
            if self.game_active:
                self.player.update()
                self._check_ball_bounce()
                self.ball.update(self)
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """Responds to player inputs"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._start_game()
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _start_game(self):
        self.settings.initialize_dynamic_settings()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.settings.ball_moving = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Updates current frame and flips to the next one"""
        self.screen.fill(self.settings.bg_colour)
        self.player.draw_player()
        self.ball.draw_ball()
        self.scoreboard.show_score()
        for brick in self.bricks.sprites():
            brick.draw_brick()
        if not self.settings.ball_moving and self.game_active:
            self.play_text.draw_msg()
        if not self.game_active:
            self.game_over.draw_msg()
        pygame.display.flip()

    def _spawn_bricks(self):
        """Spawns the initial bricks if not at maximum"""
        brick = Bricks(self)
        brick_width, brick_hight = brick.rect.size

        current_x, current_y = 15, 90
        while current_y < (self.settings.screen_hight / 1.9):
            while current_x < (self.settings.screen_width - brick_width):
                self._create_brick(current_x, current_y)
                current_x += 5 + brick_width
            current_x = 15
            current_y += 5 + brick_hight


    def _create_brick(self, position_x, position_y):
        """Creates a brick where it should be"""
        new_brick = Bricks(self)
        new_brick.x, new_brick.y = position_x, position_y
        new_brick.rect.x = position_x
        new_brick.rect.y = position_y
        self.bricks.add(new_brick)

    def _check_ball_bounce(self):
        screen_rect = self.screen.get_rect()
        if self.ball.rect.top <= 0:
            self.settings.ball_speed_y *= -1
        elif self.ball.rect.bottom >= screen_rect.bottom:
            self._ball_lost()
        elif self.ball.rect.left <= 0:
            self.settings.ball_speed_x *= -1
        elif self.ball.rect.right >= screen_rect.right:
            self.settings.ball_speed_x *= -1
        self._check_player_hit()
        self._check_brick_hit()

    def _check_player_hit(self):
        if ((self.ball.rect.colliderect(self.player.rect)) and 
                self.ball.rect.bottom >= self.player.rect.top):
            direction_x = self.ball.rect.centerx - self.player.rect.centerx
            direction_x = round(((direction_x/300) * 10), 2)
            self._ball_speed_adjust(direction_x)

    def _check_brick_hit(self):
        """Chech if the ball hits a brick and at which side"""
        """and adjusts ball movement acordingly"""
        collisisons = pygame.sprite.spritecollide(self.ball, self.bricks, True)         
        if collisisons:
            for brick in collisisons:
                self.stats.score += self.settings.brick_points
                self.scoreboard.prep_score()
                self.scoreboard.check_high_score()
            direction_x = self.ball.rect.centerx - brick.rect.centerx
            direction_y = self.ball.rect.centery - brick.rect.centery
                #change direction acordingly
            if abs(direction_x) < abs(direction_y):
                self.settings.ball_speed_y *= -1
            else:
                self.settings.ball_speed_x *= -1
        if not self.bricks:
            self.ball_moving = False
            self.stats.level += 1
            self.settings.increase_level()
            self._spawn_bricks()
            self.scoreboard.prep_level()
    
    def _ball_speed_adjust(self,direction_x):
        """Checks where exacly on the bar the ball hits and adjusts speed acordingly"""
        if self.settings.ball_speed_x < 0:
            self.settings.ball_speed_x -= (direction_x * -1)
            if self.settings.ball_speed_x < (self.settings.ball_speed_max * -1):
                self.settings.ball_speed_x = (self.settings.ball_speed_max * -1)
        if self.settings.ball_speed_x > 0:
            self.settings.ball_speed_x += direction_x
            if self.settings.ball_speed_x > self.settings.ball_speed_max:
                self.settings.ball_speed_x = self.settings.ball_speed_max
        self.settings.ball_speed_y *= -1
    
    
    def _ball_lost(self):
        if self.stats.lives > 1:
            self.stats.lives -= 1
        else:
            self.stats.lives -= 1
            self.scoreboard.prep_balls()
            self.game_active = False
        self.scoreboard.prep_balls()
        self.settings.ball_moving = False
        pygame.mouse.set_visible(True)




    
if __name__ == '__main__':
    #make game instance and run game
    pongle = Pongle()
    pongle.run_game()

