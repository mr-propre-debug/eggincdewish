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

#initialisation de pygame et pour l'affichage
pygame.init()
clock = pygame.time.Clock()

#setup de l'affichage
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

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
    screen.fill((0,0,0))

    with open("data/data.json", 'r') as f:
        data = json.load(f)
    f.close()

    money = data["money"]
    chickens = data["chickens"]
    eggs = data["eggs"]
    moneyMultiplier = data["moneyMultiplier"]
    
    def addMoney(numChick, moneyMul):
        Money = numChick * 2 * moneyMul
        return Money
    
    timeToAddMoney = USEREVENT
    pygame.time.set_timer(timeToAddMoney, 1000)

    while True:
        # screen.blit(bgGame, (0,0))

        #pour avoir la position de la souris
        game_mouse_pos = pygame.mouse.get_pos()

        generateChicken = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,670), text_input="More chicken", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        moneyDisplay = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,50), text_input= f"{money} $", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        chickensDisplay = Button(image=pygame.image.load("assets/images/Play Rect.png"), pos=(640,159), text_input=f"chickens {chickens}", font=get_font(65), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        for button in [generateChicken, moneyDisplay, chickensDisplay]:
            button.changeColor(game_mouse_pos)
            button.update(screen)

        #pour les events bouton et quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #pour checker si un bouton est cliqué
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pour quitter
                if generateChicken.checkForInput(game_mouse_pos):
                    chickens += 1
                
            #pour quitter avec echap
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == timeToAddMoney:
                money += addMoney(chickens, moneyMultiplier)

            #pour actualiser l'affichage
            pygame.display.flip()
            clock.tick(60) #nombre d'image par seconde

def main_menu():
    pygame.display.set_caption("Menu")
    screen.fill((0,0,0))

    while True:
        # screen.blit(bgMenu, (0,0))

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