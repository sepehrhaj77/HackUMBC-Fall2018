class Enemy:
    #Constructor - sets the hp of the snake to the passed parameter
    def __init__(self, health):
        self.hp = health

    #Returns the hp of the snake
    def getHealth(self):
        return self.hp
    
    #Makes the snake lose 1 heart   
    def loseHP(self):
        self.hp -= 1
        print("A mighty blow! The snake loses a heart.")    
    
    #Returns if the snake is dead. True->Dead; False->Alive
    def isDead(self):
        if(self.hp == 0):
            return True
        else:
            return False