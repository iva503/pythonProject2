import pygame

from game_objects.bullet import bullet
from game_objects.enemy import Enemy
from game_objects.player import Player


class GameManager:
    def __init__(self, screen, ):
        self.allowed_to_shoot = True
        self.score = 0
        self.enemylist = []
        self.bullets = []
        self.shooting_frq = 0.5
        self.player = Player(screen, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 30, "green")
        self.screen = screen
        self.last_shot = self.shooting_frq

    def initualize_game(self):
        self.make_sure_theres_n_enemies(5)

    def shoot(self):
        if self.allowed_to_shoot:
            self.bullets.append(bullet(self.screen, self.player.position.copy()))
            self.allowed_to_shoot = False

    def make_sure_theres_n_enemies(self, n):
        current_lenth_of_enemis = len(self.enemylist)
        if n == current_lenth_of_enemis:
            return
        for a in range(n - current_lenth_of_enemis):
            self.enemylist.append(Enemy(self.screen))

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

    def enemy_collision(self):
        for enemy in self.enemylist:
            # Creating the masks
            # Finding the positions for the mask offsets
            player_rect = self.player.sprite_to_display.get_rect(topleft=self.player.position)
            enemy_rect = enemy.sprite_base.get_rect(topleft=enemy.position)
            # Here we know that we are actually colliding
            if player_rect.colliderect(enemy_rect):
                print("Coliding")
                self.enemylist.remove(enemy)
                self.player.lives -= 1

    def check_shooting(self, dt):
        if not self.allowed_to_shoot:
            if self.last_shot < 0:
                self.last_shot = self.shooting_frq
                self.allowed_to_shoot = True
            else:
                self.last_shot -= dt

    def manager_loop(self, dt):
        self.enemy_collision()
        self.check_shooting(dt)

        self.make_sure_theres_n_enemies(5)
        for enemy in self.enemylist:
            enemy.decrease_position(dt)
            enemy.draw()
        for bullet in self.bullets:
            bullet.increase_position(dt)
            bullet.draw()
        if self.player.is_angry:
            self.shooting_frq = 0.25
        else:
            self.shooting_frq = 0.5
