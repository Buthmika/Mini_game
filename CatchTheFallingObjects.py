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
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Basket properties
basket_width = 120
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 50
basket_speed = 12

# Apple properties
apple_radius = 15
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = 0
apple_speed = 6

# Score
score = 0
missed = 0
font = pygame.font.Font(None, 36)

# Game over condition
max_missed = 5

def show_game_over():
    screen.fill(WHITE)
    game_over_text = font.render("GAME OVER", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
    pygame.display.update()
    pygame.time.delay(2000)

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
        missed += 1
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)
        apple_y = 0
    
    # Check game over condition
    if missed >= max_missed:
        show_game_over()
        running = False
    
    # Draw basket
    pygame.draw.rect(screen, GREEN, (basket_x, basket_y, basket_width, basket_height))
    
    # Draw apple
    pygame.draw.circle(screen, RED, (apple_x, apple_y), apple_radius)
    
    # Display score and missed count
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    missed_text = font.render(f"Missed: {missed}/{max_missed}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(missed_text, (10, 40))
    
    pygame.display.update()
    
pygame.quit()
