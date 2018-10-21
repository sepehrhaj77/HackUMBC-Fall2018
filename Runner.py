from Enemy import Enemy
from Player import Player


#This function will handle the running of the first level
def level1(player):
    success1 = False
    #Instantiate the snake and answer, and set success to false. Success determines if the player has beaten the level
    snake1 = Enemy(2)
    answerToken = "print(\"The knight attacks the python\")"

    #while loop to continually play the level until the player dies or the enemy snake dies
    while (not(player.isDead()) and not(success1)):

        #Give player quick tutorial on how the print statement works. Then, get their input
        gameMessage = "Printing is how you display messages on the command line! Do this by typing: print(\"<your message>\") \nHere is an example: print(\"Hello World!\")\nUse this to attack the python! Try printing the message \"The knight attacks the python\" (case-sensitive)\n"
        usrInput = input(gameMessage)

        #Compare the player's answer to the correct answer:

        #Player is correct
        if(usrInput == answerToken):
            snake1.loseHP()
            success1 = True
        
        #Player is wrong
        else:
            print("Try again!")
            player.loseHP()
        
    #The loop will only exit if the player has died or beaten the level. Check which one here
    if(success1):
        success2 = False
        while (not(player.isDead()) and not(success2)):
            #Give player quick tutorial on how the print statement works. Then, get their input
            gameMessage = "Have fun! Try printing anything you want. Do it correctly and you will slay the python!\n"
            usrInput = input(gameMessage)

            #Compare the player's answer to the correct answer:

            #Player is correct
            if(usrInput.find("print(\"") == 0 and usrInput[len(usrInput)-2:len(usrInput)] == "\")" ):
                snake1.loseHP()
                userPhrase = usrInput[7:len(usrInput)-2]
                print(userPhrase)
                success2 = True
            
            #Player is wrong
            else:
                print("Try again!")
                player.loseHP()
        #if the player succeeded with the second part of the level
        if(success2):
            print("Level 1 complete! The python has been slain.")            
        #they failed
        else:
            print("Game Over!")

        return success2    
    
        
    else:
        print("Game Over!")
        return success1

