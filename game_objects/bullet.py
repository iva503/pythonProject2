import random

import pygame
from pygame import Surface


class bullet:

    def __init__(self, screen: Surface, initial_positon):
        self.screen = screen
        self.position = initial_positon
        self.image = pygame.image.load("img_4.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.05, self.image.get_height() * 0.05))
        self.image = pygame.transform.rotate(self.image, 90)

    def draw(self):
        self.screen.blit(self.image, self.position, self.image.get_rect())

    def increase_position(self, delta_time):
        self.position.y -= 500 * delta_time
