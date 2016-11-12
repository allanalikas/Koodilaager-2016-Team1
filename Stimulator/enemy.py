<<<<<<< HEAD
import pygame
from character import Character
from constants import *


class Enemy(Character):
    def __init__(self, x, y, player_icon):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.icon = player_icon

    def draw(self, screen, cam_pos):
        screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])
=======
>>>>>>> 80011f574ff578e743c901937a520f117d6620c4
