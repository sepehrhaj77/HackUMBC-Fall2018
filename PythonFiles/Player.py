MAX_PLAYER_HP = 5
class Player:
    #Constructor - sets the hp of the player to the passed parameter
    def __init__(self, health):
        self.hp = health

    #Makes the player lose 1 heart
    def loseHP(self):
        self.hp -= 1
        print("Ouch! You lost a heart")    
            
    #Set the player's hp back to the max
    def refillHearts(self):
        self.hp = MAX_PLAYER_HP

    #Returns the hp of the player
    def getHealth(self):
        return self.hp

    #Replenishes one heart
    def replenishHeart(self):
        if(self.hp >= 5):
            print("Full health!")
        else:
            self.hp += 1
            print("One heart restored")


    #Returns if the player is dead. True->Dead; False->Alive
    def isDead(self):
        if(self.hp == 0):
            return True
        else:
            return False