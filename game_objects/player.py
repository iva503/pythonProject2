import time

import pygame
from pygame import Surface


def get_all_ship_sprites():
    all_sprites = []
    sprite_base = pygame.image.load('img.png')
    sprite_base = pygame.transform.scale(
        sprite_base,
        (int(sprite_base.get_width() * 0.6),
         int(sprite_base.get_height() * 0.6))
    )
    sprite_width, sprite_height = sprite_base.get_width() // 4, sprite_base.get_height() // 2
    for row in range(1, 3):
        for column in range(4):
            subsprite_size = pygame.Rect(
                column * sprite_width,
                sprite_height * (row - 1),
                sprite_width,
                sprite_height
            )
            print(subsprite_size)
            print(sprite_base)
            subsprite = sprite_base.subsurface(subsprite_size)
            all_sprites.append(subsprite)
    return all_sprites


class Player(pygame.sprite.Sprite):

    def __init__(
            self,
            screen: Surface,
            position,
            size,
            color
    ):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = get_all_ship_sprites()
        self.screen = screen
        self.size = size
        self.color = color
        self.is_angry = False
        self.image = self.all_sprites[0]

        # rect is required for the sprite to know what to draw
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.mask = pygame.mask.from_surface(self.image)


        # Player modifiers
        self.player_speed = 8
        self.angry_timer = 0
        self.lives = 5

    def update(self, *args, **kwargs):
        self.mask = pygame.mask.from_surface(self.image)
        self.reset_state()
        self.check_if_needed_to_be_normal()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()
        self.check_out_of_bounds()

    def reset_state(self):
        self.image = self.all_sprites[0]
        if self.is_angry:
            self.image = self.all_sprites[4]

    def check_out_of_bounds(self):
        # Limiting our players posision
        if self.rect.x < 0:
            self.rect.x = self.screen.get_width() + self.size
        if self.rect.y < self.size:
            self.rect.y = self.size
        if self.rect.y > self.screen.get_height() - self.size:
            self.rect.y = self.screen.get_height() - self.size
        if self.rect.x > self.screen.get_width() + self.size:
            self.rect.x = 0

    def move_up(self):
        self.rect.y -= self.player_speed
        if self.is_angry:
            self.image = self.all_sprites[4]

    def move_down(self):
        self.rect.y += self.player_speed
        if self.is_angry:
            self.image = self.all_sprites[4]

    def move_right(self):
        self.image = self.all_sprites[3]
        self.rect.x += self.player_speed
        if self.is_angry:
            self.image = self.all_sprites[5]

    def move_left(self):
        self.image = self.all_sprites[1]
        self.rect.x -= self.player_speed
        if self.is_angry:
            self.image = self.all_sprites[7]

    def become_angry(self):
        if self.is_angry:
            return
        self.player_speed = 10
        self.color = 'red'
        self.size += 20
        self.is_angry = True
        self.angry_timer = pygame.time.get_ticks() + 5000  # 5000 ms - 5 seconds

    def become_normal(self):
        if not self.is_angry:
            return
        self.player_speed = 6
        self.color = 'blue'
        self.size -= 20
        self.is_angry = False

    def check_if_needed_to_be_normal(self):
        if pygame.time.get_ticks() > self.angry_timer:
            self.become_normal()

    def draw_fake_enemies(self):
        first_fake_circle_pos = self.rect.copy()
        second_fake_circle_pos = self.rect.copy()
        first_fake_circle_pos.x -= self.screen.get_width() + self.size
        second_fake_circle_pos.x += self.screen.get_width() + self.size
        pygame.draw.circle(self.screen, self.color, first_fake_circle_pos, self.size)
        pygame.draw.circle(self.screen, self.color, second_fake_circle_pos, self.size)
