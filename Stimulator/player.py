import pygame
from constants import *
from character import Character

character_icon = pygame.image.load("player.jpg")

class Player(Character):
    def __init__(self, x, y, character_icon):
        self.x = x
        self.y = y
        
    def on_event(self, event):

    def update(self):

    def draw(self, screen):
        Player = screen.blit(character_icon, )
