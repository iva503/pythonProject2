import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

# Load images (you need to replace these with your own images)
player_image = pygame.Surface((50, 50))
player_image.fill((0, 0, 255))
bullet_image = pygame.Surface((10, 10))
bullet_image.fill((255, 0, 0))
target_image = pygame.Surface((30, 30))
target_image.fill((0, 255, 0))

# Define player
player_rect = player_image.get_rect()
player_rect.midbottom = (width // 2, height - 20)
player_speed = 5

# Define bullets
bullets = []
bullet_speed = 10

# Define targets
targets = []
target_speed = 3

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw everything
def draw_all():
    win.fill((0, 0, 0))
    win.blit(player_image, player_rect)
    for bullet in bullets:
        win.blit(bullet_image, bullet)
    for target in targets:
        win.blit(target_image, target)
    pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_rect.centerx - 5, player_rect.top, 10, 10)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    player_rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Create new targets
    if random.randint(20, 30) == 20:
        target = pygame.Rect(random.randint(0, width - 30), 0, 30, 30)
        targets.append(target)

    # Move bullets
    bullets = [bullet.move(0, -bullet_speed) for bullet in bullets]

    # Move targets
    targets = [target.move(0, target_speed) for target in targets]

    # Remove bullets and targets that are off-screen
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    targets = [target for target in targets if target.y < height]

    # Check for collisions
    for bullet in bullets:
        for target in targets:
            if bullet.colliderect(target):
                targets.remove(target)

    # Check if a target reached the bottom
    for target in targets:
        if target.y >= height:
            targets.remove(target)

    # Check if the player is hit
    for target in targets:
        if player_rect.colliderect(target):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    draw_all()

    # Set the frame rate
    clock.tick(110)