import pygame, sys
from pygame.locals import *

from button import Button

from menu import MainMenu

from wallet import Wallet 

main = MainMenu("Main Menu", 1280, 720, "assets/images/bgMenu.jpg")
main.gameLoop()
# essayer de trouver comment modifier, dans ce fichier, après main = MainMenu..., un truc 