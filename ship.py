import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect
        self.image = pygame.image.load_basic('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center of the screen
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the position of the ship according to the flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """update the position of ship according to flag"""
        self.screen.blit(self.image, self.rect)
