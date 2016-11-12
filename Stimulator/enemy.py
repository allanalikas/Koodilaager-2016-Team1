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


    def update(self,player):
        if self.x > player.x:
            self.x -= self.x_speed
        elif self.x < player.x:
            self.x += self.x_speed
        # Movement along y direction
        if self.y < player.y:
            self.y += self.y_speed
        elif self.y > player.y:
            self.y -= self.y_speed
