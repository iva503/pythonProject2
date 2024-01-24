import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player setup
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 8

# Load player image
player_image = pygame.image.load("img_1.png")
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Bullet setup
bullet_size = 10
bullet_speed = 10
bullets = []

# Enemy setup
enemy_size = 50
enemy_speed = 5
enemies = []

# Load enemy image
enemy_image = pygame.image.load("img.png")
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter Game")

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Keep player within screen boundaries
    player_x = max(0, min(player_x, WIDTH - player_size))

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - bullet_size // 2, player_y - bullet_size])

    # Move and draw bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_size, bullet_size))

    # Remove bullets that have gone off the screen
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Spawn new enemies
    if random.randint(1, 60) == 1:
        enemies.append([random.randint(0, WIDTH - enemy_size), 0])

    # Move and draw enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Check for collisions between bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_size
                and enemy[1] < bullet[1] < enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Check for collisions between player and enemies
    for enemy in enemies:
        if (
            player_x < enemy[0] < player_x + player_size
            and player_y < enemy[1] < player_y + player_size
        ):
            print("Game Over!")  # You can modify this part to add more game elements like scoring or restarting.
            pygame.quit()
            sys.exit()

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Update display
    pygame.display.flip()

    # Set frames per second
    clock.tick(FPS)
