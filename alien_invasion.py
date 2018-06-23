import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # title of game
    pygame.display.set_caption("Alien Invasion")
    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group to save the bullets
    bullets = Group()
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
