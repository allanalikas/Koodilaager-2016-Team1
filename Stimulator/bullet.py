import pygame

class Bullet():
    def __init__(self, x, y, x_vel, y_vel):
        self.dead = False
        self.pos = [x, y]
        self.vel = [x_vel, y_vel]
        self.icon = pygame.image.load ("bullet.png")

    def update(self, rect_list):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self, screen, cam_pos):
        pygame.draw.circle(screen, [255, 0, 0], [int(self.pos[0]-cam_pos[0]), int(self.pos[1]-cam_pos[1])], 3)
