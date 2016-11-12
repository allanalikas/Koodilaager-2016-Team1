import pygame
from constants import *
from character import Character

player_icon = pygame.image.load("player.jpg")

class Player(Character):
    def __init__(self, x, y, character_icon):
        self.x = x
        self.y = y
        
    def on_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        Player = screen.blit(player_icon, screen_h/2, screen_w/2)
