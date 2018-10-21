
import pygame, math, random, time
from pygame.locals import *
#from inputBox import InputBox

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_SKY = pygame.Color('aquamarine1')
FONT = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, FONT,  text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)


    def handle_event(self, event):
        temp = ''
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                print(self.text)
                temp = self.text
                self.text = ''
                window.fill(COLOR_SKY)


            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                window.fill(COLOR_SKY)

            elif self.txt_surface.get_width() < 590:
                self.text += event.unicode
                # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)
        if temp != '':
            return temp

    def update(self):
        # Resize the box if the text is too long.
        
        self.rect.w = 600

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
class textBox:
    def __init__(self, x, y, w, h, FONT,  text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



bg = (20, 20, 50)
black = (0, 0, 0)



ww = 800
wh = 600



def StartGame(window):

    printManual(window)
    level1(window)
    level2(window)
    final(window)

    return victory(window)

def restart(window):

    level1(window)
    level2(window)
    final(window)

    return victory(window)


def startPage(window):
    # Intro-loop
    x2 = 1
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0
                    return 0

                if event.key == K_SPACE:
                    x2 = 2
                    return StartGame(window)

 

        window.fill((255, 175, 0))
        text_subt  = pygame.font.SysFont(None, 75)
        text_subt2 = pygame.font.SysFont(None, 25)
     

        
        window.blit(title_screen, (0, 0))
        window.blit(knight, (100, 200))
        subt1 = text_subt.render("Press 'Space' to start.", True, black, (255, 250, 0))
        subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
        window.blit(subt1, (100, 400))
        window.blit(subt2, (100, 500))
     
        pygame.display.update()

def victory(window):
    again = 1
    while again == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    again = 0
                    

                if event.key == K_SPACE:
                    again = 2


        window.fill((255, 175, 0))
        text_subt  = pygame.font.SysFont(None, 75)
     

        
        window.blit(win_screen, (0, 0))
        window.blit(knight, (100, 200))
        subt1 = text_subt.render("Press 'Space' to restart.", True, black, (255, 250, 0))
        subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
        window.blit(subt1, (100, 400))
        window.blit(subt2, (100, 500))
     
        pygame.display.update()

    return again


def level1(window):
    x2 = 1
    FONT = pygame.font.Font(None, 32)

    #text message goes here
    textMessage = ""


    backGround = pygame.image.load("background.png")
    input_box = InputBox(100, 500, 600, 34 , FONT)
    #text_box = text_box(100, 400, 600, 100, FONT, textMessage)
    window.fill((COLOR_SKY))
    
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0

            input_box.handle_event(event)

     
        input_box.update()
        #window.fill((30, 30, 30))
        input_box.draw(window)

        pygame.display.flip()

        window.blit(backGround, (50,50))

        window.blit(knight, (150, 120))
        window.blit(First, (450, 200))
 
        pygame.display.update()


def level2(window):
    x2 = 1
    FONT = pygame.font.Font(None, 32)

    backGround = pygame.image.load("background.png")
    input_box = InputBox(100, 500, 600, 34 , FONT)
    window.fill((30, 30, 30))
    
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0

            input_box.handle_event(event)

     
        input_box.update()
        #window.fill((30, 30, 30))
        input_box.draw(window)

        pygame.display.flip()

        window.blit(backGround, (50,50))

        window.blit(knight, (150, 120))
        window.blit(Second, (450, 200))
 
        pygame.display.update()

def final(window):
    x2 = 1
    FONT = pygame.font.Font(None, 32)

    backGround = pygame.image.load("background.png")
    input_box = InputBox(100, 500, 600, 34 , FONT)
    window.fill((30, 30, 30))
    
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0

            input_box.handle_event(event)

     
        input_box.update()
        #window.fill((30, 30, 30))
        input_box.draw(window)

        pygame.display.flip()

        window.blit(backGround, (50,50))

        window.blit(knight, (150, 120))
        window.blit(Final, (450, 50))
 
        pygame.display.update()

def printManual(window):
    bg = (255, 255, 255)
    processed = 0
    while processed == 0:
        #print the menu
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    processed = 1



        window.fill((255, 175, 0))
        text_title = pygame.font.SysFont(None, 125)

        title = text_title.render("Manual", True, black)
        window.blit(title, (50, 50))

        """
        print the manual here

        """
        pygame.display.update()




window = pygame.display.set_mode((ww, wh), FULLSCREEN)
pygame.mouse.set_visible(0)
window.fill(bg)
pygame.display.set_caption("Slay the Python")

pygame.display.update()

knight  = pygame.image.load("knight.png")
First = pygame.image.load("python_blue.png")
Second = pygame.image.load("python_white.png")
Final = pygame.image.load("god_emperor_pythonos.png")
title_screen = pygame.image.load("title_screen.png")
win_screen = pygame.image.load("win_screen.png")
game_over = pygame.image.load("game_over.png")
heart = pygame.image.load("heart.png")
#pygame.mixer.music.load("noise.mp3")
########################################################################################################################################################################
#main loop
game = 1

Playagain = startPage(window)

while Playagain != 0:
    Playagain = restart(window)
    
pygame.quit()



