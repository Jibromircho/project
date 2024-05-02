import pygame

from pygame.sprite import Sprite

class Bricks(Sprite):
    """A class for the brick enemies in the game"""

    def __init__(self, pongle):
        super().__init__()
        self.screen = pongle.screen
        self.settings = pongle.settings
        self.screen_rect = pongle.screen.get_rect()
        self.colour = self.settings.brick_colour

        """Create a brick and position it to the top left"""
        self.rect = pygame.Rect(0, 0, self.settings.brick_width,self.settings.brick_hight)
        self.rect.topleft = self.screen_rect.topleft


    def draw_brick(self):
        """Draw a brick on the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)