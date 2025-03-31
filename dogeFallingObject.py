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

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
player_speed = 7

# Falling object settings
object_size = 30
object_speed = 3
objects = []

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
    if random.randint(1, 20) == 1:  # Increased chance to spawn objects
        objects.append([random.randint(0, WIDTH - object_size), 0])
    
  e.draw.rect(screen, RED, (obj[0], obj[1], object_size, object_size))
    
    
    for obj in objects[:]:
        if obj[1] > HEIGHT:
            obj