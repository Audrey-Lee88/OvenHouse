import pygame
import time
from pygame import font

pygame.init()
screen = pygame.display.set_mode([800,800])

line_space = 32
basicfont = pygame.font.Font('font/8bitoperator.ttf', 16)

def text_ani(str, tuple):
    x, y = tuple
    y = y * line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(0.05) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, (254, 254, 254), (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        print(textrect)
        screen.blit(text, 400 - text.get_width() // 2, 400 - text.get_height() // 2)
        # pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        pygame.display.update()
        count += 1
        letter += 1
        # print char ## for debugging in console, comment out or delete.


text_ani('You thought that the witch was the evil character who chased you so that she could gobble you up...', (0, 1))
text_ani("but she WASN'T!", (0, 2))
text_ani('You have destroyed her lovely house and invaded it, and the witch was simply trying to kick you out…', (0, 3))
text_ani('You now are an outlaw! Ayy', (0, 4))
