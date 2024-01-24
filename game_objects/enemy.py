import random

import pygame
from pygame import Surface


class Enemy:

    def __init__(self, screen: Surface):
        radius = random.choice([80, 110, 130])
        self.screen = screen
        self.position = pygame.Vector2(
            random.randrange(0 + radius, self.screen.get_width() - radius),
            random.randrange(0 + radius, self.screen.get_height() / 2 - radius)
        )
        self.size = radius
        self.color = random.choice(['blue', 'yellow', 'purple'])
        self.sprite_base = pygame.image.load('img_1.png')
        self.sprite_base = pygame.transform.scale(self.sprite_base, (self.size, self.size))
        self.speed = 100

    def draw(self):
        self.screen.blit(self.sprite_base, self.position)

        # Drwain boxes
        rect_to_draw = self.sprite_base.get_rect(center=self.position)
        rect_to_draw.x += self.sprite_base.get_width() // 2
        rect_to_draw.y += self.sprite_base.get_height() // 2
        pygame.draw.rect(self.screen, 'white', rect_to_draw, 1)

    def decrease_position(self, delta_time):
        self.position.y += self.speed * delta_time
        if self.position.y > self.screen.get_height():
            self.position.y = 0
