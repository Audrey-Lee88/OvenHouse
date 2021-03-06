import pygame
import time
import sys
from pygame import font
import end_game as eg


def text_ani(str, tuple,line_space,basicfont,screen,screen_width,screen_height):
    """
    Displays text letter by letter on the screen
    """
    x, y = tuple
    y = y * line_space # shift text down by one line
    char = ''        # string that will take one char at a time
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear()
        time.sleep(0.05)

        char = char + str[letter] # keeps the already existing characters and adds char one by one
        text = basicfont.render(char, False, (254, 254, 254), (0, 0, 0)) #  first tuple = text color; second tuple = background color
        textrect = text.get_rect(topleft=(x, y)) # x, y's provided in function call. y coordinate amended by line height where needed
        textrect.center = (textrect[0] +screen_width/2), (textrect[1] + screen_height/3)

        screen.blit(text, textrect)
        pygame.display.update(textrect) # update only the text just added without removing previous lines
        count += 1
        letter += 1


def blink_text(str, tuple, rgb, line_space, screen, basicfont, screen_width, screen_height):
    """
    Displays the input "str" as the input "rgb"
    """
    pygame.event.clear()
    time.sleep(0.20)

    x, y = tuple
    y = y * line_space

    text = basicfont.render(str, False, rgb, (0, 0, 0))
    textrect = text.get_rect(topleft=(x, y))
    textrect.center = (screen_width/2), (textrect[1] + screen_height/3)

    screen.blit(text, textrect)
    pygame.display.update(textrect)


def win_game(Second, Minute, Hour):
    """
    Displays text when the player wins the game
    """
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width,screen_height])
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 16)
    # below is the text that is displayed
    text_ani('You thought that the witch was the evil character', (0, 1), line_space,basicfont,screen,screen_width,screen_height)
    text_ani('who chased you so that she could gobble you up...', (0, 2),line_space,basicfont,screen,screen_width,screen_height)
    text_ani("but she WASN'T!", (0, 3),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('You have destroyed her lovely house and invaded it,', (0, 4),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('while the witch was simply trying to kick you out…', (0, 5),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('You are now considered an outlaw and will go to jail! Ayy', (0, 6),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('PRESS SPACEBAR TO PROCEED', (0, 8),line_space,basicfont,screen,screen_width,screen_height)

    # the two blink_text in the loop makes the text blink in black and white
    while True:
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (254,254,254),line_space,screen,basicfont,screen_width,screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                eg.end(Second,Minute,Hour)
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    eg.end(Second,Minute,Hour)
                    exit()
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (0,0,0),line_space, screen,basicfont,screen_width,screen_height)


def contact_fire(Second, Minute, Hour):
    """
    Displays text when the player makes contact with the fire sprites
    """
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width,screen_height])
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 16)
    # below is the text that is displayed
    text_ani("You were caught by one of witch's minions...", (0, 1), line_space,basicfont,screen,screen_width,screen_height)
    text_ani('You are now adequately roasted for the witch to gobble you up!', (0, 2),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('PRESS SPACEBAR TO PROCEED', (0, 4),line_space,basicfont,screen,screen_width,screen_height)

    # the two blink_text in the loop makes the text blink in black and white
    while True:
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 4), (254,254,254),line_space,screen,basicfont,screen_width,screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                eg.end(Second,Minute,Hour)
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    eg.end(Second,Minute,Hour)
                    exit()
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 4), (0,0,0),line_space, screen,basicfont,screen_width,screen_height)


def contact_witch(Second, Minute, Hour):
    """
    Displays text when the player makes contact with the witch
    """
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width,screen_height])
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 16)
    # below is the text that is displayed
    text_ani("You were caught by the witch herself...", (0, 1), line_space,basicfont,screen,screen_width,screen_height)
    text_ani('She is enranged towards you and says,', (0, 2),line_space,basicfont,screen,screen_width,screen_height)
    text_ani('"I got a lot of recipes to try on you!"', (0, 3),line_space,basicfont,screen,screen_width,screen_height)

    # the two blink_text in the loop makes the text blink in black and white
    while True:
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 5), (254,254,254),line_space,screen,basicfont,screen_width,screen_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                eg.end(Second,Minute,Hour)
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    eg.end(Second,Minute,Hour)
                    exit()
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 5), (0,0,0),line_space, screen,basicfont,screen_width,screen_height)
