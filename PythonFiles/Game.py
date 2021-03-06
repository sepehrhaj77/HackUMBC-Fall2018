
import pygame, math, random, time
from pygame.locals import *
from printer import Textprint

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_SKY = pygame.Color('aquamarine1')
COLOR_WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 32)

class InputBox:
    
    def __init__(self,FONT= pygame.font.Font(None, 32),  text='',x=100, y=550, w=600, h=34):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0,0,0)
        self.text = text
        self.txt_surface = FONT.render(text, True, (0,0,0))



    def handle_event(self, event):
        temp = ''
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                print(self.text)
                temp = self.text
                self.text = ''

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
       
            elif self.txt_surface.get_width() < 580:
                self.text += event.unicode
                # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)
            #pygame.display.update()
        if temp != '':
            return temp

    def update(self):
        # Resize the box if the text is too long.
        self.rect.w = 600

    def draw(self, screen):
        # Blit the text.

        
        # Blit the rect.
        pygame.draw.rect(screen, (255,255,255), self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5)) 


bg = (20, 20, 50)
black = (0, 0, 0)



ww = 800
wh = 600



def StartGame(window):

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
    

    #text message goes here
    textMessage = "Stage 1"


    backGround = pygame.image.load("background.png")
    input_box = InputBox()
    textBox = Textprint(textMessage)
    window.fill((COLOR_SKY))
    
    while x2 == 1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    x2 = 0

            Input = input_box.handle_event(event)
            if(Input):
                textBox.changeText("You did something")


        #visual effects  
        textBox.blit_text(window)     
        input_box.draw(window)
        pygame.display.flip()
        window.blit(backGround, (0,50))
        window.blit(knight, (150, 120))
        window.blit(First, (450, 200))
 



def level2(window):
    x2 = 1
    FONT = pygame.font.Font(None, 32)

    backGround = pygame.image.load("background.png")
    input_box = InputBox()
    window.fill(COLOR_SKY)
    
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

        window.blit(backGround, (0,50))

        window.blit(knight, (150, 120))
        window.blit(Second, (450, 200))
 
  

def final(window):
    x2 = 1
    FONT = pygame.font.Font(None, 32)

    backGround = pygame.image.load("background.png")
    input_box = InputBox()
    window.fill(COLOR_SKY)
    
    while x2 == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                input_box.update()
                #window.fill((30, 30, 30))
                input_box.draw(window)

                pygame.display.flip()

                window.blit(backGround, (0,50))

                window.blit(knight, (150, 120))
                window.blit(Final, (450, 50))
         
                
                if event.key == K_ESCAPE:
                    x2 = 0

                input_box.handle_event(event)

     
       



clock = pygame.time.Clock()


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
    Playagain = startPage(window)
    
pygame.quit()



