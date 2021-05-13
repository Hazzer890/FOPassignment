#
# ChosenAnimals.py -  Contains the Classes for the chosen simulated animals
#

from random import randint
from Animal import * 

class wombat(animal):
    def __init__(self, homeX, homeY, xdim, ydim, baseArea):
        super().__init__("wombat", homeX, homeY, xdim, ydim, baseArea)
        self.food = False
        

    def pos(self):
        return(self.posn)

    def move(self):
        if self.food == False:
            #approach food
            if abs((self.foodCood[0]-self.posn[0])) == 0 and abs((self.foodCood[1]-self.posn[1])) == 0:
                self.food = True
            elif abs((self.foodCood[0]-self.posn[0])) == 0:
                self.posn[0] = self.posn[0] + random.randint(-1,1)
            elif abs((self.foodCood[1]-self.posn[1])) == 0:
                self.posn[1] = self.posn[1] + random.randint(-1,1)
            else:
                self.posn[0] = self.posn[0] + ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
                self.posn[1] = self.posn[1] + ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
                if (self.baseArea[int(self.posn[0]), int(self.posn[1])] == 1):
                    self.posn[0] = self.posn[0] - ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
                    self.posn[1] = self.posn[1] - ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
        else:
            #approach home
            if abs((self.homeX-self.posn[0])) == 0 and abs((self.homeY-self.posn[1])) == 0:
                pass
            elif abs((self.homeX-self.posn[0])) == 0 or abs((self.homeY-self.posn[1])) == 0:
                self.posn[0] = self.posn[0] + random.randint(-1,1)
                self.posn[1] = self.posn[1] + random.randint(-1,1)
            else:
                self.posn[0] = self.posn[0] + ((self.homeX-self.posn[0])/abs((self.homeX-self.posn[0])))
                self.posn[1] = self.posn[1] + ((self.homeY-self.posn[1])/abs((self.homeY-self.posn[1])))

        # randomize movement
        self.posn[0] = self.posn[0] + random.randint(-1, 1)
        self.posn[1] = self.posn[1] + random.randint(-1, 1)
        if self.posn[0] > self.xdim:
            self.posn[0] = self.posn[0] - 1
        if self.posn[0] < 0:
            self.posn[0] = self.posn[0] + 1
        if self.posn[1] > self.ydim:
            self.posn[1] = self.posn[1] - 1
        if self.posn[1] < 0:
            self.posn[1] = self.posn[1] + 1
        
        return(self.posn)