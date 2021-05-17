#
# ChosenAnimals.py -  Contains the Classes for the chosen simulated animals
#
import sys
from random import randint
from Animal import * 

numWom = 10
tinder4wombats = []


class wombat(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("wombat", home, xdim, ydim, baseArea)
        self.food = False
        self.laid = False
        self.closestFem = (xdim/2,ydim/2)
        self.mating = True
        self.counter = 0
        self.cantMate = True
        self.fps = fps
        tinder4wombats.append((0,0))

    def periodic(self, form):
        # Pathfinding Code
        if self.food == False:
            #approach food
            if abs((self.foodCood[0]-self.posn[0])) == 0 and abs((self.foodCood[1]-self.posn[1])) == 0:
                self.food = True
                self.mating = True
            elif abs((self.foodCood[0]-self.posn[0])) == 0:
                self.posn[1] = self.posn[1] + ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
            elif abs((self.foodCood[1]-self.posn[1])) == 0:
                self.posn[0] = self.posn[0] + ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
            else:
                self.posn[0] = self.posn[0] + ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
                self.posn[1] = self.posn[1] + ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
                if (self.baseArea[int(self.posn[0]), int(self.posn[1])] == 1):
                    self.posn[0] = self.posn[0] - ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])+1))
                    self.posn[1] = self.posn[1] - ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])+1))
        
        elif self.laid == True and self.gndr == 1:
            #find closest female
            for i in range(len(tinder4wombats)):
                if self.closestFem[0]**2 + self.closestFem[1]**2 < tinder4wombats[i][0]**2 + tinder4wombats[i][1]**2:
                    self.closestFem = tinder4wombats[i]
            #approach closest female
            if self.closestFem != [0,0]:
                if abs((self.closestFem[0]-self.posn[0])) == 0 and abs((self.closestFem[1]-self.posn[1])) == 0:
                    self.food = True
                elif abs((self.closestFem[0]-self.posn[0])) == 0:
                    self.posn[1] = self.posn[1] + ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
                elif abs((self.closestFem[1]-self.posn[1])) == 0:
                    self.posn[0] = self.posn[0] + ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                else:
                    self.posn[0] = self.posn[0] + ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                    self.posn[1] = self.posn[1] + ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
                    if (self.baseArea[int(self.posn[0]), int(self.posn[1])] == 1):
                        self.posn[0] = self.posn[0] - ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                        self.posn[1] = self.posn[1] - ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
        
        else:
            if self.gndr == 0 and self.mating:
                tinder4wombats[form] = (self.posn[0], self.posn[1])
            #approach home
            if abs((self.home[0]-self.posn[0])) == 0 and abs((self.home[1]-self.posn[1])) == 0:
                self.laid = True
            elif abs((self.home[0]-self.posn[0])) == 0:
                self.posn[1] = self.posn[1] + ((self.home[1]-self.posn[1])/abs((self.home[1]-self.posn[1])))
            elif abs((self.home[1]-self.posn[1])) == 0:
                self.posn[0] = self.posn[0] + ((self.home[0]-self.posn[0])/abs((self.home[0]-self.posn[0])))
            else:
                self.posn[0] = self.posn[0] + ((self.home[0]-self.posn[0])/abs((self.home[0]-self.posn[0])))
                self.posn[1] = self.posn[1] + ((self.home[1]-self.posn[1])/abs((self.home[1]-self.posn[1])))

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
        
        # 30 second breeding cooldown
        if self.cantMate:
            self.counter = self.counter + 1
            if self.counter > 10 * self.fps:
                self.cantMate = False

        return(self.posn)

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 120 * self.fps:
            return(True)


    def pos(self):
        return(self.posn)

    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)

    def mate(self):
        hX = True
        hY = True
        self.posn[0] = self.posn[0] + random.randint(-20, 20)
        self.posn[1] = self.posn[1] + random.randint(-20, 20)
        self.home[0] = self.home[0] + random.randint(-50, 50)
        while hX:
            if self.home[0] > self.xdim:
                self.home[0] = self.home[0] + random.randint(-70, 0)
            elif self.home[0] < 0:
                self.home[0] = self.home[0] + random.randint(0, 70)
            else:
                hX = False
        self.home[1] = self.home[1] + random.randint(-50, 50)
        while hY:
            if self.home[1] > self.ydim:
                self.home[1] = self.home[1] + random.randint(-70, 0)
            elif self.home[1] < 0:
                self.home[1] = self.home[1] + random.randint(0, 70)
            else:
                hY = False
        self.laid = False
        self.mating = False
        self.food = False
        self.cantMate = True