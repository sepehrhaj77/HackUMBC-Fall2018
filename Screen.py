import pygame, math, random, time
from pygame.locals import *
from printer import Textprint

pygame.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_SKY = pygame.Color('aquamarine1')
FONT = pygame.font.Font(None, 32)

bg = (20, 20, 50)
black = (0, 0, 0)

ww = 800
wh = 600

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

class Screen:

    knight  = pygame.image.load("knight.png")
    First = pygame.image.load("python_blue.png")
    Second = pygame.image.load("python_white.png")
    Final = pygame.image.load("god_emperor_pythonos.png")
    title_screen = pygame.image.load("title_screen.png")
    win_screen = pygame.image.load("win_screen.png")
    game_over = pygame.image.load("game_over.png")
    heart = pygame.image.load("heart.png")
    backGround = pygame.image.load("background.png")
    enemyHeart = pygame.image.load("enemy_heart.png")
    
    QUIT = 0
    START = 1
    
    def __init__(self, window):
        self.window = window

    #returns Screen.QUIT or Screen.START
    def startScreen(self):
        # Intro-loop
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return Screen.QUIT

                    if event.key == K_SPACE:
                        return Screen.START

            self.window.fill((255, 175, 0))
            text_subt  = pygame.font.SysFont(None, 75)
            text_subt2 = pygame.font.SysFont(None, 25)
        
            self.window.blit(Screen.title_screen, (0, 0))
            subt1 = text_subt.render("Press 'Space' to start.", True, black, (255, 250, 0))
            subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
            self.window.blit(subt1, (100, 400))
            self.window.blit(subt2, (100, 500))
     
            pygame.display.update()

    #returns Screen.START or Screen.QUIT
    def victoryScreen(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return QUIT
                    
                    if event.key == K_SPACE:
                        return START


            self.window.fill((255, 175, 0))
            text_subt  = pygame.font.SysFont(None, 75)
        
            self.window.blit(Screen.win_screen, (0, 0))
            subt1 = text_subt.render("Press 'Space' to restart.", True, black, (255, 250, 0))
            subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
            self.window.blit(subt1, (100, 400))
            self.window.blit(subt2, (100, 500))
     
            pygame.display.update()

    #returns Screen.START or Screen.QUIT
    def lossScreen(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return QUIT
                    
                    if event.key == K_SPACE:
                        return START


            self.window.fill((255, 175, 0))
            text_subt  = pygame.font.SysFont(None, 75)
        
            self.window.blit(Screen.game_over, (0, 0))
            subt1 = text_subt.render("Press 'Space' to restart.", True, black, (255, 250, 0))
            subt2 = text_subt.render("Press 'Esc' to exit game.", True, black, (255, 100, 0))
        
            self.window.blit(subt1, (100, 400))
            self.window.blit(subt2, (100, 500))
     
            pygame.display.update()
    
    def battleScreen(self, playerSprite, enemySprite, playerHearts, enemyHearts, text):

        game = 1

        #text message goes here
        textMessage = text

        mybackGround = self.backGround
        input_box = InputBox()
        textBox = Textprint(textMessage)
        window.fill((COLOR_SKY))
        
        while game == 1:
     
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game = 0

                Input = input_box.handle_event(event)
                if(Input):

                    textBox.changeText("You did something")

            #visual effects  
            heartwidth = Screen.heart.get_width() + 5
            for i in range(playerHearts):
                width = 25 + heartwidth * i
                window.blit(Screen.heart, (width, 50))

            heartwidth = Screen.enemyHeart.get_width() + 5
            for i in range(enemyHearts):
                width = 700 - heartwidth * i
                window.blit(Screen.enemyHeart, (width, 50))

            textBox.blit_text(window)     
            input_box.draw(window)
            pygame.display.flip()
            window.blit(mybackGround, (0,50))
            window.blit(playerSprite, (150, 120))
            window.blit(enemySprite, (450, 200))
            



"""

    def animateLeft():

    def animateRight():

    def displayTutorialText(text):

    def displayBattleText(text):
"""
#returns the window
def InitGraphics():
    window = pygame.display.set_mode((ww, wh), FULLSCREEN)
    pygame.mouse.set_visible(0)
    window.fill(bg)
    pygame.display.set_caption("Slay the Python")

    pygame.display.update()

    return window

window = pygame.display.set_mode((ww, wh), FULLSCREEN)

myScreeen = Screen(window)
game = 1
while game:

    game = myScreeen.startScreen()
    stage = 1
    if game:
        myScreeen.battleScreen(myScreeen.knight, myScreeen.First, 5,5,"This is stage one")


pygame.quit()