#This function will handle the running of the first level
def level2(player):
    success1 = False
    #Instantiate the snake and answer, and set success to false. Success determines if the player has beaten the level
    snake1 = Enemy(5)

    #while loop to continually play the level until the player dies or the enemy snake dies
    while (not(player.isDead()) and not(success1)):

        #Give player quick tutorial on how the print statement works. Then, get their input
        gameMessage = ("Oh no! Your knight lost his sword so his attack value is 0! Use variables to set your attack to 1!\nVariables are how python allows the programmer to save values and reuse them. For example, this is how you set the variable \"x\" to 10: x=10\nIn this case, we have the knight's attack value stored in the variable name \"attack\". Set it to 1:\n")
        usrInput = input(gameMessage)

        #Compare the player's answer to the correct answer:
        usrInput = usrInput.replace(" ", "")
        answerToken = ("attack=1")
        #Player is correct
        if(usrInput == answerToken):
            snake1.loseHP()
            success1 = True
        
        #Player is wrong
        else:
            print("Try again!")
            player.loseHP()    
        
    #The loop will only exit if the player has died or beaten the level. Check which one here
    if(success1):
        success2 = False
        while (not(player.isDead()) and not(success2)):
            #Game message for second part of level 2
            gameMessage = "Cool! Now lets save your knight's battlecry to the variable \"phrase\"\n"
            usrInput = input(gameMessage)
            usrInput = usrInput.strip()
            #Compare the player's answer to the correct answer:
            
            #Player is correct
            if(usrInput[0:usrInput.find("=")+1].replace(" ","") == "phrase="):
                usrInput = usrInput[usrInput.find("\""):len(usrInput)]
                if(usrInput[0] == "\"" and usrInput[len(usrInput)-1] == "\""):
                    userPhrase = usrInput[1:len(usrInput)-1]
                    snake1.loseHP()
                    success2 = True

                #Player is wrong
                else:
                    print("Try again!")
                    player.loseHP()

            #Player is wrong
            else:
                print("Try again!")
                player.loseHP()
    else:
        print("Game Over!")
        return success1        
                
    #if the player succeeded with the second part of the level
    if(success2):
        success3 = False
        while(not(player.isDead()) and not(success3)):
            #Game message for second part of level 2
            gameMessage = "Awesome! You can also print variables by putting it in the print statement. For example, to print the variable \"x\" you would type: print(x)\nNow, print out your knight's phrase.\n"
            usrInput = input(gameMessage)
            usrInput = usrInput.strip()
            #Compare the player's answer to the correct answer:
            answerToken = ("print(phrase)")
            #Player is correct
            if(usrInput == answerToken):
                print(userPhrase)
                snake1.loseHP()
                success3 = True
            
            #Player is wrong
            else:
                print("Try again!")
                player.loseHP()

    #they failed
    else:
        print("Game Over!")
        return success2  

    #if the player succeeded with the third part of the level
    if(success3):
        success4 = False
        while(not(player.isDead()) and not(success4)):
            #Game message for second part of level 2
            gameMessage = "Booleans are variables that can only be either True or False. Note! \"=\" sets a variable to a value. If you want to make a boolean you should use \"==\".\nFor example, myBool = 3+4 = 5 would not do anything. However, myBool = 3+4 == 5 would return a \"False\".\n"
            gameMessage2 = "The color purple is the mark of our enemies. Set the variable \"enemyIsBad\" to be True if \"enemyColor\" is \"purple\"\n"
            print(gameMessage)
            usrInput = input(gameMessage2)
            usrInput = usrInput.strip()
            usrInput = usrInput.replace(" ", "")

            #Compare the player's answer to the correct answer:
            answerToken = ("enemyIsBad=enemyColor==purple")
            #Player is correct
            if(usrInput == answerToken):
                snake1.loseHP()
                success4 = True
            
            #Player is wrong
            else:
                print("Try again!")
                player.loseHP()   
    
    else:
        print("Game Over!")
        return success3
            
    if(success4):
        success5 = False
        while(not(player.isDead()) and not(success5)):
            #Game message for second part of level 2
            gameMessage = "If statements are used to block off lines of code unless a certain specification is met.\nFor example: if(bool == True): would run the code in the if statement. We want to attack only IF our enemy is purple. So put our boolean from before (enemyIsBad) into an if statement to see if we will attack pythonos."
            usrInput = input(gameMessage)
            usrInput = usrInput.strip()
            usrInput = usrInput.replace(" ", "")

            #Compare the player's answer to the correct answer:
            answerToken = ("if(enemyIsBad==True):")
            #Player is correct
            if(usrInput == answerToken):
                snake1.loseHP()
                success5 = True
            
            #Player is wrong
            else:
                print("Try again!")
                player.loseHP()

        #if the player succeeded with the second part of the level
        if(success5):
            print("Level 2 complete! Pythonos has been slain.")            
        #they failed
        else:
            print("Game Over!")

        return success5

    else:
        print("Game Over!")
        return success4

#Function to see if the player wants to restart their game after dying
def keepPlaying():
    answer = input("Do you wish to restart? [y/n]")
    return answer == "y"

#The main runner function
def main():
    #Instantiate a player with 5 hearts. 
    p1 = Player(5)
    print("Welcome to Slay the Python!")
    play = True

    while(play):
        #Begin the first level. Set success for the level to false. Afterwards, check if the game is over and if they want to restart with keepPlaying
        success = level1(p1)
        #If the player died
        if(not success):
            #If they wish to restart
            if(keepPlaying()):
                p1.refillHearts()
                continue
            else:
                play = False
                print("Game over! Goodbye.")

        success = level2(p1)
        #If the player died
        if(not success):
            #If they wish to restart
            if(keepPlaying()):
                p1.refillHearts()
                continue
            else:
                play = False
                print("Game over! Goodbye.")
        play = False
        print("You won!")

main()
