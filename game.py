import pygame, sys
from pygame.locals import *

from math import log, floor

from button import Button
from window import Window
from data import Data
from gameSettings import GameSettings
from shop import Shop


class Game(Window):

    playing = True

    def __init__(self, title, width, height, bg_path):
        Window.__init__(self, title, width, height)
        
        pygame.init()
        clock = pygame.time.Clock()

        self.bg = pygame.image.load(bg_path)
        self.screen.fill((255,255,255))

        dataObj = Data
        data = dataObj.getData()

        def get_font(size): # Returns Press-Start-2P in the desired size
            return pygame.font.Font("assets/font.ttf", size)

        def addMoney(chicken, eggLayingRate, moneyMult):
            return chicken * eggLayingRate * moneyMult
        
        def human_format(number):
            
            units = ["", "K", "M", "B", "t", "q", "Q", "s", "S", "o", "n", "d", "U", "D", "T", "Qt", "Qd", "Sd", "St", "O", "N", "v", "c"]
            k = 1000.0
            if number == 0:
                return '%.2f%s' % (number, units[0])
            magnitude = int(floor(log(number, k)))
            return '%.2f%s' % (number / k**magnitude, units[magnitude])

        timeToAddMoney = USEREVENT + 1
        pygame.time.set_timer(timeToAddMoney, 1000)

        autoSave = USEREVENT
        pygame.time.set_timer(autoSave, 30000)

        addChicken = USEREVENT + 2
        pygame.time.set_timer(addChicken, 350)

        while Game.playing:
            self.screen.blit(self.bg, (0,0))

            #pour avoir la position de la souris
            game_mouse_pos = pygame.mouse.get_pos()

            generateChicken = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,655), text_input="More chicken", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            moneyDisplay = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,50), text_input=f"{human_format(data['money'])} $", font=get_font(57), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            chickensDisplay = Button(image=pygame.image.load("assets/images/invisible rect.png"), pos=(640,90), text_input=f"chickens : {human_format(data['chickens'])}", font=get_font(45), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            settings = Button(image=pygame.image.load("assets/images/settings.png"), pos=(30, 30), text_input=" ", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
            shopButton = Button(image=pygame.image.load("assets/images/shop 128.png"), pos=(892, 651), text_input=" ", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

            for button in [generateChicken, moneyDisplay, chickensDisplay, settings, shopButton]:
                button.changeColor(game_mouse_pos)
                button.update(self.screen)

            #pour les events bouton et quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dataObj.save(data)
                    pygame.quit()
                    sys.exit()

                #pour checker si un bouton est cliqué
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if generateChicken.checkForInput(game_mouse_pos):
                        data["chickens"] += 1
                        data["eggs"] += data["chickens"] * data["eggLayingRate"]
                    
                    if settings.checkForInput(game_mouse_pos):
                        truc = GameSettings(400, 300)
                    
                    if shopButton.checkForInput(game_mouse_pos):
                        dataObj.save(data)
                        shopWindow = Shop(800,600)
                        data = dataObj.getData()

                    
                #pour quitter avec echap
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        dataObj.save(data)
                        pygame.quit()
                        sys.exit()
                    
                    if event.key == K_DOLLAR:
                        data["money"] += 100_000_000

                elif event.type == timeToAddMoney:
                    data["money"] += addMoney(data["chickens"], data["eggLayingRate"], data["moneyMultiplier"])
                
                elif event.type == autoSave:
                    dataObj.save(data)

                #pour actualiser l'affichage
                pygame.display.flip()
                clock.tick(60) #nombre d'image par seconde