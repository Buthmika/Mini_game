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
GREEN = (0, 255, 0)

# Basket properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 10

# Apple properties
apple_radius = 15
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = 0
apple_speed = 6

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed
    
    # Move apple
    apple_y += apple_speed
    
    # Check if apple is caught
    if basket_y < apple_y + apple_radius and basket_x < apple_x < basket_x + basket_width:
        score += 1
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)
        apple_y = 0
        apple_speed += 0.2  # Increase speed after each catch
    
    # Reset apple if it falls
    if apple_y > HEIGHT:
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)
        apple_y = 0
    
    # Draw basket
    pygame.draw.rect(screen, GREEN, (basket_x, basket_y, basket_width, basket_height))
    
    # Draw apple
    pygame.draw.circle(screen, RED, (apple_x, apple_y), apple_radius)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    
pygame.quit()