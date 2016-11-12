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
        self.rect = pygame.Rect(self.x, self.y, TILESIZE, TILESIZE)
        
    def on_event(self, event):
        #print(self.x, self.y, self.rect)
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

    def update(self, rect_list):
        if self.x_speed != 0:
            if not self.collide(rect_list, self.x_speed, 0):
                self.x += self.x_speed

        if self.y_speed != 0:
            if not self.collide(rect_list, 0, self.y_speed):
                self.y += self.y_speed

        # self.x += self.x_speed
        # self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self, screen, cam_pos):
        screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1]])

    def collide(self, wall_list, dx, dy):
        rect = pygame.Rect([screen_w/2 - TILESIZE/2 + dx, screen_h/2-TILESIZE/2 + dy, TILESIZE, TILESIZE])

        index = rect.collidelist(wall_list)

        if index != -1:
            return True

        else:
            return False