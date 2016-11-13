import pygame
from constants import *

class Bullet():
    def __init__(self, x, y, x_vel, y_vel):
        self.dead = False
        self.pos = [x+25, y+20]
        self.vel = [(x_vel)*0.1, (y_vel)*0.1]
        self.icon = pygame.image.load ("bullet.png")
        self.speed = 30

    def update(self,map_data):
        self.pos[0] += self.vel[0] * self.speed
        self.pos[1] += self.vel[1] * self.speed
        print(self.pos)
        self.collide(map_data)


    def draw(self, screen, cam_pos):
        pygame.draw.circle(screen, [255, 0, 0], [int(self.pos[0]-cam_pos[0]), int(self.pos[1]-cam_pos[1])], 3)
    def collide(self, map_data):
        tile_x = int(self.pos[0] // TILESIZE)
        tile_y = int(self.pos[1] // TILESIZE)
        print(tile_x,tile_y)
        try:
            if map_data[tile_y][tile_x] != 0:
                self.dead = True
                self.vel = [0,0]
        except:
            pass


