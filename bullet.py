import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """class for managing bullet's"""

  def __init__(self, ai_game):
      #creating bullet object at the ship current position
      super().__init__()
      self.screen = ai_game.screen
      self.settings = ai_game.settings
      self.color = self.settings.bullet_color

      #create a bullet
      self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
      self.rect.midtop = ai_game.ship.rect.midtop

      #store the bullet position
      self.y = float(self.rect.y)

      self.shot_bullet=False


  def update(self):
      """ move the buillet up in the screen """

      #update the decimal position of th bullet
      self.y -= self.settings.bullet_speed

      #update rect position
      self.rect.y = self.y

  def draw_bullet(self):
      """draw the bullets on screen"""
      pygame.draw.rect(self.screen, self.color, self.rect)

