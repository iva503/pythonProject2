import random

import pygame
from pygame import Surface


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen: Surface, speed: float):
        super().__init__()
        radius = random.choice([80, 110, 130])
        self.screen = screen
        initial_position = pygame.Vector2(
            random.randrange(0 + radius // 2, self.screen.get_width() - radius // 2),
            0
        )
        self.size = radius
        self.image = pygame.image.load('img_1.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.speed = speed
        self.rect = self.image.get_rect(center=initial_position)
        self.offset = 0
        self.move_right = random.choice([True, False])

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.screen.get_height():
            self.kill()
        if self.move_right:
            self.rect.x += self.speed
            self.offset += self.speed
        if not self.move_right:
            self.rect.x -= self.speed
            self.offset -= self.speed
        if self.offset >= self.size:
            self.move_right = False
        if self.offset <= 0:
            self.move_right = True
