import pygame
import show_text as st

def main():
    pygame.init()
    screen_width, screen_height = 600, 600
    window = pygame.display.set_mode((screen_width, screen_height))
    running = True
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 20)
    img = pygame.image.load('gretel.png')
    img2 = pygame.image.load('hansel.png')

    # Draw Once
    Rectplace = window.blit(img,(40,100))
    Rectplace2 = window.blit(img2,(350,100))
    pygame.display.update()
    # Main Loop
    st.text_ani('Choose', (0, -5), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Gretel', (-150, 9), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Hansel', (150, 9), line_space,basicfont,window,screen_width, screen_height)
    while running:
        # Mouse position and button clicking.
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        # Check if the rect collided with the mouse pos and if the left mouse button was pressed.
        if Rectplace.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("You have picked Gretel")
            return 1

        if Rectplace2.collidepoint(pos) and (pressed1 or pressed2 or pressed3):
            print("You have picked Hansel")
            return 2

        # Quit pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
