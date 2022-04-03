#Importe

import pygame
from pygame.locals import *
pygame.init()

import sys
import random

#Variablen/KONSTANTEN definieren
#Variablen
main = True
menueaktiv = True
levelaktiv = True

#Konstanten
W = 800
H = 600
FPS = 30
SCHWARZ = (0,0,0)
WEISS = (255,255,255)

#Font
font = pygame.font.Font(None, 75)

#Definiern/ öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W,H))
pygame.display.set_caption('...')
clock = pygame.time.Clock()


#Definieren von Funktionen


#buttontexte 1

text_start = font.render('Start', True, WEISS)
text_levelauswahl = font.render('Levelauswahl',True, WEISS)
text_quit = font.render('Quit',True, WEISS)

#butontexte 2
text_start_rect = text_start.get_rect(center=(150, 125))
text_levelauswahl_rect = text_levelauswahl.get_rect(center=(150, 125))
text_quit_rect = text_quit.get_rect(center=(150, 125))

#buttons
button_start = pygame.draw.rect(fenster, WEISS, text_start_rect, 1)
button_levelauswahl = pygame.draw.rect(fenster, WEISS, text_levelauswahl_rect, 1)
button_quit = pygame.draw.rect(fenster, WEISS, text_quit_rect, 1)

#Schleife Hauptprogramm
while main == True:
    if menueaktiv ==True:
        #Spielereingaben
        for event in pygame.event.get():
            if event.type == QUIT:
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_start_clicked = True if text_start_rect.collidepoint(event.pos) else False
                button_levelauswahl_clicked = True if text_levelauswahl_rect.collidepoint(event.pos) else False
                button_quit_clicked = True if text_quit_rect.collidepoint(event.pos) else False

        #Spielfeld aktualisieren
        pygame.display.flip()
        clock.tick(FPS)


pygame.quit()                
sys.exit()

