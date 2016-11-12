import pygame
from constants import *
from character import Character


class Player(Character):
    def __init__(self, x, y, player_icon):
        self.x = x
        self.y = y
        self.icon = player_icon
        
    def on_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.icon, [screen_w/2 -25, screen_h/2 -25])
