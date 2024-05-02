import pygame

class PlayerBar:

    def __init__(self, pongle):
        """Creating a bar that represents the player"""
        self.screen = pongle.screen
        self.settings = pongle.settings
        self.screen_rect = pongle.screen.get_rect()
        self.colour = self.settings.player_colour

        """Create a bar rect and than move to right loacation location"""
        self.rect = pygame.Rect(0, 0, self.settings.player_width,self.settings.player_hight)
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)
        self.rect.y = self.y - 10

        #movement flags
        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def update(self):
        """Update the bar position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        self.rect.x = self.x
    

    def draw_player(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)