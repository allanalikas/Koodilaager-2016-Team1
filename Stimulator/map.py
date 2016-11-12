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
    cam_tiles_x = cam_pos[0] // TILESIZE
    cam_tiles_y = cam_pos[1] // TILESIZE

    cam_offset_x = cam_pos[0] % TILESIZE
    cam_offset_y = cam_pos[1] % TILESIZE

    for j in range(MAPY):
        for i in range(MAPX):
            try:
                if int((j+cam_tiles_y)*MAP_W + i + cam_tiles_x) >= 0:
                    value = map1[int((j+cam_tiles_y)*MAP_W + i + cam_tiles_x)]
                else:
                    value = ' '
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
