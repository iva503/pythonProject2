import random

import pygame
from pygame import Surface


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen: Surface, initial_positon):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("img_4.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.05, self.image.get_height() * 0.05))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=initial_positon)

    def update(self):
        self.rect.y -= 7
        if self.rect.y < 0:
            self.kill()
