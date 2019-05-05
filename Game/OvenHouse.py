"""

"""

import configparser
import pygame
import pygame.locals as pg
import random
import math

import show_text as st
import choose_char as cc
import end_game as eg
import open_scene as os

# Motion offsets for particular directions
#     N  E  S   W
DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

# Dimensions of the map tiles
MAP_TILE_WIDTH, MAP_TILE_HEIGHT = 24, 16

class SortedUpdates(pygame.sprite.RenderUpdates):
    """A sprite group that sorts them by depth."""

    def sprites(self):
        """The list of sprites in the group, sorted by depth."""

        return sorted(list(self.spritedict.keys()), key=lambda sprite: sprite.depth)


class TileCache(object):
    """Load the tilesets lazily into global cache"""

    def __init__(self,  width=32, height=None):
        self.width = width
        self.height = height or width
        self.cache = {}

    def __getitem__(self, filename):
        """Return a table of tiles, load it from disk if needed."""

        key = (filename, self.width, self.height)
        try:
            return self.cache[key]
        except KeyError:
            tile_table = self._load_tile_table(filename, self.width,
                                               self.height)
            self.cache[key] = tile_table
            return tile_table

    def _load_tile_table(self, filename, width, height):
        """Load an image and split it into tiles."""

        image = pygame.image.load(filename).convert_alpha()
        image_width, image_height = image.get_size()
        tile_table = []
        for tile_x in range(0, image_width // width):
            line = []
            tile_table.append(line)
            for tile_y in range(0, image_height // height):
                rect = (tile_x*width, tile_y*height, width, height)
                line.append(image.subsurface(rect))
        return tile_table

class Sprite(pygame.sprite.Sprite):
    """Sprite for animated items and base class for Player."""

    is_player = False

    def __init__(self, pos=(0, 0), frames=None):
        super(Sprite, self).__init__()
        if frames:
            self.frames = frames
        self.image = self.frames[0][0]
        self.rect = self.image.get_rect()
        self.animation = self.stand_animation()
        self.pos = pos

    def _get_pos(self):
        """Check the current position of the sprite on the map."""

        return ((self.rect.midbottom[0] - 12) // 24,
                (self.rect.midbottom[1] - 16) // 16)

    def _set_pos(self, pos):
        """Set the position and depth of the sprite on the map."""

        self.rect.midbottom = pos[0]*24+12, pos[1]*16+16
        self.depth = self.rect.midbottom[1]

    pos = property(_get_pos, _set_pos)

    def move(self, dx, dy):
        """Change the position of the sprite on screen."""

        self.rect.move_ip(dx, dy)
        self.depth = self.rect.midbottom[1]

    def stand_animation(self):
        """The default animation."""

        while True:
            # Change to next frame every two ticks
            for frame in self.frames[0]:
                self.image = frame
                yield None
                yield None

    def update(self, *args):
        """Run the current animation."""

        next(self.animation)

class Exit(Sprite):

    def __init__(self, pos=(5, 1)):
        self.frames = SPRITE_CACHE["door.png"]
        Sprite.__init__(self, pos)
        self.direction = 0
        self.animation = None
        self.image = self.frames[self.direction][0]

    def update(self, *args):
        """Updates "animation" of door"""

        if self.animation is None:
            self.image = self.frames[0][0]
        else:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None

class Key(Sprite):

    def __init__(self, pos=(3, 1),key_pic = 1):
        if key_pic == 1:
            self.frames = SPRITE_CACHE["key1_small.png"]
        if key_pic == 2:
            self.frames = SPRITE_CACHE["key2_small.png"]
        Sprite.__init__(self, pos)
        self.direction = 0
        self.animation = None
        self.image = self.frames[self.direction][0]

    def update(self, *args):
        """Updates "animation" of key"""

        if self.animation is None:
            self.image = self.frames[0][0]
        else:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None

class Enemy(Sprite):

    def __init__(self, pos=(2, 1)):
        self.frames = SPRITE_CACHE["fire.png"]
        Sprite.__init__(self, pos)
        self.direction = 0
        self.animation = None
        self.image = self.frames[self.direction][0]

    def walk_animation(self):
        """Animation for the enemy walking."""

        # This animation is hardcoded for 4 frames and 16x24 map tiles
        for frame in range(0,3):
            self.image = self.frames[0][frame]
            yield None
            self.move(DX[self.direction], DY[self.direction])
            yield None
            self.move(DX[self.direction], DY[self.direction])

    def update(self, *args):
        """Run the current animation or just stand there if no animation set."""

        if self.animation is None:
            self.image = self.frames[0][0]
        else:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None

class Witch(Sprite):

    def __init__(self, pos=(4, 1)):
        self.frames = SPRITE_CACHE["witch.png"]
        Sprite.__init__(self, pos)
        self.direction = 2
        self.animation = None
        self.image = self.frames[self.direction][0]

    def update(self, *args):
        """Run the current animation or just stand there if no animation set."""

        if self.animation is None:
            self.image = self.frames[self.direction][0]
        else:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None

    def move_towards_player(self):
        for frame in range(4):
            self.image = self.frames[self.direction][frame]
            yield None
            self.move(2*DX[self.direction], DY[self.direction])
            yield None
            self.move(2*DX[self.direction], DY[self.direction])


class Player(Sprite):
    """ Display and animate the player character."""

    is_player = True
    initial_screen =os.main()
    which_player = cc.main()

    def __init__(self, pos=(1, 1)):
        if self.which_player == 1:
            self.frames = SPRITE_CACHE["player.png"]
        if self.which_player == 2:
            self.frames = SPRITE_CACHE["player2.png"]
        Sprite.__init__(self, pos)
        self.direction = 2
        self.animation = None
        self.image = self.frames[self.direction][0]

    def walk_animation(self):
        """Animation for the player walking."""

        # This animation is hardcoded for 4 frames and 16x24 map tiles
        for frame in range(4):
            self.image = self.frames[self.direction][frame]
            yield None
            self.move(3*DX[self.direction], 2*DY[self.direction])
            yield None
            self.move(3*DX[self.direction], 2*DY[self.direction])

    def update(self, *args):
        """Run the current animation or just stand there if no animation set."""

        if self.animation is None:
            self.image = self.frames[self.direction][0]
        else:
            try:
                next(self.animation)
            except StopIteration:
                self.animation = None

class Level(object):
    """Load and store the map of the level, together with all the items."""

    def __init__(self, which_level,filename="level.map"):
        self.tileset = ''
        self.map = []
        self.items = {}
        self.key = {}
        self.width = 0
        self.height = 0
        self.whichlevel = which_level
        print(self.whichlevel)
        self.load_file(filename)

    def load_file(self, filename="level.map"):
        """Load the level from specified file."""

        parser = configparser.ConfigParser()
        parser.read(filename)
        self.tileset = parser.get(self.whichlevel, "tileset")
        self.map = parser.get(self.whichlevel, "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.map[0])
        self.height = len(self.map)
        for y, line in enumerate(self.map):
            for x, c in enumerate(line):
                if not self.is_wall(x, y) and 'sprite' in self.key[c]:
                    self.items[(x, y)] = self.key[c]

    def render(self):
        """Draw the level on the surface."""

        wall = self.is_wall
        tiles = MAP_CACHE[self.tileset]
        image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
        overlays = {}
        for map_y, line in enumerate(self.map):
            for map_x, c in enumerate(line):
                if wall(map_x, map_y):
                    # Draw different tiles depending on neighbourhood
                    if not wall(map_x, map_y+1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            tile = 1, 2
                        elif wall(map_x+1, map_y):
                            tile = 0, 2
                        elif wall(map_x-1, map_y):
                            tile = 2, 2
                        else:
                            tile = 3, 2
                    else:
                        if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
                            tile = 1, 1
                        elif wall(map_x+1, map_y+1):
                            tile = 0, 1
                        elif wall(map_x-1, map_y+1):
                            tile = 2, 1
                        else:
                            tile = 3, 1
                    # Add overlays if the wall may be obscuring something
                    if not wall(map_x, map_y-1):
                        if wall(map_x+1, map_y) and wall(map_x-1, map_y):
                            over = 1, 0
                        elif wall(map_x+1, map_y):
                            over = 0, 0
                        elif wall(map_x-1, map_y):
                            over = 2, 0
                        else:
                            over = 3, 0
                        overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
                else:
                    try:
                        tile = self.key[c]['tile'].split(',')
                        tile = int(tile[0]), int(tile[1])
                    except (ValueError, KeyError):
                        # Default to ground tile
                        tile = 0, 3
                tile_image = tiles[tile[0]][tile[1]]
                image.blit(tile_image,
                           (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
        return image, overlays

    def get_tile(self, x, y):
        """Tell what's at the specified position of the map."""

        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}

    def get_bool(self, x, y, name):
        """Tell if the specified flag is set for position on the map."""

        value = self.get_tile(x, y).get(name)
        return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

    def is_wall(self, x, y):
        """Is there a wall?"""

        return self.get_bool(x, y, 'wall')

    def is_blocking(self, x, y):
        """Is this place blocking movement?"""

        if not 0 <= x < self.width or not 0 <= y < self.height:
            return True
        return self.get_bool(x, y,  'block')

class Game(object):
    """The main game object."""

    def __init__(self):
        self.current = 'level1'
        self.last = 'level3'
        self.screen = pygame.display.get_surface()
        self.pressed_key = None
        self.game_over = False
        self.sprites = SortedUpdates()
        self.overlays = pygame.sprite.RenderUpdates()
        self.use_level(Level(self.current))
        for i in range(len(self.keynum)):
            self.key[i].gotKey = False

    def use_level(self, level):
        """Set the level as the current one."""

        self.sprites = SortedUpdates()
        self.overlays = pygame.sprite.RenderUpdates()
        self.level = level
        self.enemynum = []
        self.keynum = []
        # Populate the game with the level's objects
        for pos, tile in level.items.items():
            if tile.get("player") in ('true', '1', 'yes', 'on'):
                sprite = Player(pos)
                self.player = sprite
            elif tile.get("enemy") in ('true', '1', 'yes', 'on'):
                sprite = Enemy(pos)
                self.enemynum += [sprite]
                self.enemy = self.enemynum
            elif tile.get("key") in ('true', '1', 'yes', 'on'):
                key_pic = 1
                sprite = Key(pos, key_pic)
                self.keynum += [sprite]
                self.key = self.keynum
            elif tile.get("key") in ('true', '2', 'yes', 'on'):
                key_pic = 2
                sprite = Key(pos, key_pic)
                self.keynum += [sprite]
                self.key = self.keynum
            elif tile.get("witch") in ('true', '1', 'yes', 'on'):
                sprite = Witch(pos)
                self.witch = sprite
            elif tile.get("exit") in ('true', '2', 'yes', 'on'):
                sprite = Exit(pos)
                self.exit = sprite
            else:
                sprite = Sprite(pos, SPRITE_CACHE[tile["sprite"]])
            self.sprites.add(sprite)

        # Render the level map
        self.background, overlays = self.level.render()
        # Add the overlays for the level map
        for (x, y), image in overlays.items():
            overlay = pygame.sprite.Sprite(self.overlays)
            overlay.image = image
            overlay.rect = image.get_rect().move(x*24, y*16-16)

    def witch_blocking(self,x,y):
        if not self.level.is_blocking(x+DX[self.witch.direction], y+DY[self.witch.direction]):
            self.witch.animation = self.witch.move_towards_player()

    def witch_move(self):
        x, y = self.witch.pos
        px, py = self.player.pos
        if x < px:
            self.witch.direction = 1
            self.witch_blocking(x,y)
        if x > px:
            self.witch.direction = 3
            self.witch_blocking(x,y)
        if y < py:
            self.witch.direction = 2
            self.witch_blocking(x,y)
        if y > py:
            self.witch.direction = 0
            self.witch_blocking(x,y)

    def enemy_walk(self,enemy):
        x,y = enemy.pos
        enemy.direction = enemy.de
        if not self.level.is_blocking(x+DX[enemy.de],y+DY[enemy.de]):
            enemy.animation = enemy.walk_animation()
            return enemy.de
        else:
            if enemy.de == 2:
                return 0
            elif enemy.de == 0:
                return 2
            elif enemy.de == 1:
                return 3
            elif enemy.de == 3:
                return 1

    def control(self):
        """Handle the controls of the game."""

        keys = pygame.key.get_pressed()

        def pressed(key):
            """Check if the specified key is pressed."""

            return self.pressed_key == key or keys[key]

        def walk(d):
            """Start walking in specified direction."""

            x, y = self.player.pos
            self.player.direction = d
            if not self.level.is_blocking(x+DX[d], y+DY[d]):
                self.player.animation = self.player.walk_animation()

        if pressed(pg.K_UP):
            walk(0)
        elif pressed(pg.K_DOWN):
            walk(2)
        elif pressed(pg.K_LEFT):
            walk(3)
        elif pressed(pg.K_RIGHT):
            walk(1)
        self.pressed_key = None

    def next_level(self):
        if self.current == 'level1':
            self.current = 'level2'
        elif self.current == 'level2':
            self.current = 'level3'
        self.use_level(Level(self.current))
        for i in range(len(self.keynum)):
            self.key[i].gotKey = False
        for i in range(len(self.enemynum)):
            self.enemy[i].de = random.randint(0,3)
        self.screen.blit(self.background, (0, 0))
        self.overlays.draw(self.screen)
        pygame.display.flip()

    def main(self):
        count = 0
        self.Second = 0
        self.Minute = 0
        self.Hour = 0

        White = (255, 255, 255)
        #Fonts
        Font = pygame.font.SysFont("Trebuchet MS", 25)

        #Day
        DayFont = Font.render("Hour:{0:03}".format(self.Hour),1, White) #zero-pad day to 3 digits
        DayFontR=DayFont.get_rect()
        DayFontR.center=(1285,100)
        #Hour
        HourFont = Font.render("Minute:{0:02}".format(self.Minute),1, White) #zero-pad hours to 2 digits
        HourFontR=HourFont.get_rect()
        HourFontR.center=(1385,100)
        #Minute
        MinuteFont = Font.render("Second:{0:02}".format(self.Second),1, White) #zero-pad minutes to 2 digits
        MinuteFontR=MinuteFont.get_rect()
        MinuteFontR.center=(1500,100)

        #Clock functioning
        Clock = pygame.time.Clock()
        CLOCKTICK = pygame.USEREVENT+1
        pygame.time.set_timer(CLOCKTICK, 1000)

        """Run the main loop."""
        for i in range(len(self.enemynum)):
            self.enemy[i].de = random.randint(0,3)
        clock = pygame.time.Clock()

        # Draw the whole screen initially
        self.screen.blit(self.background, (0, 0))
        self.overlays.draw(self.screen)
        pygame.display.flip()
        # The main game loop
        while not self.game_over:
            # Don't clear shadows and overlays, only sprites.
            self.sprites.clear(self.screen, self.background)
            self.sprites.update()
            # If the player's animation is finished, check for keypresses


            if self.player.animation is None:
                self.control()
                self.player.update()
            if self.witch.animation is None:
                self.witch_move()
                self.witch.update()
            if self.player.pos == self.witch.pos:
                print("Game over!")
                st.contact_witch(self.Second,self.Minute,self.Hour)
            for i in range(len(self.keynum)):
                if self.player.pos == self.key[i].pos and self.key[i].gotKey == False:
                    self.key[i].gotKey = True
                    count += 1
                if self.key[i].gotKey == True:
                    self.key[i].image = self.key[i].frames[1][0]
            for i in range(len(self.enemynum)):
                if self.player.pos == self.enemy[i].pos:
                    print('Game Over')
                    st.contact_fire(self.Second,self.Minute,self.Hour)
                elif self.enemy[i].animation is None:
                    self.enemy[i].de = self.enemy_walk(self.enemy[i])
                    self.enemy[i].update()
            if count == 2:
                if self.player.pos == self.exit.pos:
                    if self.current == self.last:
                        print('done')
                        st.win_game(self.Second,self.Minute,self.Hour)
                        exit()
                    self.next_level()
                    count = 0

            dirty = self.sprites.draw(self.screen)
            # Don't add ovelays to dirty rectangles, only the places where
            # sprites are need to be updated, and those are already dirty.
            self.overlays.draw(self.screen)
            # Update the dirty areas of the screen
            pygame.display.update(dirty)
            # Wait for one tick of the game clock

            clock.tick(15)
            # Process pygame events
            for event in pygame.event.get():
                if event.type == pg.QUIT:
                    self.game_over = True
                if event.type == CLOCKTICK: # count up the clock
                    #Timer
                    self.Second += 1
                    if self.Second == 60:
                        self.Minute+=1
                        self.Second=0
                    if self.Minute==60:
                        self.Hour+=1
                        self.Minute=0
                    # redraw time
                    MinuteFont = Font.render("Second:{0:02}".format(self.Second),1, White)
                    pygame.draw.rect(self.screen, (0, 0, 0),(1200, 50, 1000, 100))
                    self.screen.blit(MinuteFont, MinuteFontR)
                    HourFont = Font.render("Minute:{0:02}".format(self.Minute),1, White)
                    self.screen.blit(HourFont, HourFontR)
                    DayFont = Font.render("Hour:{0:03}".format(self.Hour),1, White)
                    self.screen.blit(DayFont, DayFontR)
                    pygame.display.flip()
                elif event.type == pg.KEYDOWN:
                    self.pressed_key = event



if __name__ == "__main__":
    SPRITE_CACHE = TileCache()
    MAP_CACHE = TileCache(MAP_TILE_WIDTH, MAP_TILE_HEIGHT)
    TILE_CACHE = TileCache(16, 24)
    pygame.mixer.music.load("Ovenhouse.ogg")
    pygame.mixer.music.play(-1) # repeat 5 times

    pygame.init()

    pygame.display.set_mode((1600, 600))
    Game().main()
