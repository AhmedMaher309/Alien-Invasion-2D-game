import pygame


class Settings:
   #class to store all the settings of the game 
   def __init__(self):
       """initialize the game's settings"""
       #First, screen settings
       self.screen_width=1200
       self.screen_height=750
       self.bg_color=(260,260,260)

       self.image = pygame.image.load("images\space3.bmp")
       self.image = pygame.transform.scale(self.image, (1200, 750))
       

       #ship settingd
       self.ship_speed=2
       self.ship_limit=3

       #Aliens speed
       self.alien_speed=1.5
       self.fleet_drop_speed=6

       # fleet_direction of is right, -1 is left
       self.fleet_direction =1

       #Bullet Settings
       self.bullet_speed = 3
       self.bullet_width = 4
       self.bullet_height = 12
       self.bullet_color = (210,210,160)


