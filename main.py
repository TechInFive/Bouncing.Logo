import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing DVD Logo")
pygame.mouse.set_visible(False) 

# Load and scale the DVD logo image
dvd_logo_path = "dvd.logo.png"
dvd_logo = pygame.image.load(dvd_logo_path).convert_alpha()
dvd_logo = pygame.transform.scale(dvd_logo, (100, 50))
logo_rect = dvd_logo.get_rect()

# Set the initial position and speed
logo_rect.x = 660
logo_rect.y = 360
speed_x, speed_y = 2, 2  # Speed in pixels per frame

# Variables for spinning
is_spinning = False
spin_count = 0
spin_speed = 10

def change_logo_color(surface):
    r = random.randint(0, 3) * 64
    g = random.randint(0, 3) * 64
    b = random.randint(0, 3) * 64
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixle_color = surface.get_at((x, y))
            if pixle_color != (0, 0, 0, 0):
                new_r = (pixle_color[0] + r) % 256
                new_g = (pixle_color[1] + g) % 256
                new_b = (pixle_color[2] + b) % 256
                surface.set_at((x, y), (new_r, new_g, new_b, pixle_color[3]))
    return surface

# Function to rotate the logo
def rotate_logo(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(logo_rect.x, logo_rect.y)).center)
    return rotated_image, new_rect

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if logo_rect.collidepoint(mouse_pos) and not is_spinning:
                is_spinning = True
                spin_count = 0

    # Move the logo
    logo_rect.x += speed_x
    logo_rect.y += speed_y

    # Bounce off the edges
    if logo_rect.left <= 0 or logo_rect.right >= width:
        speed_x = -speed_x
        dvd_logo = change_logo_color(dvd_logo)
    if logo_rect.top <= 0 or logo_rect.bottom >= height:
        speed_y = -speed_y
        dvd_logo = change_logo_color(dvd_logo)

    # Clear the screen and draw the logo
    screen.fill((0, 0, 0))
    if is_spinning:
        spin_count += spin_speed
        display_logo, display_rect = rotate_logo(dvd_logo, spin_count)
        screen.blit(display_logo, display_rect)

        if spin_count >= 360*3:
            is_spinning = False
            spin_count = 0
    else:
        screen.blit(dvd_logo, logo_rect)

    if not is_spinning:
        # Draw the aiming circle and cross
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 20, 2)
        pygame.draw.line(screen, (255, 0, 0), (mouse_x - 15, mouse_y), (mouse_x + 15, mouse_y), 2)
        pygame.draw.line(screen, (255, 0, 0), (mouse_x, mouse_y - 15), (mouse_x, mouse_y + 15), 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
