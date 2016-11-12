import pygame
from constants import *
from character import Character




class Player(Character):
    def __init__(self, x, y, player_icon):
        self.x = x
        self.y = y
        self.icon = player_icon
        
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            elif event.key == pygame.K_a:
                pass
            elif event.key == pygame.K_s:
                pass
            elif event.key == pygame.K_d:
                pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.icon, [screen_w/2, screen_h/2])
