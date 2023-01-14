import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mouse Game")

# Set the background color
bg_color = (255, 255, 255)

# Create a variable to control the game loop
running = True

# Start the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(bg_color)

    # Draw a circle at the mouse position
    pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 50)

    # Update the screen
    pygame.display.flip()

# Exit Pygame
pygame.quit()