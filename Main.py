import pygame, sys
from pygame.locals import *

from button import Button

import tkinter as tk
from tkinter import messagebox

import os

import json

import random

#initialisation de pygame et pour l'affichage
pygame.init()
clock = pygame.time.Clock()

#setup de l'affichage
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

def menu():
    pygame.display.set_caption("Menu")