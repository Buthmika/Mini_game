import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Clock
clock = pygame.time.Clock()

# Load assets
car_width = 50
car_height = 100
player_car = pygame.Surface((car_width, car_height))
player_car.fill(BLUE)

enemy_car = pygame.Surface((car_width, car_height))
enemy_car.fill(RED)

star = pygame.Surface((10, 10))
star.fill(YELLOW)

# Functions
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Animate stars in the background
def animate_stars(stars):
    for star_pos in stars:
        star_pos[1] += 5
        if star_pos[1] > SCREEN_HEIGHT:
            star_pos[1] = -10
            star_pos[0] = random.randint(0, SCREEN_WIDTH - 10)
        screen.blit(star, (star_pos[0], star_pos[1]))

# Spawn multiple enemies
def spawn_enemies(enemy_list, enemy_speed):
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:
            enemy[1] = -car_height
            enemy[0] = random.randint(0, SCREEN_WIDTH - car_width)
        screen.blit(enemy_car, (enemy[0], enemy[1]))

# Check for collisions with multiple enemies
def check_collision(player_x, player_y, enemy_list):
    for enemy in enemy_list:
        if (enemy[0] < player_x < enemy[0] + car_width or enemy[0] < player_x + car_width < enemy[0] + car_width) and (
                enemy[1] < player_y < enemy[1] + car_height or enemy[1] < player_y + car_height < enemy[1] + car_height):
            return True
    return False

# Game loop
def game_loop():
    player_x = SCREEN_WIDTH // 2 - car_width // 2
    player_y = SCREEN_HEIGHT - car_height - 10

    enemy_list = [[random.randint(0, SCREEN_WIDTH - car_width), random.randint(-600, -100)] for _ in range(3)]
    enemy_speed = 5

    score = 0
    running = True

    # Create stars for background animation
    stars = [[random.randint(0, SCREEN_WIDTH - 10), random.randint(0, SCREEN_HEIGHT)] for _ in range(50)]

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 5
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - car_width:
            player_x += 5

        # Animate stars
        animate_stars(stars)

        # Move and draw enemy cars
        spawn_enemies(enemy_list, enemy_speed)

        # Check collision
        if check_collision(player_x, player_y, enemy_list):
            draw_text("Game Over!", 50, RED, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        # Draw player car
        screen.blit(player_car, (player_x, player_y))

        # Draw score
        draw_text(f"Score: {score}", 30, BLACK, 10, 10)

        # Update score and increase difficulty
        score += 1
        if score % 100 == 0:
            enemy_speed += 1

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Run the game
game_loop()
