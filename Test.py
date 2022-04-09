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
level_1_aktiv = True
level_2_aktiv = False
levauswahlaktiv = False
levelmenue = False
settings = False

#Konstanten
W = 800
H = 600
FPS = 30
SCHWARZ = (0,0,0)
WEISS = (255,255,255)

#Fonts
font = pygame.font.Font(None, 75)
font2 =pygame.font.Font(None,35)
lautstaerke_musik = 100

#Definiern/ öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W,H))
pygame.display.set_caption('...')
clock = pygame.time.Clock()


#Definieren von Funktionen




#Schleife Hauptprogramm
while main == True:
    if menueaktiv ==True:
        #buttontexte 1

        text_start = font.render('Start', True, WEISS)
        text_levelauswahl = font.render('Levels',True, WEISS)
        text_quit = font.render('Quit',True, WEISS)
        text_settings = font.render('Settings',True,WEISS)
    

        #butontexte 2
        text_start_rect = text_start.get_rect(center=(400, 150))
        text_levelauswahl_rect = text_levelauswahl.get_rect(center=(400, 250))
        text_quit_rect = text_quit.get_rect(center=(400, 450))
        text_settings_rect = text_settings.get_rect(center=(400,350))


        #buttons
        button_start = pygame.draw.rect(fenster, WEISS, text_start_rect, 1)
        button_levelauswahl = pygame.draw.rect(fenster, WEISS, text_levelauswahl_rect, 1)
        button_quit = pygame.draw.rect(fenster, WEISS, text_quit_rect, 1)
        button_settings=pygame.draw.rect(fenster,WEISS,text_settings_rect,1)


        #Texte für die Buttons
        starttext = font.render('Start',True, WEISS)
        fenster.blit(starttext, [340,130])

        levelauswahltext = font.render('Levels',True, WEISS)
        fenster.blit(levelauswahltext, [317,230])

        quittext = font.render('Quit',True, WEISS)
        fenster.blit(quittext, [345,430])

        herstellertext = font2.render('produced by LylianProgrammer and Indoorgamer123',True,WEISS)
        fenster.blit(herstellertext, [100,530])        
        
        fenster.blit(text_settings, [295,323])
        
        #Spielereingaben
        for event in pygame.event.get():
            if event.type == QUIT:
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_start_clicked = True if text_start_rect.collidepoint(event.pos) else False
                button_levelauswahl_clicked = True if text_levelauswahl_rect.collidepoint(event.pos) else False
                button_quit_clicked = True if text_quit_rect.collidepoint(event.pos) else False
                button_settings_clicked = True if text_settings_rect.collidepoint(event.pos) else False

                if button_start_clicked == True:
                    levelaktiv = True

                if button_levelauswahl_clicked == True:
                    levelmenue = True
                    menueaktiv = False
                    fenster.fill(SCHWARZ)
                    

                if button_quit_clicked == True:
                    main = False

                if button_settings_clicked == True:
                    menueaktiv = False
                    settings = True 
                    fenster.fill(SCHWARZ)
                    
        #Spielfeld aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

        
    if levelmenue == True:
        #Elemente zeichnen        
        text_level1 = font.render('Level 1', True, WEISS)
        text_level2 = font.render('Level 2', True, WEISS)
        text_back = font.render('Back to Menu', True, WEISS)
        
        text_level1_rect= text_level1.get_rect(center=(400, 150))
        text_level2_rect= text_level2.get_rect(center=(400, 250))
        text_back_rect= text_back.get_rect(center=(400, 350))
        
        button_level1 = pygame.draw.rect(fenster,WEISS, text_level1_rect,1)
        button_level2= pygame.draw.rect(fenster,WEISS, text_level2_rect,1)
        button_back=  pygame.draw.rect(fenster,WEISS, text_back_rect,1)
        
        fenster.blit(text_level1, [315,130])
        
        fenster.blit(text_level2, [313,230])

        fenster.blit(text_back, [230,330])        
        
        #Spielereingaben
        for event in pygame.event.get():
            if event.type == QUIT:
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_level1_clicked = True if text_level1_rect.collidepoint(event.pos) else False
                button_level2_clicked = True if text_level2_rect.collidepoint(event.pos) else False                
                button_back_clicked = True if text_back_rect.collidepoint(event.pos) else False
                
                if button_level1_clicked == True:
                    level_1_aktiv = True
                    
                if button_level2_clicked == True:
                    level_2_aktiv = True
                    
                if button_back_clicked == True:
                    menueaktiv = True
                    fenster.fill(SCHWARZ)
                    levelmenue = False
                     
        
        #aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

    if settings == True:
        text_musiklauter = font.render('louder',True,WEISS)
        text_musikleiser = font.render('quiter',True,WEISS)
        text_musik = font.render('Music',True,WEISS)
        text_exit_musik=font.render('Back to Menu',True,WEISS)
        
        text_musiklauter_rect = text_musiklauter.get_rect(center=(500,330))
        text_musikleiser_rect = text_musiklauter.get_rect(center=(300,330))
        text_exit_musik_rect = text_exit_musik.get_rect(center=(400,430))
        
        button_musiklauter=pygame.draw.rect(fenster,WEISS,text_musiklauter_rect,1)
        button_musikleiser=pygame.draw.rect(fenster,WEISS,text_musikleiser_rect,1)
        button_exit_musik=pygame.draw.rect(fenster,WEISS,text_exit_musik_rect,1)
        
        fenster.blit(text_musiklauter,[417,305])
        fenster.blit(text_musikleiser,[225,303])
        fenster.blit(text_musik,[325,205])
        fenster.blit(text_exit_musik,[230,405])

        for event in pygame.event.get():
            if event.type == QUIT:
                settings = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_musiklauter_clicked = True if text_musiklauter_rect.collidepoint(event.pos) else False
                button_musikleiser_clicked = True if text_musikleiser_rect.collidepoint(event.pos) else False                
                button_exit_musik_clicked = True if text_exit_musik_rect.collidepoint(event.pos) else False

                if button_musiklauter_clicked == True:
                    lautstaerke_musik += 50 #Muss noch angepasst werden

                if button_musikleiser_clicked == True:
                     lautstaerke_musik -= 50 #Muss noch angepasst werden

                if button_exit_musik_clicked == True:
                    settings = False
                    menueaktiv = True
                    fenster.fill(SCHWARZ)

               
        pygame.display.flip()
        clock.tick(FPS)
        
pygame.quit()                
sys.exit()

