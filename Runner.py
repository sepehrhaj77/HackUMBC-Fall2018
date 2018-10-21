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

        if(success2):
            print("Level 1 complete! The python has been slain.")            

        else:
            print("Game Over!")

        return success2    
    
        
    else:
        print("Game Over!")
        return success1

      
    
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
        play = False
        print("You won! u have big ghey")

            
    
    
    


main()
