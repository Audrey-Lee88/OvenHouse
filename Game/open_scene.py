import pygame
import show_text as st

def main():
    pygame.init()
    screen_width, screen_height = 1200, 800
    window = pygame.display.set_mode((screen_width, screen_height))
    running = True
    line_space = 32
    basicfont = pygame.font.Font('8bitoperator.ttf', 20)


    st.text_ani('Welcome to OvenHouse', (0, 1), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Your goal as Hansel/Gretel is to escape from the witch's clutches.", (0, 2), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('To do so, you must collect two parts to the candy-key.', (0, 3), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Only so then you can enter the door (the door has a keyhole).', (0, 4), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Do NOT run into the witch's minions or the witch herself!", (0, 5), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Well then, GOOD LUCK!', (0, 6), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('PRESS SPACEBAR TO PROCEED', (0, 8),line_space,basicfont, window,screen_width,screen_height)

    while True:
        st.blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (254,254,254),line_space, window, basicfont,screen_width,screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
        st.blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (0,0,0),line_space, window, basicfont, screen_width,screen_height)


if __name__ == "__main__":
    main()
