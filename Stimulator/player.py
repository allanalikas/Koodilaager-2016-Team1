import pygame
from constants import *
from character import Character
from bullet import *
import math


class Player(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.angle = 0

        self.acc_x = 0
        self.acc_y = 0

        self.max_acc = 0.7
        self.max_speeed = 9

        # self.player_icon_down = pygame.image.load("girl.down.png")
        # self.plyer.icon_up = pygame.image.load("girl.up.png")
        self.icon = pygame.image.load("girl.left.png")
        # self.player_icon_right = pygame.image.load("girl.right.png")

        # self.player_icon_down_right = pygame.image.load("girl.down.right.png")
        # self.player_icon_up_right = pygame.image.load("girl.up.right.png")
        # self.player_icon_down_left = pygame.image.load("girl.down.left.png")
        # self.player_icon_up_left = pygame.image.load("girl.right.left.png")

        # self.icon = self.player_icon_down
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])

    def on_event(self, event, bullet_list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.shoot(event.pos, bullet_list)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.acc_y = -self.max_acc
                # self.icon = (self.player_icon_up)
                self.y_speed = -5

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.acc_x = -self.max_acc
                # self.icon = self.player_icon_left
                self.x_speed = -5

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.acc_x = self.max_acc
                # self.icon = self.player_icon_right
                self.x_speed = 5

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.acc_y = self.max_acc
                # self.icon = self.player_icon_down
                self.y_speed = 5

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

    """if event.key == pygame.K_UP and pygame.K_RIGHT:
        self.acc_y = 0
        self.acc_x = 0
        self.y_speed = 0
        self.x_speed = 0"""

    def shoot(self, mouse_pos, bullet_list):
        h = math.sqrt((math.pow( -(screen_w/2 - mouse_pos[0]), 2 )) +
                      (math.pow( -(screen_h / 2 - mouse_pos[1]), 2)))
        print(h)
        vel_x = (-(screen_w/2 - mouse_pos[0])) / h
        vel_y = (-(screen_h/2 - mouse_pos[1])) / h
        print(vel_x, vel_y)
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

        """self.x += self.x_speed
        self.y += self.y_speed"""
        self.rect.x = self.x
        self.rect.y = self.y

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = screen_w / 2 - mouse_pos[0]
        mouse_y = screen_h/2 - mouse_pos[1]
        mousa_x = abs(mouse_x)
        mousa_y = abs(mouse_y)

        if mouse_x > 0 > mouse_y:
            self.angle = math.atan(mousa_y/mousa_x) / (2 * math.pi) * 360
        elif mouse_x < 0 and mouse_y < 0:
            self.angle = 90 + math.atan(mousa_x/mousa_y) / (2 * math.pi) * 360
        elif mouse_x < 0 < mouse_y:
            self.angle = 180 + math.atan(mousa_y/mousa_x) / (2 * math.pi) * 360
        elif mouse_x > 0 and mouse_y > 0:
            self.angle = 270 + math.atan(mousa_x/mousa_y) / (2 * math.pi) * 360

    def draw(self, screen, cam_pos):
        surf = pygame.transform.rotate(self.icon, self.angle)
        saiz = surf.get_rect().size
        screen.blit(surf, [screen_w/2 - saiz[0]/2, screen_h/2 - saiz[1]/2])

    def collide(self, wall_list, dx, dy):
        rect = pygame.Rect([screen_w/2 - TILESIZE/2 + 5 + dx, screen_h/2-TILESIZE/2 + 5 + dy, TILESIZE - 10, TILESIZE - 10])

        index = rect.collidelist(wall_list)

        if index != -1:
            return True

        else:
            return False
