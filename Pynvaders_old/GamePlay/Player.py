import sys
import pygame
from pygame.locals import *
from random import randint, seed
#from . import LaserShot


class Player:
    def __init__(self):  #
        self.speed = 0.4
        self._Display = None
        self.image = pygame.image.load("./Content/main-spritesheet.png").convert_alpha()
        self.sheet_position = pygame.Rect(152, 1, 21, 21)
        self.position = [349, 400]
        self.handle_surface = None
        self.sprite = None
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(60)
        self.limit = [21, 678]
        self.hitbox = None
        self.laser = None
        #self.laser_shot = LaserShot()

    def on_init(self):
        self.clip()

    def on_render(self):
        self.movement()

# The code of the function "clip" comes from StackOverflow,
# from user "DaFluffyPotato" : https://stackoverflow.com/questions/38535330/load-only-part-of-an-image-in-pygame
    def clip(self):  # Get a part of the image
        self.handle_surface = self.image.copy()  # Sprite that will get process later
        self.handle_surface.set_clip(self.sheet_position)  # Clip or you can call cropped
        self.sprite = self.image.subsurface(self.handle_surface.get_clip())  # Get subsurface
        self.hitbox = self.sprite.get_rect()
        return self.sprite.copy(), self.hitbox  # Return

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed * self.delta_time
        elif keys[pygame.K_RIGHT]:
            self.position[0] += self.speed * self.delta_time

        if self.position[0] < self.limit[0]:
            self.position[0] = self.limit[0]
        elif self.position[0] > self.limit[1]:
            self.position[0] = self.limit[1]

    def fire(self):
        self.laser = LaserShot()
#        laser.get_position(LaserShot, self.position)
#        laser.movement()

    def laser_movement(self):
        self.laser.movement()

class LaserShot:

    def __init__(self):
        self.laser_speed = 0.5
        self.boundaries = [8, 472]
        self.laser_image = pygame.image.load("./Content/Laser.png").convert_alpha()
        self.sheet = pygame.Rect(0, 0, 1, 8)
        self.laser_position = []
        self.surface = None
        self.laser_sprite = None
        self.laser_hitbox = None
        self.player = Player()

    def on_init(self):
        self.clip()

    def clip(self):
        self.surface = self.laser_image.copy()
        self.surface.set_clip(self.sheet)
        self.laser_sprite = self.laser_image.subsurface(self.surface.get_clip())
        self.laser_hitbox = self.laser_sprite.get_rect()
        return self.laser_sprite.copy(), self.laser_hitbox

    def in_bounds(self):
        return True if self.boundaries[0] > self.laser_position[1] > self.boundaries[1] else False

    def fire(self):
        self.movement()

    def movement(self):

        while self.in_bounds():
            self.laser_position[1] -= self.laser_speed * self.player.delta_time
        #del self.sprite, self.hitbox

    def get_position(self, position):
        self.laser_position = position
        self.laser_position[1] += 25
        return self.laser_position
