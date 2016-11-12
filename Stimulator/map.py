import pygame, sys
from constants import *
from math import floor

MAPX = screen_w // TILESIZE
MAPY = screen_h // TILESIZE

"""
WALL = "#"
GROUND = " "
COUCH = "C"
"""

map1 = open("map_files/map1.data", "r")
map1_width = int(map1.readline().strip())

rectangle_list = []


def read_map(map_data):
    map_list = []
    row = 0
    column = 0

    for line in map_data:
        map_list.append([])
        for letter in line:
            if letter == ' ':
                map_list[row].append(0)

            elif letter == '#':
                map_list[row].append(1)

        row += 1

    return map_list


def return_values(map, x1, x2, y):
    if y < 0 or y >= len(map):
        return [0 for i in range(x2-x1)]

    elif x1 < 0:
        return [0 for i in range(0 - x1)] + map[y][:x2]

    elif x2 >= len(map):
        return map[y][x1:] + [0 for i in range(x2 - len(map) - 1)]

    else:
        return map[y][x1:x2]


map1_data = read_map(map1)


def get_rect_list():
    return rectangle_list


def draw(s, cam_pos):
    global rectangle_list

    tiles_x = screen_w // TILESIZE + 1
    tiles_y = screen_h // TILESIZE + 1

    cam_tiles_x = int(cam_pos[0] // TILESIZE)
    cam_tiles_y = int(cam_pos[1] // TILESIZE)

    cam_offset_x = int(cam_pos[0] % TILESIZE)
    cam_offset_y = int(cam_pos[1] % TILESIZE)

    subsection = [return_values(map1_data, cam_tiles_x, cam_tiles_x+tiles_x, j)
                  for j in range(cam_tiles_y, cam_tiles_y + tiles_y)]

    #print(subsection)

    rectangle_list = []

    for y, j in enumerate(subsection):
        for x, i in enumerate(j):
            #print(i, x, y)
            if i == 1:
                rect = pygame.Rect([x*TILESIZE - cam_offset_x,
                       y*TILESIZE - cam_offset_y,
                       TILESIZE,
                       TILESIZE])

                pygame.draw.rect(s, [0, 255, 0], rect)

                rectangle_list.append(rect)
