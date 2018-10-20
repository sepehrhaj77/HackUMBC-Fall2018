from Enemy import Enemy
from Player import Player


#This function will handle the running of the first level
def level1(player):
    success = False
    #Instantiate the snake and answer, and set success to false. Success determines if the player has beaten the level
    snake1 = Enemy(1)
    answerToken = "print(\"The knight attacks the python\")"

    #while loop to continually play the level until the player dies or the enemy snake dies
    while (not(player.isDead()) and not(success)):

        #Give player quick tutorial on how the print statement works. Then, get their input
        introMessage = "Printing is how you display messages on the command line! Do this by typing: print(\"<your message>\") \nHere is an example: print(\"Hello World!\")\nUse this to attack the python! Try printing the message \"The knight attacks the python\" (case-sensitive)\n"
        usrInput = input(introMessage)

        #Compare the player's answer to the correct answer:

        #Player is correct
        if(usrInput == answerToken):
            snake1.loseHP()
            #Check if the attack killed the snake
            if(snake1.isDead()):
                success = True
                print("Snake has died.")
        
        #Player is wrong
        else:
            player.loseHP()
        
    #The loop will only exit if the player has died or beaten the level. Check which one here
    if(success):
        print("Level 1 complete! The python has been slain.")
        
    else:
        print("Game Over!")

    return success  
    
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
