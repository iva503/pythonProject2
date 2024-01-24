import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodging Game")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Define the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Define obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_list = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(win, white, [x, y, player_size, player_size])

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(win, red, obstacle)

# Function to check collisions
def check_collision(player_rect, obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Create new obstacles
    if random.randint(1, 10) == 1:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_list.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Move obstacles
    for obstacle in obstacle_list:
        obstacle.y += obstacle_speed

    # Remove obstacles that are off-screen
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.y < height]

    # Draw everything
    win.fill((0, 0, 0))
    draw_player(player_x, player_y)
    draw_obstacles(obstacle_list)

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    if check_collision(player_rect, obstacle_list):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(70)