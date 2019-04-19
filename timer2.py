import pygame
import time

pygame.init()
#
display_width = 800
display_height = 200

done = False
#Time Info
Time = 0
Second = 0
Minute = 0
Hour = 0
counter=0

#Colour
Black = (0,0,0)
White = (255, 255, 255)

#Fonts
Font = pygame.font.SysFont("Trebuchet MS", 25)

#Day
DayFont = Font.render("Hour:{0:03}".format(Hour),1, Black) #zero-pad day to 3 digits
DayFontR=DayFont.get_rect()
DayFontR.center=(985,20)
#Hour
HourFont = Font.render("Minute:{0:02}".format(Minute),1, Black) #zero-pad hours to 2 digits
HourFontR=HourFont.get_rect()
HourFontR.center=(1085,20)
#Minute
MinuteFont = Font.render("Second:{0:02}".format(Second),1, Black) #zero-pad minutes to 2 digits
MinuteFontR=MinuteFont.get_rect()
MinuteFontR.center=(1200,20)

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

size = width, height = 1280, 720 #Make sure background image is same size
screen = pygame.display.set_mode(size)
screen.fill(White)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == CLOCKTICK: # count up the clock
            #Timer
            Second=Second+1
            if Second == 60:
                Minute=Minute+1
                Second=0
            if Minute==60:
                Hour=Hour+1
                Minute=0
            # redraw time
            screen.fill(White)
            MinuteFont = Font.render("Second:{0:02}".format(Second),1, Black)
            screen.blit(MinuteFont, MinuteFontR)
            HourFont = Font.render("Minute:{0:02}".format(Minute),1, Black)
            screen.blit(HourFont, HourFontR)
            DayFont = Font.render("Hour:{0:03}".format(Hour),1, Black)
            screen.blit(DayFont, DayFontR)

            pygame.display.flip()

    Clock.tick(60) # ensures a maximum of 60 frames per second

pygame.quit()
