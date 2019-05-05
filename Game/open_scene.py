import pygame
import show_text as st
import choose_char as cc

def main():
    pygame.init()
    screen_width, screen_height = 1200, 800
    window = pygame.display.set_mode((screen_width, screen_height))
    running = True
    line_space = 32
    basicfont = pygame.font.Font('8bitoperator.ttf', 20)


    st.text_ani('Welcome to OvenHouse', (0, 0), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("In this game, you get to choose whether to be Gretel or Hansel.", (0, 1), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Your goal is to escape from the witch's clutches.", (0, 2), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('To do so, you must collect two parts of a candy-key.', (0, 3), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Only then, can you can enter the door with a keyhole to escape.', (0, 4), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani("Do NOT run into the witch's minions (the balls of fire) or the witch herself!", (0, 5), line_space,basicfont,window,screen_width, screen_height)
    st.text_ani('Well then, GOOD LUCK!', (0, 6), line_space,basicfont,window,screen_width, screen_height)

    while running:
        st.blink_text('EXIT THE WINDOW TO PROCEED', (0, 8), (254,254,254),line_space, window, basicfont,screen_width,screen_height)
        st.blink_text('EXIT THE WINDOW  TO PROCEED', (0, 8), (0,0,0),line_space, window, basicfont, screen_width,screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                character = cc.main()
                return character



if __name__ == "__main__":
    main()
