import sys
import pygame
from pygame.locals import *
from random import randint, seed
from enum import Enum, auto


class Player:
    def __init__(self):
        self.speed = 0.3
        self._Display = None
        self.sprite = pygame.image.load("./Content/main-spritesheet.png").convert()
        self.rect = pygame.Rect(152, 1, 21, 21)
        self.position = pygame.Rect(349, 400, 21, 21)
        self.handle_surface = None
        self.clipRect = None
        self.image = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        self.clip()

    def on_render(self):
        self.movement()

    def clip(self):  # Get a part of the image
        self.handle_surface = self.sprite.copy()  # Sprite that will get process later
        self.clipRect = self.rect  # Part of the image
        self.handle_surface.set_clip(self.clipRect)  # Clip or you can call cropped
        self.image = self.sprite.subsurface(self.handle_surface.get_clip())  # Get subsurface
        return self.image.copy()  # Return

    def movement(self):

        keys = pygame.key.get_pressed()
        dt = self.clock.tick(60)

        if keys[pygame.K_LEFT]:
            # self.speed[0] = -30
            self.position[0] -= self.speed * dt
        elif keys[pygame.K_RIGHT]:
            # self.speed[0] = 30
            self.position[0] += self.speed * dt
