import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprite Display')

# Load sprite file
sprite_file = "img.png"  # Replace with the actual file path
spritesheet = pygame.image.load(sprite_file)

# Define sprite size and number of sprites
sprite_width, sprite_height = spritesheet.get_width() // 4, spritesheet.get_height()//2
num_sprites = 4

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the index of the sprite to display (0 to 7)
    sprite_index = 0  # Replace with your logic to get the desired index

    # Calculate the rectangle for the current sprite
    sprite_rect = pygame.Rect(sprite_index * sprite_width, 0, sprite_width, sprite_height)

    # Blit the sprite onto the screen
    screen.blit(spritesheet, (0, 0), sprite_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()