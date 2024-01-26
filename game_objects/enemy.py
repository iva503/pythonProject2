import random

import pygame
from pygame import Surface


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen: Surface):
        super().__init__()
        radius = random.choice([80, 110, 130])
        self.screen = screen
        initial_position = pygame.Vector2(
            random.randrange(0 + radius, self.screen.get_width() - radius),
            random.randrange(0 + radius, self.screen.get_height() / 2 - radius)
        )
        self.size = radius
        self.image = pygame.image.load('img_1.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.speed = 2
        self.rect = self.image.get_rect(center=initial_position)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.screen.get_height():
            self.rect.y = 0
