import pygame, sys
from constants import *

MAPX = screen_w // TILESIZE
MAPY = screen_h // TILESIZE

BLACK = (0,0,0)
WHITE = (255, 255, 255)

WALL = "#"
GROUND = " "

colours ={
        WALL : BLACK,
        GROUND : WHITE
         }

MAP_W = 22

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


'''
def init(map_nr):

    if map_nr == 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for row in range(MAPX):
                print("jouab")
                for column in range(MAPY):
                    print("jouab2")
                    pygame.draw.rect(DISPLAYSURF, colours[map1[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
        
            pygame.display.update()
init(1)
'''
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
                pygame.draw.rect(s, [0, 0, 0], tile_rect)

            elif value == '#':
                pygame.draw.rect(s, [255, 255, 255], tile_rect)
