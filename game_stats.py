import pygame.font
from pygame.sprite import Sprite
from Ship import Ship
from Settings import Settings

class GameStats:
    def __init__(self,ai_game):
        """initialize statistics"""
        self.Settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score
        self.high_score = 0

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.Settings.ship_limit
        self.score = 0
        self.level = 1
    
