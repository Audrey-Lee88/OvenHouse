#
# import os
# import sys
# import random
# import os
# import getopt
# import pygame
# from socket import *
# from pygame import *
# import time
#
# pygame.init()
#
# textbox = pygame.draw.rect(DISPLAY, blue, (200,150,100,50))
# pygame.draw.update(textbox)
# textbox

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

fish_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

fishImg = pygame.image.load('fish.png')

def car(x,y):
    gameDisplay.blit(fishImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/1.15),(display_height/11.5))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('TIME HERE')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - fish_width or x < 0:
            crash()


        pygame.display.update()
        clock.tick(60)
#time
clock = pygame.time.Clock()
print(int(round(pygame.time.get_ticks()/1000)))
clock.tick(25)
temp = 25
if temp == 0:
    exit()
temp = temp-1
###
game_loop()
pygame.quit()
quit()
