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

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
player_speed = 5