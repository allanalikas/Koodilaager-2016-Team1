import pygame
from character import Character
from constants import *


class Enemy(Character):
    def __init__(self, x, y, enemy_icon):
        self.x = x
        self.y = y
        self.x_speed = 1
        self.y_speed = 1
        self.icon = enemy_icon

    def draw(self, screen, cam_pos):
        screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])

    def update(self, player, map_data):
        tile_x = self.x // TILESIZE
        tile_y = self.y // TILESIZE

        # left = 1, up = 2, right = 3, down = 4
        possible_dirs = []

        if map_data[tile_y][tile_x-1] == 0:
            possible_dirs.append(1)

        if map_data[tile_y-1][tile_x] == 0:
            possible_dirs.append(2)

        if map_data[tile_y][tile_x+1] == 0:
            possible_dirs.append(3)

        if map_data[tile_y+1][tile_x] == 0:
            possible_dirs.append(4)

        if self.x > player.x and 1 in possible_dirs:
            self.x -= self.x_speed

        if self.x < player.x and 3 in possible_dirs:
            self.x += self.x_speed
        # Movement along y direction
        if self.y < player.y and 4 in possible_dirs:
            self.y += self.y_speed
        elif self.y > player.y and 2 in possible_dirs:
            self.y -= self.y_speed
