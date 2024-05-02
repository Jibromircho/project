import pygame.font
from pygame.sprite import Group

from ball import Ball

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, pongle):
        """Initialize scorekeeping attributes"""
        self.pongle = pongle
        self.screen = pongle.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pongle.settings
        self.stats = pongle.stats
#        self.prep_balls()

        #font setting for the score
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prepere initial scoring image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turning the score into an image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_img = self.font.render(score_str, True,self.text_colour, self.settings.bg_colour)

        #display the score at top right corner
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 5
        self.score_rect.top = 10

    def prep_high_score(self):
        """Turning highscore into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"Highscore: {high_score:,}"
        self.high_score_img = self.font.render(high_score_str, True,
                self.text_colour,self.settings.bg_colour)
        #center the high score
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn level into img"""
        level_str =  "Level: " + str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_colour,self.settings.bg_colour)
        #position level below the score
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5


    def show_score(self):
        """Draw score on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img,self.level_rect)
        for ball in self.balls.sprites():
            ball.draw_ball()


    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open("highscore.txt","w") as hfile:
                hfile.write(str(self.stats.high_score))
            self.prep_high_score()


    def prep_balls(self):
        """Show how many lives the player has on the left"""
        self.balls = Group()
        for ball_number in range(self.stats.lives):
            ball = Ball(self.pongle)
            ball.rect.x = 12 + ball_number * (ball.rect.width * 1.5)
            ball.rect.y = 12
            self.balls.add(ball)
