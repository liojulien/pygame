#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
import os
import time
from pygame.locals import *
from pygame import font
from grille import Grille
from player import Player
from config import *
from Colors import *
from splashScreen import a

pygame.init()
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

lvl = ['lvl/lv0','lvl/lv1','lvl/lv2','lvl/lv3']
i = 0

	
def main_loop(level):
	
	_grille = Grille(level)
	_grille.drawMap(screen)
	_player = Player(_grille)
	_player.drawPlayer(screen)
	pygame.display.update()
	background = pygame.image.load("img/back.png")
	
	while not _grille.is_fini():
		
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == KEYDOWN:
				_player.move(event.key)
				
				if event.key == K_r:
					_grille.genMap(level)
					_grille.drawMap(screen)
					_player = Player(_grille)
					_player.drawPlayer(screen)
				if event.key == K_q:
					sys.exit()
				l = 0
				if event.key == K_p:
					for level in lvl:
						main_loop(lvl[l])
					l += 1
			
		
		screen.blit(background, (150,100))
		_grille.drawMap(screen)
		_player.drawPlayer(screen)
		pygame.display.update()



		
