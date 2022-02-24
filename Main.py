import sys
from time import sleep
import pygame
from Settings import Settings
from game_stats import GameStats
from Ship import Ship
from bullet import Bullet
from Alien import Alien
class AlienInvasion:
  """Overall class to manage the game."""

  def __init__(self):
      """Initalize the game, and creating resources."""
      pygame.init()
      self.settings=Settings()

      self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
      pygame.display.set_caption("Alien Invation")

      #Create an inistance to store statistics.
      self.stats = GameStats(self)

      self.ship = Ship(self)
      self.bullets = pygame.sprite.Group()
      self.aliens = pygame.sprite.Group()

      self.create_fleet()

  def run_game(self):
      """Start the main loop for the game."""
      while True:
          self._check_events()

          if self.stats.game_active:
              self.ship.update()
              self.update_bullets()
              self.update_aliens()

          self._update_screen()    

          #keyboard and mouse events
  def _check_events(self):
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
               sys.exit()
          elif event.type==pygame.KEYDOWN:
              self._check_keydown_events(event)
          elif event.type == pygame.KEYUP:
              self._check_keydup_events(event)

  def _check_keydown_events(self,event):
     #move the ship to the right side 
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right= True
      elif event.key == pygame.K_LEFT:
        self.ship.movin_left= True
      elif event.key == pygame.K_q:
        sys.exit()
      elif event.key == pygame.K_SPACE:
          self._fire_bullet()
           
  def _check_keydup_events(self,event):
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right=False
      elif event.key == pygame.K_LEFT:
        self.ship.movin_left= False

  def _fire_bullet(self):
      """Create a new bullet and add it to the bullets group"""
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def update_bullets(self):
      """function for updating the bullets"""
      self.bullets.update()
    #gitting rid of the old bullets
      for bullet in self.bullets.copy():
         if bullet.rect.bottom <= 0:
             self.bullets.remove(bullet)
      print(len(self.bullets))

      if not self.aliens:
          #Destroy existing bullets and create new fleet
          self.bullets.empty()
          if self.settings.alien_speed<7 and   self.settings.fleet_drop_speed<8:
             self.settings.alien_speed= self.settings.alien_speed+0.5
             self.settings.fleet_drop_speed=self.settings.fleet_drop_speed+0.1
          else:
             self.settings.alien_speed= self.settings.alien_speed
             self.settings.fleet_drop_speed=self.settings.fleet_drop_speed
          self.create_fleet()

        # Check for any bulltes to have hit the aliens, if so get rid of the bullet and the alien
      collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True , True)

  def create_fleet(self):
      """create the aliens fleet"""
      #make an alien
      alien = Alien(self)
      alien_width , alien_height = alien.rect.size
      available_space_x = self.settings.screen_width - (2*alien_width) + alien_width
      number_aliens_x =available_space_x // (2*alien_width)

      #Determine the number of rows of the alien that fit the screen
      ship_height = self.ship.rect.height
      available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
      number_rows = available_space_y // (2*alien_height)

      #create the full fleet of aliens
      for row_number in  range(number_rows -3):
          for alien_number in range(number_aliens_x):
              self.create_alien(alien_number, row_number)

  def create_alien(self,alien_number, row_number):
        #create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height *row_number
        self.aliens.add(alien)

  def ship_hit(self):
      """Respond to ship being hit by an alien"""

      if self.stats.ships_left > 0:
          #Decrement ships number left
          self.stats.ships_left -=1
          #get rid of remaining aliens and bullets
          self.aliens.empty()
          self.bullets.remove()

          #Create new flet and center the ship
          self.create_fleet()
          self.ship.center_ship()
          #pause
          sleep(0.5)
      else:
        self.stats.game_active = False

  def update_aliens(self):
      """Check if the fleet is at an edge, Update all aliens positions"""
      self.check_fleet_edges() 
      self.aliens.update()

      #look for alien-ship collision
      if pygame.sprite.spritecollideany(self.ship,self.aliens):
          print("Ship Hit!!!")
          self.ship_hit()

      # Look for aliens hitting the bottom of the screen.
      self.check_aliens_bottom()

  def check_fleet_edges(self):
      """respond appropriately if any aliens have reached edges"""
      for alien in self.aliens.sprites():
          if alien.check_edges():
              self. check_fleet_direction()
              break

  def check_fleet_direction(self):
      """Drop the entire fleet and change the fleet direction"""
      for alien in self.aliens.sprites():
          alien.rect.y += self.settings.fleet_drop_speed
      self.settings.fleet_direction *= -1

  def check_aliens_bottom(self):
      """Check if any aliens have reached the bottom of the screen."""
      screen_rect= self.screen.get_rect()
      for alien in self.aliens.sprites():
          if alien.rect.bottom >= screen_rect.bottom:
             # Treat this the same as if the ship got hit.
             self._ship_hit()
             break


  def _update_screen(self):
          # Redraw the screen during every pass through the loop
          self.screen.blit(self.settings.image,(-1,0))
          self.ship.blitme()

          for bullet in self.bullets.sprites():
              bullet.draw_bullet()

          self.aliens.draw(self.screen)
           # Make the most recently drawn screen visible.
          pygame.display.flip()   
          
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()



  