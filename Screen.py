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
    
    def battleScreen(self, playerSprite, enemySprite, playerHeartss, enemyHeartss, text, isFinalBoss):

        game = 1
        userTurn = True
        playerHearts = playerHeartss
        enemyHearts = enemyHeartss
        #text message goes here
        textMessage = text

        mybackGround = self.backGround
        input_box = InputBox()
        textBox = Textprint(textMessage)
        window.fill((COLOR_SKY))
        if isFinalBoss:
            pos = (425, 60)
            stageMessage = [] #here is the input message box
        else:
            pos = (450, 200)
            stageMessage = []

        while game == 1:
            Input = ""
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    #this is for testing
                    if event.key == K_ESCAPE:
                        game = 0
                        return 1
                    #####################

                Input = input_box.handle_event(event)

                ########################################
                #here is the action
            if(Input == "print(\"The knight attacks the python\")"):
                    #matches the requirement
                #textBox.changeText("You did something, Press enter to continue")
                enemyHearts -= 1
                return 1, playerHeartss, enemyHeartss
            elif Input != "":
                #if the player did not enter the right message
                playerHearts -= 1
                return 1, playerHeartss, enemyHeartss
                ##########################################

            #visual effects  
            heartwidth = Screen.heart.get_width() + 5
            for i in range(playerHearts):
                width = 25 + heartwidth * i
                window.blit(Screen.heart, (width, 25))

            heartwidth = Screen.enemyHeart.get_width() + 5
            for i in range(enemyHearts):
                width = 700 - heartwidth * i
                window.blit(Screen.enemyHeart, (width, 25))

            textBox.blit_text(window)     
            input_box.draw(window)
            pygame.display.flip()
            window.blit(mybackGround, (0,50))
            window.blit(playerSprite, (150, 120))
            window.blit(enemySprite, pos)
            



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
Stage1texts = ["Printing is how you display messages on the command line! Do this by typing: print(\"<your message>\") Here is an example: print(\"Hello World!\").Use this to attack the python! Try printing the message \"The knight attacks the python\" (case-sensitive)", "Good job! Now you can set your own battlecry! Try printing any statement you want. Do it correctly and you will slay the python!", "Level 1 complete! The python has been slain."]
Stage2texts = ["Oh no! Your knight's sword has dulled so his attack value is 0! Use variables to set your attack to 1! Variables are how python allows the programmer to save values and reuse them. For example, this is how you set the variable \"x\" to 10: x=10.", "In this case, we have the knight's attack value stored in the variable name \"attack\". Set it to 1:", "Cool! Now lets save your knight's battlecry to the variable \"phrase\". To save text to a variable, simply put your desired text in quotation marks instead of a number like in the previous phrase.", "Awesome! You can also print variables by putting it in the print statement. For example, to print the variable \"x\" you would type: print(x)", "Now, print out your knight's phrase.", "Booleans are variables that can only be either True or False. Note! \"=\" sets a variable to a value. If you want to make a boolean you should use \"==\". For example, myBool = 3+4 = 5 would not do anything. However, myBool = 3+4 == 5 would return a \"False\".", "The color purple is the mark of our enemies. Set the variable \"enemyIsBad\" to be True if \"enemyColor\" is \"purple\"", "If statements are used to block off lines of code unless a certain specification is met. For example: if(bool == True): would run the code in the if statement. "\
                , "We want to attack only IF our enemy is purple. So put our boolean from before (enemyIsBad) into an if statement to see if we will attack Pythonos.", "Level 2 complete! Pythonos has been slain."]
myScreeen = Screen(window)
game = 1
while game:

    game = myScreeen.startScreen()
    stage = 1
    if game:

        heroHeart = 5
        enemyHeart = 5
        while stage == 1:
            status, heroHeart, enemyHeart = myScreeen.battleScreen(myScreeen.knight, myScreeen.First, heroHeart,enemyHeart,Stage1texts[0], 0)
            if status == 1:
                status, heroHeart, enemyHeart = myScreeen.battleScreen(myScreeen.knight, myScreeen.First, heroHeart,enemyHeart,Stage1texts[1], 0)
            elif status == 2:
                status, heroHeart, enemyHeart = myScreeen.battleScreen(myScreeen.knight, myScreeen.First, heroHeart,enemyHeart,"Sorry, try again", 0)
            elif status == 3:
                status, heroHeart, enemyHeart = myScreeen.battleScreen(myScreeen.knight, myScreeen.First, heroHeart,enemyHeart,Stage1texts[2], 0)
            elif status == 4:
                status, heroHeart, enemyHeart = myScreeen.battleScreen(myScreeen.knight, myScreeen.First, heroHeart,enemyHeart,"Sorry you lost", 0)      
        status = myScreeen.battleScreen(myScreeen.knight, myScreeen.Final, heroHeart,enemyHeart, "This is the final Boss", 1)
    
        game = myScreeen.lossScreen()

pygame.quit()


