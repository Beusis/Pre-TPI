# Pygame Pynvaders
#
# Author : Loik Meylan
# Version : 1.0
# Date : 28.02.2023
#
# Implémentation du fichier principal du projet,
# il contiendra les liaisons aux autres fichiers ainsi que le démarrage du jeux.

import sys
import pygame
from pygame.locals import *
import GamePlay.Player
from random import randint, seed


class App:
    def __init__(self):
        self.size = (1280, 720)
        self._running = True
        self._Display = None
        self._Background = None
        self.player = None

    def on_init(self):
        pygame.init()
        pygame.event.set_allowed([QUIT, KEYDOWN])
        self._Display = pygame.display.set_mode(self.size)
        self._Background = pygame.image.load(r'C:\Users\loik.meylan\Documents\GitHub\Pre-TPI\Pynvaders\Content\heic1304c.jpg').convert()
        self._Display.blit(self._Background, (0, 0))
        self.player = GamePlay.Player.Player()


    def on_loop(self):
        pygame.display.flip()

    def start_game(self):
        self.on_init()
        self.player.on_init()
        while self._running:
            self.on_loop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if True:
    App().start_game()
