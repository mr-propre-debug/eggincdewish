#import des modules nécessaires pour faire fonctionner le jeu
import pygame, sys
from pygame.locals import *

class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        
        pygame.display.set_caption(self.title)
