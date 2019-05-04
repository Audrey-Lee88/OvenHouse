import pygame

def main():
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    running = True

    # Draw Once
    Rectplace = pygame.draw.rect(window, (255, 0, 0),(100, 100, 100, 100))
    Rectplace2 = pygame.draw.rect(window, (255, 0, 0),(300, 100, 100, 100))
    pygame.display.update()
    # Main Loop

    while running:
        # Mouse position and button clicking.
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        # Check if the rect collided with the mouse pos
        # and if the left mouse button was pressed.
        if Rectplace.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("You have picked player 1")
            return 1

        if Rectplace2.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("You have picked player 2")
            return 2

        # Quit pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
