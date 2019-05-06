import pygame

import show_text as st

def end(Second,Minute,Hour):
    """Displays the final time the player finished the game or died"""
    pygame.init()
    screen_width, screen_height = 600, 600
    window = pygame.display.set_mode((screen_width, screen_height))
    running = True
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 20)

    st.text_ani('Time Survived:', (0, -5), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Second:{0:02}".format(Second),(0, 1),line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Minute:{0:02}".format(Minute),(0, 3),line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Hour:{0:03}".format(Hour),(0, 5),line_space,basicfont,window,screen_width, screen_height)
    while running:
        # Quit pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    end(1,1,1)
