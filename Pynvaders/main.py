# Pygame Pynvaders
#
# Author : Loik Meylan
# Version : 1.0_old
# Date : 28.02.2023
#
# Space Invaders with pygame

import sys
import pygame
from pygame.locals import *
import GamePlay.Player
from pathlib import Path
import os


# The code structure is heavily inspired by pySnake.py by Julien Ithurbide
class App:
    _Background = None

    def __init__(self):
        self.size = (720, 480)
        self._running = True
        self._Display = None
        self.player = None
        self.laser = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        script_dir = Path(__file__).parent.absolute()
        full_path = os.path.join(script_dir, r"Content\back.png")

        pygame.init()
        pygame.event.set_allowed([QUIT, KEYDOWN])

        self._Display = pygame.display.set_mode(self.size)
        self._Background = pygame.image.load(full_path)

    def on_render(self):
        self.player = GamePlay.Player.Player()

    def on_loop(self):
        self._Display.blit(self._Background, [0, 0])
        self._Display.blit(self.player.sprite, self.player.position)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        self.player.on_render()
        self.clock.tick(60)

    def start_game(self):
        self.on_init()
        self.on_render()
        self.player.on_init()
        while self._running:
            self.on_loop()


if True:
    App().start_game()
