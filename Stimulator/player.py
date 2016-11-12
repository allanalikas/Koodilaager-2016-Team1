import pygame
from constants import *
from character import Character


class Player(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.player_icon_down = pygame.image.load("girl.down.png")
        self.player_icon_up = pygame.image.load("girl.up.png")
        self.player_icon_left = pygame.image.load("girl.left.png")
        self.player_icon_right = pygame.image.load("girl.right.png")

        #self.player_icon_down_right = pygame.image.load("girl.down.right.png")
        #self.player_icon_up_right = pygame.image.load("girl.up.right.png")
        #self.player_icon_down_left = pygame.image.load("girl.down.left.png")
        #self.player_icon_up_left = pygame.image.load("girl.right.left.png")

        self.icon = self.player_icon_down
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP or event.key == pygame.K_w:
               self.y_speed = -10
               self.icon = (self.player_icon_up)

           elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
               self.x_speed = -10
               self.icon = (self.player_icon_left)

           elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               self.x_speed = +10
               self.icon = (self.player_icon_right)

           elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
               self.y_speed = 10
               self.icon = (self.player_icon_down)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.y_speed = 0

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.y_speed = 0

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.x_speed = 0

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
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
        screen.blit(self.icon, [self.x - cam_pos[0], self.y - cam_pos[1] - 30])

    def collide(self, wall_list, dx, dy):
        rect = pygame.Rect([screen_w/2 - TILESIZE/2 + 5 + dx, screen_h/2-TILESIZE/2 + 5 + dy, TILESIZE - 10, TILESIZE - 10])

        index = rect.collidelist(wall_list)

        if index != -1:
            return True

        else:
            return False