import sys
import pygame
from pygame.locals import *
from random import randint, seed
from enum import Enum, auto


class Player():
    def __init__(self):
        self.speed = 0
        self._Display = None
        self.sprite = None
        self.rect = None
        self.size = (1280, 720)

    def on_init(self):
        self.on_render()

    def on_render(self):
        self._Display = pygame.display.set_mode(self.size)
        self.sprite = pygame.image.load(r'C:\Users\loik.meylan\Documents\GitHub\Pre-TPI\Pynvaders\Content\main-spritesheet.png').convert()
        self.rect = pygame.Rect(152, 1, 21, 21)
        self._Display = pygame.Surface.blit(self.sprite, self._Display, (152, 1, 21, 21))
