class GameStats:
    """Track all statistics in the game"""

    def __init__(self, pongle):
        """Initializing all statistics"""
        self.settings = pongle.settings
        self.reset_stats()
        #highscore for the game
        with open("highscore.txt","r") as hfile:
            self.high_score = int(hfile.read())
        self.level = 1

    def reset_stats(self):
        """Initializing stats that can change during a game"""
        self.lives = self.settings.player_lives
        self.score = 0