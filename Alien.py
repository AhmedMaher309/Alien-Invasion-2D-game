import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_game):
        """initilaize the alien and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings=ai_game.settings
        #load the alien image and set its attributes
        self.image = pygame.image.load("images\Alien.bmp")
        self.image = pygame.transform.scale(self.image, (50, 32))
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def  check_edges(self):
        """return true if the alien at the edge of screen"""
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move the alien to the right side"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

   


