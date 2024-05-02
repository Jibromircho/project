import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A class for the ball that bounces around"""

    def __init__(self, pongle):
        super().__init__()
        self.screen = pongle.screen
        self.settings = pongle.settings
        self.screen_rect = self.screen.get_rect()
        #Create the ball and move it to the center of the player
        position_x , position_y = self.screen_rect.center
        self.rect = pygame.Rect(0, 0, self.settings.ball_size * 1.5,
                 self.settings.ball_size * 1.5)
        self.rect.center = pongle.player.rect.center

        self.x = int(self.rect.x)
        self.y = int(self.rect.y)


    def update(self, pongle):
        if not self.settings.ball_moving:
            self.x , self.y = pongle.player.rect.midtop
            self.y -= 50
            self.rect.y = self.y
            self.rect.x = self.x
        elif self.settings.ball_moving:
            self.x += self.settings.ball_speed_x
            self.y += self.settings.ball_speed_y
            self.rect.y = self.y
            self.rect.x = self.x


    def draw_ball(self):
        """Draw the ball at current location"""        
        pygame.draw.circle(self.screen, self.settings.ball_colour,
                self.rect.center, self.settings.ball_size)
        


