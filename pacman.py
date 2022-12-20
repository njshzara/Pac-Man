import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 400
window_height = 400

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the window caption
pygame.display.set_caption("Tic-Tac-Toe")

# Create a 2D list to represent the game board
board = [[None, None, None], [None, None, None], [None, None, None]]


# Create a function to draw the game board
def draw_board():
    # Set the line thickness
    thickness = 4

    # Draw the horizontal lines
    pygame.draw.line(window, (0, 0, 0), (0, window_height / 3), (window_width, window_height / 3), thickness)
    pygame.draw.line(window, (0, 0, 0), (0, 2 * window_height / 3), (window_width, 2 * window_height / 3), thickness)

    # Draw the vertical lines
    pygame.draw.line(window, (0, 0, 0), (window_width / 3, 0), (window_width / 3, window_height), thickness)
    pygame.draw.line(window, (0, 0, 0), (2 * window_width / 3, 0), (2 * window_width / 3, window_height), thickness)


# Run the game loop
running = True
while running:
    # Get the list of user events
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            running = False

        # Check if the user clicked the mouse button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the row and column of the board based on the mouse position
            row = mouse_y // (window_height / 3)
            col = mouse_x // (window_width / 3)

            # Update the game board based on the row and column
            board[row][col] = "X"  # Replace with player's symbol

# Use Pygame's font module to render the player's symbols
font = pygame.font.Font(None, 100)


# Create a function to draw the player's symbols on the board
def draw_symbols():
    for i in range(3):
        for j in range(3):
            symbol = board[i][j]
            if symbol:
                # Calculate the position of the symbol on the board
                x = j * (window_width / 3) + (window_width / 6)
                y = i * (window_height / 3) + (window_height / 6)
                text = font.render(symbol, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (x, y)
                window.blit(text, text_rect)


# Update the game board and draw the symbols on the screen
def update_board():
    window.fill((255, 255, 255))
    draw_board()
    draw_symbols()
    pygame.display.update()
