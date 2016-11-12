import pygame, sys
from constants import *

MAPX = screen_w // TILESIZE
MAPY = screen_h // TILESIZE
MAP_W = 22

"""
WALL = "#"
GROUND = " "
COUCH = "C"
"""

map1 =   """
######################
#                    #
#        #           #
#        #           #
#        #           #
####### ##############
#                    #
#                    #
#                    #
#                    #
######################"""

map1 = map1.replace('\n', '')

def draw(s, cam_pos):
    x = 5
    y = 3
    print(map1[y*MAP_W + x])

    cam_tiles_x = cam_pos[0] // TILESIZE
    cam_tiles_y = cam_pos[1] // TILESIZE

    cam_offset_x = cam_pos[0] % TILESIZE
    cam_offset_y = cam_pos[1] % TILESIZE

    for j in range(MAPY):
        for i in range(MAPX):
            try:
                value = map1[(j+cam_tiles_y)*MAP_W + i+ cam_tiles_x]
            except:
                value = ' '

            tile_rect = pygame.Rect((i) * TILESIZE - cam_offset_x,
                                    (j) * TILESIZE - cam_offset_y,
                                    TILESIZE,
                                    TILESIZE)

            if value == ' ':
                pygame.draw.rect(s, [255, 255, 255], tile_rect)

            elif value == '#':
                pygame.draw.rect(s, [0, 0, 0], tile_rect)

            elif value == 'C':
                pygame.draw.rect(s, [255, 255, 0], tile_rect)
