import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Define the bullet
bullet_size = 10
bullet_speed = 7
bullet_list = []

# Define the target
target_size = 50
target_speed = 3
target_list = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(win, white, [x, y, player_size, player_size])

# Function to draw bullets
def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.rect(win, white, bullet)

# Function to draw targets
def draw_targets(targets):
    for target in targets:
        pygame.draw.rect(win, red, target)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_size // 2 - bullet_size // 2
                bullet_y = player_y
                bullet_list.append(pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size))

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Create new targets
    if random.randint(1, 10) == 1:
        target_x = random.randint(0, width - target_size)
        target_y = -target_size
        target_list.append(pygame.Rect(target_x, target_y, target_size, target_size))

    # Move bullets
    bullet_list = [bullet.move(0, -bullet_speed) for bullet in bullet_list]

    # Move targets
    target_list = [target.move(0, target_speed) for target in target_list]

    # Remove bullets and targets that are off-screen
    bullet_list = [bullet for bullet in bullet_list if bullet.y > 0]
    target_list = [target for target in target_list if target.y < height]

    # Check for collisions
    for bullet in bullet_list:
        for target in target_list:
            if bullet.colliderect(target):
                target_list.remove(target)

    # Draw everything
    win.fill(black)
    draw_player(player_x, player_y)
    draw_bullets(bullet_list)
    draw_targets(target_list)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(100)