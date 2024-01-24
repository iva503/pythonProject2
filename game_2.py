# Example file showing a circle moving on screen
import random

import pygame

from collision import detect_collision

player_speed = 600

player_size = 40
enemy_size = 40

screen_bound_x = 1280
screen_bound_y = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


def check_game_should_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True


def check_player_movement(player):
    move_distance = player_speed * dt
    # Handling Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= move_distance
    if keys[pygame.K_s]:
        player.y += move_distance
    if keys[pygame.K_a]:
        player.x -= move_distance
    if keys[pygame.K_d]:
        player.x += move_distance


def check_out_of_bounds(player):
    # Limiting our players posision
    if player.x < 0:
        player.x = 1240 + player_size
    if player.y < player_size:
        player.y = player_size
    if player.y > 720 - player_size:
        player.y = 720 - player_size
    if player.x > 1240 + player_size:
        player.x = 0


def draw_fake_player_objects(player):
    first_fake_circle_pos = player.copy()
    second_fake_circle_pos = player.copy()
    first_fake_circle_pos.x -= 1240 + player_size
    second_fake_circle_pos.x += 1240 + player_size

    pygame.draw.circle(screen, "red", first_fake_circle_pos, player_size)
    pygame.draw.circle(screen, "red", second_fake_circle_pos, player_size)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
object_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 4)


# Each enemy has position (x, y), color (blue or green or purple), radius - enemy_radius

def generate_enemy():
    radius = random.choice([30, 40, 50])
    new_enemy = {
        "position": pygame.Vector2(random.randrange(0 + radius, screen_bound_x - radius),
                                   random.randrange(0 + radius, screen_bound_y - radius)),
        "color": random.choice(['blue', 'green', 'purple']),
        "radius": radius
    }
    return new_enemy


enemies_list = []

for time in range(5):
    enemies_list.append(
        generate_enemy()
    )


def make_sure_theres_n_enemies(list_of_enemies, n):
    current_lenth_of_enemis = len(list_of_enemies)
    if n == current_lenth_of_enemis:
        return
    for a in range(n - current_lenth_of_enemis):
        list_of_enemies.append(generate_enemy())


def decrease_enemy_position(by_how_much):
    for enemy in enemies_list:
        enemy['position'].y += by_how_much * dt


points = 0

while running:
    if check_game_should_quit():
        break

    screen.fill("black")

    # Check if we need to move the player and move if needed
    check_player_movement(player_pos)
    # Check we didn't go out of bounds
    check_out_of_bounds(player_pos)

    # Draw the objects
    pygame.draw.circle(screen, "red", player_pos, player_size)

    for enemy in list(enemies_list):
        if detect_collision(player_pos, enemy['position'], player_size, enemy['radius']):
            # We are killing an emey
            enemies_list.remove(enemy)
            points += enemy['radius']
            print(f"Current points are {points}")

    make_sure_theres_n_enemies(enemies_list, 5)
    decrease_enemy_position(by_how_much=100)

    for enemy in enemies_list:
        pygame.draw.circle(screen, enemy['color'], enemy['position'], enemy['radius'])

    # if detect_collision(player_pos, object_pos, player_size, enemy_size):
    #     print("objects are colliding")
    # else:
    #     print("objects are not colliding")

    # Drawing the fake objects for warping
    draw_fake_player_objects(player_pos)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()