import time

import pygame
from pygame import Surface


class Player:

    def __init__(
            self,
            screen: Surface,
            position,
            size,
            color
    ):
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color
        self.player_speed = 600
        self.is_angry = False
        self.angry_timer = 0
        self.sprite_base = pygame.image.load('img.png')
        self.sprite_base = pygame.transform.scale(self.sprite_base,
                                                  (int(self.sprite_base.get_width() * 0.6),
                                                   int(self.sprite_base.get_height() * 0.6))
                                                  )
        sprite_width, sprite_height = self.sprite_base.get_width() // 4, self.sprite_base.get_height() // 2
        self.all_sprites = []

        self.lives = 5

        for row in range(1, 3):
            for column in range(4):
                subsprite_size = pygame.Rect(
                    column * sprite_width,
                    sprite_height * (row - 1),
                    sprite_width,
                    sprite_height
                )
                print(subsprite_size)
                print(self.sprite_base)
                subsprite = self.sprite_base.subsurface(subsprite_size)
                self.all_sprites.append(subsprite)
        self.sprite_to_display = self.all_sprites[0]




    def reset_state(self):
        self.sprite_to_display = self.all_sprites[0]
        if self.is_angry:
            self.sprite_to_display = self.all_sprites[4]

    def check_out_of_bounds(self):
        # Limiting our players posision
        if self.position.x < 0:
            self.position.x = self.screen.get_width() + self.size
        if self.position.y < self.size:
            self.position.y = self.size
        if self.position.y > self.screen.get_height() - self.size:
            self.position.y = self.screen.get_height() - self.size
        if self.position.x > self.screen.get_width() + self.size:
            self.position.x = 0

    def draw(self):
        self.check_out_of_bounds()
        if self.is_angry:
            if self.angry_timer < time.time():
                self.become_normal()
        self.screen.blit(self.sprite_to_display, self.position)

        # Drawin boxes
        rect_to_draw = self.sprite_to_display.get_rect(center=self.position)
        rect_to_draw.x += self.sprite_to_display.get_width() // 2
        rect_to_draw.y += self.sprite_to_display.get_height() // 2
        pygame.draw.rect(self.screen, 'white', rect_to_draw, 1)
        self.draw_fake_enemies()

    def move_up(self, delta_time):
        self.position.y -= self.player_speed * delta_time
        if self.is_angry:
            self.sprite_to_display = self.all_sprites[4]

    def move_down(self, delta_time):
        self.position.y += self.player_speed * delta_time
        if self.is_angry:
            self.sprite_to_display = self.all_sprites[4]

    def move_right(self, delta_time):
        self.sprite_to_display = self.all_sprites[3]
        self.position.x += self.player_speed * delta_time
        if self.is_angry:
            self.sprite_to_display = self.all_sprites[5]

    def move_left(self, delta_time):
        self.sprite_to_display = self.all_sprites[1]
        self.position.x -= self.player_speed * delta_time
        if self.is_angry:
            self.sprite_to_display = self.all_sprites[7]

    def become_angry(self):
        if self.is_angry:
            return
        self.player_speed = 1200
        self.color = 'red'
        self.size += 20
        self.is_angry = True
        self.angry_timer = time.time() + 5  # From the moment we became angry + 10 seconds

    def become_normal(self):
        if not self.is_angry:
            return
        self.player_speed = 600
        self.color = 'blue'
        self.size -= 20
        self.is_angry = False

    def draw_fake_enemies(self):
        first_fake_circle_pos = self.position.copy()
        second_fake_circle_pos = self.position.copy()
        first_fake_circle_pos.x -= self.screen.get_width() + self.size
        second_fake_circle_pos.x += self.screen.get_width() + self.size
        pygame.draw.circle(self.screen, self.color, first_fake_circle_pos, self.size)
        pygame.draw.circle(self.screen, self.color, second_fake_circle_pos, self.size)
