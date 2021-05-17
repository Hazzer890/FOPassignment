#
# ChosenAnimals.py -  Contains the Classes for the chosen simulated animals
#

from random import randint
from Animal import * 

numWom = 10
tinder4wombats = []

for i in range(numWom):
    tinder4wombats.append((0,0))

class wombat(animal):
    def __init__(self, homeX, homeY, xdim, ydim, baseArea):
        super().__init__("wombat", homeX, homeY, xdim, ydim, baseArea)
        self.food = False
        self.laid = False
        self.closestFem = (xdim/2,ydim/2)
        

    def pos(self):
        return(self.posn)

    def move(self, form):
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
        elif self.laid == True and self.gndr == 1:
            #find closest female
            for i in range(len(tinder4wombats)):
                if self.closestFem[0]**2 + self.closestFem[1]**2 < tinder4wombats[i][0]**2 + tinder4wombats[i][1]**2:
                    self.closestFem = tinder4wombats[i]
            #approach closest female
            if len(self.closestFem):
                if abs((self.closestFem[0]-self.posn[0])) == 0 and abs((self.closestFem[1]-self.posn[1])) == 0:
                    self.food = True
                elif abs((self.closestFem[0]-self.posn[0])) == 0:
                    self.posn[0] = self.posn[0] + random.randint(-1,1)
                elif abs((self.closestFem[1]-self.posn[1])) == 0:
                    self.posn[1] = self.posn[1] + random.randint(-1,1)
                else:
                    self.posn[0] = self.posn[0] + ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                    self.posn[1] = self.posn[1] + ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
                    if (self.baseArea[int(self.posn[0]), int(self.posn[1])] == 1):
                        self.posn[0] = self.posn[0] - ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                        self.posn[1] = self.posn[1] - ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
        else:
            if self.gndr == 0:
                tinder4wombats[form] = (self.posn[0], self.posn[1])
            #approach home
            if abs((self.homeX-self.posn[0])) == 0 and abs((self.homeY-self.posn[1])) == 0:
                self.laid = True
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