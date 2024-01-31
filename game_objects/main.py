# Example file showing a circle moving on screen
import random

import pygame
from pygame import Surface

from collision import detect_collision
from game_objects.enemy import Enemy
from game_objects.manager import GameManager
from game_objects.player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

background = pygame.image.load("img_2.png")
background = pygame.transform.scale(background, (1280, 720))
game_manager = GameManager(screen)
game_manager.initualize_game()

clock.tick(60)
while running:
    screen.blit(background, (0, 0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_manager.manager_loop()

    game_manager.show_score()
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()
