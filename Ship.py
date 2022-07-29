import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
     """A class to manage the space ship"""

     def __init__(self, ai_game):
         """Intialize the ship and set the position"""
         super().__init__()
         self.screen = ai_game.screen
         self.screen_rect = ai_game.screen.get_rect()
         self.settings =ai_game.settings

         #get the ship image from the files and set its attributes
         self.image = pygame.image.load("images\space-ship111.bmp")
         self.image = pygame.transform.scale(self.image, (45, 50))
         self.rect = self.image.get_rect()

         # Start each new new ship at the bottom center of screen
         self.rect.midbottom = self.screen_rect.midbottom

         self.x=float(self.rect.x)

         #Movement flag
         self.moving_right=False
         self.movin_left=False

     def update(self):
         """update the ship position based on the movement flag"""
         if self.moving_right and self.rect.right < self.screen_rect.right:
             self.x += self.settings.ship_speed
         elif self.movin_left and self.rect.left > 0:
              self.x -= self.settings.ship_speed

         self.rect.x=self.x

     def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

     def center_ship(self):
         """Center the ship on the screen"""
         self.rect.midbottom = self.screen_rect.midbottom
         self.x = float(self.rect.x)

    