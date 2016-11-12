import pygame
from constants import *
from character import Character


class Player(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.player_icon_down = pygame.image.load("guy.down1.png")
        self.player_icon_up = pygame.image.load("Guy.up.png")
        self.player_icon_left = pygame.image.load("Guy.left.png")
        self.player_icon_right = pygame.image.load("guy.right1.png")

        self.icon = self.player_icon_down
    def on_event(self, event):
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP or event.key == pygame.K_w:
                   self.icon = (self.player_icon_up)
                   self.y_speed = -5

               elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                   self.icon = (self.player_icon_down)
                   self.y_speed = 5

               elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                   self.icon = (self.player_icon_left)
                   self.x_speed = -5

               elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                   self.icon = (self.player_icon_right)
                   self.x_speed = +5

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.y_speed = 0

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.y_speed = 0

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.x_speed = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.x_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.icon, [screen_w/2 -25, screen_h/2 -25])