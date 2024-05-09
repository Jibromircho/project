class Settings:
    """Class for all the settings we will use in the game"""

    def __init__(self):
        #screen settings
        self.screen_width = 1440
        self.screen_hight = 900
        self.bg_colour = (150, 210, 200)
        #ball settings
        self.ball_colour = (70, 90, 90)
        self.ball_size = 15
        #bricks settings
        self.brick_colour = (150, 70, 70)
        self.brick_points_scale = 1.2
        self.brick_size_scale = 0.95
        #player 
        self.player_width = 300
        self.player_hight = 20
        self.player_colour = (70, 70, 70)
        self.player_lives = 5
        self.player_speed_scale = 1.1
        #initialize the settings the first time
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #dynamic ball settings
        self.ball_moving = False
        self.player_speed = 5 
        self.ball_speed_max = 5
        self.ball_speed_x = -4
        self.ball_speed_y = -4
        self.brick_hight = 125
        self.brick_width = 125
        self.brick_points = 10
    
    def increase_level(self):
        """Increase level settings"""
        if self.player_speed >= 25:
            self.player_speed *= self.player_speed_scale
        if self.ball_speed_max >= 22:
            self.ball_speed_x *= self.player_speed_scale
            self.ball_speed_y *= self.player_speed_scale
            self.ball_speed_max *= self.player_speed_scale
        if self.brick_hight < 25:
            self.brick_hight *= self.brick_size_scale
            self.brick_width *= self.brick_size_scale
        self.brick_points = int(self.brick_points_scale * self.brick_points)