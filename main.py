import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing DVD Logo")

# Load the DVD logo image
dvd_logo_path = "dvd.logo.png"
dvd_logo = pygame.image.load(dvd_logo_path)
dvd_logo = pygame.transform.scale(dvd_logo, (100, 50))
logo_rect = dvd_logo.get_rect()

# Set the initial position and speed
logo_rect.x = random.randint(0, width - logo_rect.width)
logo_rect.y = random.randint(0, height - logo_rect.height)
speed_x, speed_y = 2, 2  # Speed in pixels per frame

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the logo
    logo_rect.x += speed_x
    logo_rect.y += speed_y

    # Bounce off the edges
    if logo_rect.left <= 0 or logo_rect.right >= width:
        speed_x = -speed_x
    if logo_rect.top <= 0 or logo_rect.bottom >= height:
        speed_y = -speed_y

    # Clear the screen and draw the logo
    screen.fill((0, 0, 0))
    screen.blit(dvd_logo, logo_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
