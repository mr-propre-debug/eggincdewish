import pygame, sys
from pygame.locals import *

from button import Button

from game import Game
from window import Window

class MainMenu(Window):

    def __init__(self, title, width, height, bg_path):
        # background
        self.bg = pygame.image.load(bg_path)

        Window.__init__(self, title, width, height)

        #initialisation de pygame et pour l'affichage
        pygame.init()
        clock = pygame.time.Clock()

        #volume du jeu
        volume = 1.0

        #pour la police d'écriture
        def get_font(size): # Returns Press-Start-2P in the desired size
            return pygame.font.Font("assets/font.ttf", size)

        self.screen.fill((0,0,0))

        while True:
            self.screen.blit(self.bg, (0,0))

            #pour avoir la position de la souris
            menu_mouse_pos = pygame.mouse.get_pos()

            playButton = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,250), text_input="JOUER", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            optButton = Button(image=pygame.image.load("assets/images/Option Rect.png"), pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            quitButton = Button(image=pygame.image.load("assets/images/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            #pour changer la couleur du bouton quand on passe dessus
            for button in [playButton, quitButton, optButton]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)

            #pour les events bouton et quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #pour checker si un bouton est cliqué
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #pour quitter
                    if quitButton.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

                    if playButton.checkForInput(menu_mouse_pos):
                        gameMenu = Game("Generating chickens", 1280, 720, "assets/images/bgGame.jpg")
                        
                #pour quitter avec echap
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                #pour actualiser l'affichage
                pygame.display.flip()
                clock.tick(60) #nombre d'image par seconde

main = MainMenu("Main Menu", 1280, 720, "assets/images/bgMenu.jpg")