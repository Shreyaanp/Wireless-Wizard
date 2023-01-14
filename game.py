import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wireless Wizzard")

# Set the background color
bg_color = (255, 255, 255)

# Create a variable to control the game loop
running = True

# Create a variable to store the cursor position
cursor_pos = [350, 250]

# Create a variable to store the dot position
dot_pos = [random.randint(0,700), random.randint(0,500)]

# Start the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the cursor is within the dot
            if (cursor_pos[0]-dot_pos[0])*2 + (cursor_pos[1]-dot_pos[1])**2 < 50*2:
                # Generate a new random dot position
                dot_pos = [random.randint(0,700), random.randint(0,500)]
    # Get the mouse position
    cursor_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(bg_color)

    # Draw the cursor at the updated position
    pygame.draw.circle(screen, (255, 0, 0), cursor_pos, 10)

    # Draw the dot at the random position
    pygame.draw.circle(screen, (0, 255, 0), dot_pos, 50)

    # Update the screen
    pygame.display.flip()

# Exit Pygame
pygame.quit()