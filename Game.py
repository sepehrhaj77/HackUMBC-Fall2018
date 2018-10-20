# Zeit wird gezaehlt
import pygame, math, random, time
from pygame.locals import *



def StartGame(fenster):
    printManual(fenster)
  
    return 0


def printManual(fenster):
    bg = (255, 255, 255)
    processed = 0
    while processed == 0:
        #print the menu
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    processed = 1



        fenster.fill((255, 175, 0))
        text_title = pygame.font.SysFont(None, 125)

        title = text_title.render("Manual", True, black)
        fenster.blit(title, (50, 50))

        """
        print the manual here

        """
        pygame.display.update()


pygame.init()

#bg = (255, 255, 255)
bg = (20, 20, 50)
black = (0, 0, 0)



ww = 800
wh = 600

fenster = pygame.display.set_mode((ww, wh), FULLSCREEN)
pygame.mouse.set_visible(0)
fenster.fill(bg)
pygame.display.set_caption("Slay the Python")

pygame.display.update()

#pygame.mixer.music.load("noise.mp3")
########################################################################################################################################################################

game = 1
while game == 1:
    time_count = 0
 
    x2 = 1
   
    # Intro-loop
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0
                    game = 0

                if event.key == K_SPACE:
                    x2 = 2
                  


        fenster.fill((255, 175, 0))
        text_title = pygame.font.SysFont(None, 125)
        text_subt  = pygame.font.SysFont(None, 75)
        text_subt2 = pygame.font.SysFont(None, 25)
     

        title = text_title.render("Python Slayer", True, black)
        fenster.blit(title, (50, 50))

        subt1 = text_subt.render("Press 'Space' to start.", True, black, (255, 250, 0))
        subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
        fenster.blit(subt1, (100, 325))
        fenster.blit(subt2, (100, 400))
     
        pygame.display.update()

    if x2 == 2:
          game = StartGame(fenster)

pygame.quit()



