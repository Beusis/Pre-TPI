# Pygame Pynvaders
#
# Author : Loik Meylan
# Version : 1.0
# Date : 28.02.2023
#
# Implémentation du fichier principal du projet,
# il contiendra les liaisons aux autres fichiers ainsi que le démarrage du jeux.

import pygame
from  pygame.locals import *
from random import randint, seed
from enum import Enum, auto

class App:
    def __init__(self):
        self.size = (1280, 720)
        self._running = True



    def on_init(self):
        pygame.init()
        pygame.event.set_allowed([QUIT, KEYDOWN])
        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._Background = pygame.image.load(r'C:\Users\loik.meylan\Documents\GitHub\Pre-TPI\Pynvaders\Content\heic1304c.jpg').convert()
        self._display.blit(self._Background, (0, 0))
        pygame.display.flip()

    def start_game(self):
        while self._running:
            self.on_init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if True:
    App().start_game()
