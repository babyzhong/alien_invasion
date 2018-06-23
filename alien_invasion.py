import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien


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
    # bulit a alien
    alien = Alien(ai_settings, screen)

    # begin the main loop
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
