import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """the class for single alien"""

    def __init__(self, ai_settings, screen):
        """initial ailen and set position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # load the picture of alien and set rect
        self.image = pygame.image.load_basic('images\\alien_ship.bmp')
        self.rect = self.image.get_rect()

        # every alien shows up at left-top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save exact position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """update the position of alien according to flag"""
        self.screen.blit(self.image, self.rect)