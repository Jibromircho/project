import pygame.font

class GameText:
    """A class for the text in game"""
    def __init__(self,pongle,msg):
        """Initialize the buttons atributes"""
        self.screen = pongle.screen
        self.screen_rect = self.screen.get_rect()
        #set dimentions and properties of the text
        self.width, self.height = 200,50
        self.bg_colour = pongle.settings.bg_colour
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #build buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #the buttons message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into img and center on the button"""
        self.msg_img = self.font.render(msg, True, self.text_colour,self.bg_colour)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_msg(self):
        """Draw a blank button and then draw the text on it"""
        self.screen.fill(self.bg_colour, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)