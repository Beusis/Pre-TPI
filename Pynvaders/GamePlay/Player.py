import sys
import pygame
from pygame.locals import *
from random import randint, seed
from enum import Enum, auto


class Player():
    def __init__(self):
        self.speed = 0
        self._Display = None
        self.sprite = pygame.image.load("./Content/main-spritesheet.png").convert()
        self.rect = pygame.Rect(152, 1, 21, 21)
        self.handle_surface = None
        self.clipRect = None
        self.image = None

    def on_init(self):
        self.clip()
        self.on_render()

    def on_render(self):
        pass
       # self.rect =

    def clip(self):  # Get a part of the image
        self.handle_surface = self.sprite.copy()  # Sprite that will get process later
        self.clipRect = self.rect  # Part of the image
        self.handle_surface.set_clip(self.clipRect)  # Clip or you can call cropped
        self.image = self.sprite.subsurface(self.handle_surface.get_clip())  # Get subsurface
        return self.image.copy()  # Return
