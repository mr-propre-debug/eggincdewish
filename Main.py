import pygame, sys
from pygame.locals import *

from button import Button

import tkinter as tk
from tkinter import messagebox

import os

import json

import random

import threading
from threading import Timer

from math import log, floor

#initialisation de pygame et pour l'affichage
pygame.init()
clock = pygame.time.Clock()

#setup de l'affichage
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

# backgrounds
bgMenu = pygame.image.load("assets/images/bgMenu.jpg")
bgGame = pygame.image.load("assets/images/bgGame.jpg")

#volume du jeu
volume = 1.0

#pour la police d'écriture
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


with open("data/data.json", "ab+") as ab:
    ab.close()
    f = open('data/data.json','r+')
    f.readline()
    if os.stat("data/data.json").st_size == 0:
        f.write('{"money" : 0, "chickens" : 0, "eggs" : 0, "moneyMultiplier": 1}')
        f.close()
    else:
        pass

def game_menu():
    pygame.display.set_caption("Generating chickens")
    screen.fill((255,255,255))

    with open("data/data.json", 'r') as f:
        data = json.load(f)
    f.close()

    money = data["money"]
    chickens = data["chickens"]
    eggs = data["eggs"]
    moneyMultiplier = data["moneyMultiplier"]
    
    def addMoney(numChick, moneyMul):
        data["money"] = money
        data["chickens"] = chickens
        data["eggs"] = eggs
        data["moneyMultiplier"] = moneyMultiplier
        Money = numChick * 2 * moneyMul
        return Money
    
    def human_format(number):
        
        units = ["", "K", "M", "B", "t", "q", "Q", "s", "S", "o", "n", "d", "U", "D", "T", "Qt", "Qd", "Sd", "St", "O", "N", "v", "c"]
        k = 1000.0
        if number == 0:
            return '%.2f%s' % (number, units[0])
        magnitude = int(floor(log(number, k)))
        return '%.2f%s' % (number / k**magnitude, units[magnitude])

    def save():
        with open('data/data.json', 'w') as f:
            json.dump(data, f)
        f.close()

    def manualSave():
        with open('data/data.json', 'w') as f:
            json.dump(data, f)
        f.close()
        root.destroy()

    timeToAddMoney = USEREVENT + 1
    pygame.time.set_timer(timeToAddMoney, 1000)

    autoSave = USEREVENT
    pygame.time.set_timer(autoSave, 30000)

    while True:
        screen.blit(bgGame, (0,0))

        #pour avoir la position de la souris
        game_mouse_pos = pygame.mouse.get_pos()

        generateChicken = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,655), text_input="More chicken", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        moneyDisplay = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,50), text_input=f"{human_format(money)} $", font=get_font(57), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        chickensDisplay = Button(image=pygame.image.load("assets/images/invisible rect.png"), pos=(640,90), text_input=f"chickens : {human_format(chickens)}", font=get_font(45), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        settings = Button(image=pygame.image.load("assets/images/settings.png"), pos=(30, 30), text_input=" ", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        shopButton = Button(image=pygame.image.load("assets/images/shop 128.png"), pos=(892, 651), text_input=" ", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        for button in [generateChicken, moneyDisplay, chickensDisplay, settings, shopButton]:
            button.changeColor(game_mouse_pos)
            button.update(screen)

        #pour les events bouton et quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #pour checker si un bouton est cliqué
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if generateChicken.checkForInput(game_mouse_pos):
                    chickens += 1
                    eggs += chickens * 2
                
                if settings.checkForInput(game_mouse_pos):
                    root= tk.Tk()

                    canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
                    canvas1.pack()

                    label1 = tk.Label(root, text='Save')
                    label1.config(font=('assets/font.ttf', 14))
                    canvas1.create_window(200, 25, window=label1)

                    button1 = tk.Button(text='save', command=manualSave, bg='brown', fg='white', font=('assets/font.ttf', 9, 'bold'))
                    canvas1.create_window(200, 50, window=button1)

                    root.mainloop()
                
            #pour quitter avec echap
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    save()
                    pygame.quit()
                    sys.exit()
                
                if event.key == K_DOLLAR:
                    money += 100_000_000
                
                if event.key == K_a:
                    money -= 10**9
                    if money < 0:
                        money = 0
                    save()

                if event.key == K_z:
                    moneyMultiplier *= 1.5
                    save()

            elif event.type == timeToAddMoney:
                money += addMoney(chickens, moneyMultiplier)
            
            elif event.type == autoSave:
                save()

            #pour actualiser l'affichage
            pygame.display.flip()
            clock.tick(60) #nombre d'image par seconde

def main_menu():
    
    pygame.display.set_caption("Menu")
    screen.fill((0,0,0))

    while True:
        screen.blit(bgMenu, (0,0))

        #pour avoir la position de la souris
        menu_mouse_pos = pygame.mouse.get_pos()

        playButton = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,250), text_input="JOUER", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        optButton = Button(image=pygame.image.load("assets/images/Option Rect.png"), pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        quitButton = Button(image=pygame.image.load("assets/images/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        #pour changer la couleur du bouton quand on passe dessus
        for button in [playButton, quitButton, optButton]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

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
                    game_menu()
                
            #pour quitter avec echap
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            #pour actualiser l'affichage
            pygame.display.flip()
            clock.tick(60) #nombre d'image par seconde

main_menu()