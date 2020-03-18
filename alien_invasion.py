import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from button import Button
from pause import Pause
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, 0, 1)
    pause_button = Pause(ai_settings, screen, "Pause")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, pause_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, 1 ,pause_button)
run_game()
 