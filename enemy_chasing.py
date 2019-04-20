import pygame
import sys
import os
import math
import random

pygame.init()
pygame.display.init()


'''
Objects
'''
# put Python classes and functions here
class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames

        self.images = []
        img = pygame.image.load(os.path.join('images','characters.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()

    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
                self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
                self.image = self.images[self.frame//ani]

class Enemy(pygame.sprite.Sprite):
    '''
    Spawn an enemy
    '''
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.rect.x -= dx * 20
        self.rect.y -= dy * 20

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    ### now have to make two keys not overlap
    def random_location(self):
        location_set = [(100,100), (700,600), (200,700), (300, 400), (700, 100)]
        random_locations = random.sample(location_set, 1)
        first_location = random_locations[0]
        self.rect.x = first_location[0]
        self.rect.y = first_location[1]

    # def generate_keys(self):


'''
Setup
'''
BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)

worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 300   # go to x
player.rect.y = 200   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 5

key1 = Key(200, 300, "key1_small.png")
key1.random_location()
key_list = pygame.sprite.Group()
key_list.add(key1)

key2 = Key(500, 600, "key2_small.png")
key2.random_location()
key_list.add(key2)

enemy = Enemy(500,200,'slime.png')
enemy_list = pygame.sprite.Group()   # create enemy group
enemy_list.add(enemy)                # add enemy to group
# put run-once code here

'''
Main Loop
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
                enemy.move_towards_player(player)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
                enemy.move_towards_player(player)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
                enemy.move_towards_player(player)
            if event.key == pygame.K_DOWN or event.key == ord('w'):
                player.control(0, -steps)
                enemy.move_towards_player(player)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
                enemy.move_towards_player(player)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
                enemy.move_towards_player(player)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps)
                enemy.move_towards_player(player)
            if event.key == pygame.K_DOWN or event.key == ord('w'):
                player.control(0, steps)
                enemy.move_towards_player(player)



    world.blit(backdrop, backdropbox)
    key_list.draw(world)
    player.update()  # update player position
    player_list.draw(world) # draw player
    enemy_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
    pygame.display.update()
