import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the paddles
paddle_width, paddle_height = 10, 60
player_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = 5

# Define the ball
ball_size = 15
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5 * random.choice([1, -1])

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw paddles and ball
def draw_game():
    win.fill(black)
    pygame.draw.rect(win, white, player_paddle)
    pygame.draw.rect(win, white, opponent_paddle)
    pygame.draw.ellipse(win, white, ball)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_paddle.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * paddle_speed

    # Ensure paddles stay within the screen boundaries
    player_paddle.y = max(0, min(player_paddle.y, height - paddle_height))
    opponent_paddle.y = max(0, min(ball.y, height - paddle_height))

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    # Opponent AI
    if opponent_paddle.bottom < ball.y:
        opponent_paddle.y += paddle_speed
    if opponent_paddle.top > ball.y:
        opponent_paddle.y -= paddle_speed

    # Draw the game
    draw_game()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)