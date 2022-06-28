import pygame.font

class Scoreboard:
    """ A class to report the score information"""

    def __init__(self, ai_game):
        """ Initalize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for score.
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image 
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        # Draw the score on screen.
        self.screen.blit(self.score_image, self.score_rect)