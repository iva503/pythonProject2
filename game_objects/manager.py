import pygame

from game_objects.bullet import Bullet
from game_objects.enemy import Enemy
from game_objects.player import Player


class GameManager:
    def __init__(self, screen, ):
        self.allowed_to_shoot = True
        self.score = 0
        self.player_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.shooting_frq = 0.5
        self.player = Player(screen, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 30, "green")
        self.player_group.add(self.player)
        self.screen = screen
        self.next_shot = self.shooting_frq

    def initualize_game(self):
        self.make_sure_theres_n_enemies(5)

    def shoot(self):
        if self.allowed_to_shoot:
            self.bullets_group.add(
                Bullet(self.screen, (self.player.rect.x, self.player.rect.y))
            )
            self.allowed_to_shoot = False
            self.next_shot = pygame.time.get_ticks() + 500

    def make_sure_theres_n_enemies(self, n):
        current_lenth_of_enemis = len(self.enemies_group.sprites())
        if n == current_lenth_of_enemis:
            return
        for a in range(n - current_lenth_of_enemis):
            self.enemies_group.add(Enemy(self.screen))

    def enemy_killed(self):
        self.score += 5

    def show_score(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(f'Score:{self.score} ', True, 'red', 'blue')
        text_lives = font.render(f'lifes:{self.player.lives} ', True, 'yellow', 'green')
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        text_lives_rect = text_lives.get_rect()
        # set the center of the rectangular object.
        textRect.center = (self.screen.get_width() // 2, 50)
        text_lives_rect.center = (100, self.screen.get_height() - 50)
        self.screen.blit(text, textRect)
        self.screen.blit(text_lives, text_lives_rect)

    def check_shooting(self):
        if not self.allowed_to_shoot:
            if self.next_shot < pygame.time.get_ticks():
                self.next_shot = self.shooting_frq
                self.allowed_to_shoot = True

    def manager_loop(self):
        print("Bullet count", len(self.bullets_group))
        self.enemy_collision()
        self.bullet_collision()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.player.become_angry()
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.check_shooting()

        self.make_sure_theres_n_enemies(5)

        self.player_group.update()
        self.enemies_group.update()
        self.bullets_group.update()

        # Draw everything else
        self.enemies_group.draw(self.screen)
        self.bullets_group.draw(self.screen)

        # Draw the player
        self.player_group.draw(self.screen)

        if self.player.is_angry:
            self.shooting_frq = 0.25
        else:
            self.shooting_frq = 0.5

    def bullet_collision(self):
        for bullet in self.bullets_group.sprites():
            if pygame.sprite.spritecollide(bullet, self.enemies_group, True, pygame.sprite.collide_mask):
                bullet.kill()

    def enemy_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemies_group, True, pygame.sprite.collide_mask):
            self.player.lives -= 1
