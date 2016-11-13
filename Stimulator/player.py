import pygame
from constants import *
from character import Character
from bullet import *

class Player(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.acc_x = 0
        self.acc_y = 0

        self.max_acc = 0.2
        self.max_speeed = 5

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

    def on_event(self, event, bullet_list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.shoot(event.pos, bullet_list)

        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP or event.key == pygame.K_w:
               self.acc_y = -self.max_acc
               self.icon = (self.player_icon_up)

           elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
               self.acc_x = -self.max_acc
               self.icon = (self.player_icon_left)

           elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               self.acc_x = self.max_acc
               self.icon = (self.player_icon_right)

           elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
               self.acc_y = self.max_acc
               self.icon = (self.player_icon_down)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.acc_y = 0
                self.y_speed = 0

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.acc_y = 0
                self.y_speed = 0

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.acc_x = 0
                self.x_speed = 0

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.acc_x = 0
                self.x_speed = 0

    def shoot(self, mouse_pos, bullet_list):
        vel_x = -(screen_w/2 - mouse_pos[0])
        vel_y = -(screen_h/2 - mouse_pos[1])

        bullet_list.append(Bullet(self.x, self.y, vel_x, vel_y))

    def update(self, rect_list):
        if abs(self.x_speed) < self.max_speeed:
            self.x_speed += self.acc_x

        if abs(self.y_speed) < self.max_speeed:
            self.y_speed += self.acc_y

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