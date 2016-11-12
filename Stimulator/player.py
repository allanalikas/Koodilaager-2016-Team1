import pygame
from constants import *
from character import Character


class Player(Character):
    def __init__(self, x, y, player_icon):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.icon = player_icon
        
    def on_event(self, event):
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                   self.y_speed = -5

               elif event.key == pygame.K_DOWN:
                   self.y_speed = 5
        
               elif event.key == pygame.K_LEFT:
                   self.x_speed = -5

               elif event.key == pygame.K_RIGHT:
                   self.x_speed = +5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.y_speed = 0

                elif event.key == pygame.K_DOWN:
                    self.y_speed = 0

                elif event.key == pygame.K_LEFT:
                    self.x_speed = 0

                elif event.key == pygame.K_RIGHT:
                    self.x_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.icon, [screen_w/2 -25, screen_h/2 -25])
