import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Basket properties
basket_width = 80
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 7

# Apple properties
apple_radius = 15
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = 0
apple_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)