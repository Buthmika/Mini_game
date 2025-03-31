import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
player_speed = 7

# Falling object settings
object_size = 30
object_speed = 3
objects = []
powerups = []

# Font for score display
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
score = 0

def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Spawn falling objects
    if random.randint(1, 20) == 1:
        objects.append([random.randint(0, WIDTH - object_size), 0])
    
    # Spawn power-ups
    if random.randint(1, 150) == 1:
        powerups.append([random.randint(0, WIDTH - object_size), 0])
    
    # Move falling objects
    for obj in objects:
        obj[1] += object_speed
        pygame.draw.rect(screen, RED, (obj[0], obj[1], object_size, object_size))
    
    # Move power-ups
    for powerup in powerups:
        powerup[1] += object_speed // 2  # Power-ups fall slower
        pygame.draw.rect(screen, GREEN, (powerup[0], powerup[1], object_size, object_size))
    
    # Collision detection for objects
    for obj in objects[:]:
        if obj[1] > HEIGHT:
            objects.remove(obj)
            score += 1  # Increase score for dodging
        elif (player_x < obj[0] < player_x + player_size or player_x < obj[0] + object_size < player_x + player_size) and obj[1] + object_size > player_y:
            running = False  # Game over on collision
    
    # Collision detection for power-ups
    for powerup in powerups[:]:
        if powerup[1] > HEIGHT:
            powerups.remove(powerup)
        elif (player_x < powerup[0] < player_x + player_size or player_x < powerup[0] + object_size < player_x + player_size) and powerup[1] + object_size > player_y:
            powerups.remove(powerup)
            score += 5  # Power-ups increase score
    
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Display score
    draw_text(f"Score: {score}", 10, 10)
    
    # Update display
    pygame.display.update()
    clock.tick(30)  # Limit FPS

pygame.quit()
print("Game Over! Final Score:", score)