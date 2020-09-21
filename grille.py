#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from config import * 
import time
from pygame import font
class Grille:
    lvls = ['lvl/lv0','lvl/lv1','lvl/lv2','lvl/lv3']
    i = 0
    lvl = lvls[i]
    def __init__(self, fichier):
        self.ref_img = {
			MENU:pygame.image.load("img/menu.jpg"),
            MUR: pygame.image.load("img/mur.jpg"),
            CAISSE: pygame.image.load("img/caisse.jpg"),
            OBJECTIF: pygame.image.load("img/objectif.png"),
            CAISSE_OK: pygame.image.load("img/caisse_ok.jpg"),
        }
        with open (fichier, 'r') as fich:
            self.lvtest = [[int(l) for l in line.strip().split(" ")] for line in fich]

        self.coord_objec = []
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == OBJECTIF :
                    self.coord_objec.append((x,y))


    def drawMap(self, screen):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                img = self.lvtest[y][x]
                if img in (VIDE, PLAYER) :
                    x += 1

                else:
                    screen.blit(self.ref_img[img], (x*SIZE + 150, y*SIZE + 100))        


    
    def getPlayerPosition(self, grille):
        for y in range(len(self.lvtest)):
            for x in range(len(self.lvtest[y])):
                if self.lvtest[y][x] == PLAYER :
                    return (x*SIZE + 150, y*SIZE+150)


    #---Déplacement des caisses ---#
    def moveCaisse(self, x, y, pos):
        self.is_fini()
        if pos == "gauche":
            if self.lvtest[y][x-2] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y][x-1] == CAISSE_OK:
                    self.lvtest[y][x-1] = OBJECTIF
                else:
                    self.lvtest[y][x-1] = VIDE
                if self.lvtest[y][x-2] == OBJECTIF:
                    self.lvtest[y][x-2] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][x-2] = CAISSE
                    return True

        if pos == "droite":
            if self.lvtest[y][x+2] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y][x+1] == CAISSE_OK:
                    self.lvtest[y][x+1] = OBJECTIF
                else:
                    self.lvtest[y][x+1] = VIDE
                if self.lvtest[y][x+2] == OBJECTIF:
                    self.lvtest[y][x+2] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y][x+2] = CAISSE
                    return True

        if pos == "haut":
            if self.lvtest[y-2][x] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y-1][x] == CAISSE_OK:
                    self.lvtest[y-1][x] = OBJECTIF
                else:
                    self.lvtest[y-1][x] = VIDE
                if self.lvtest[y-2][x] == OBJECTIF:
                    self.lvtest[y-2][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y-2][x] = CAISSE
                    return True

        if pos == "bas":
            if self.lvtest[y+2][x] not in (MUR, CAISSE, CAISSE_OK):
                if self.lvtest[y+1][x] == CAISSE_OK:
                    self.lvtest[y+1][x] = OBJECTIF
                else:
                    self.lvtest[y+1][x] = VIDE
                if self.lvtest[y+2][x] == OBJECTIF:
                    self.lvtest[y+2][x] = CAISSE_OK
                    return True
                else:
                    self.lvtest[y+2][x] = CAISSE
                    return True
        return False
    
    def is_fini(self):
        lis = [self.lvtest[y][x] for (x, y) in self.coord_objec]
        return lis.count(CAISSE_OK) == len(self.coord_objec)
    def genMap(self,level):
		i = 0
		if self.is_fini():
			screen.blit(self.ref_img[MENU], (x*SIZE + 150, y*SIZE + 100))        

		else:
			level = level[i]
		i += 1
		
    

if __name__ == '__main__' :
    
    g = Grille()
    g.genMap(lvl)
   
    
