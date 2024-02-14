import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Tulip")

# Load the tulip image
tulip_image = pygame.image.load("tulip.png")
tulip_rect = tulip_image.get_rect()

# Initial position of the tulip
tulip_x = 0
tulip_y = 0

# Movement speed
speed = 1

# Main loop
while True:
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update tulip position
    tulip_x += speed
    tulip_y += speed

    # If tulip goes off the screen, reset its position
    if tulip_x > screen_width or tulip_y > screen_height:
        tulip_x = 0
        tulip_y = 0

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the tulip at its current position
    screen.blit(tulip_image, (tulip_x, tulip_y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.delay(10)
