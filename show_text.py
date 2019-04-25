import pygame
import time
from pygame import font

pygame.init()
screen = pygame.display.set_mode([800,800])

line_space = 32
basicfont = pygame.font.Font('font/8bitoperator.ttf', 16)


# ONE: make the screen stay on until the user clicks the next button
# TWO: make the text center
def text_ani(str, tuple):
    x, y = tuple
    y = y * line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(0.05)

        char = char + str[letter]
        text = basicfont.render(char, False, (254, 254, 254), (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        textrect.center = (800/2), (textrect[1] + 800/3)

        screen.blit(text, textrect)
        pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1


text_ani('You thought that the witch was the evil character', (0, 1))
text_ani('who chased you so that she could gobble you up...', (0, 2))
text_ani("but she WASN'T!", (0, 3))
text_ani('You have destroyed her lovely house and invaded it,', (0, 4))
text_ani('and the witch was simply trying to kick you out…', (0, 5))
text_ani('You now are an outlaw! Ayy', (0, 6))
text_ani('PRESS SPACEBAR TO PROCEED', (0, 8))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
