# 
# Animal.py - Contains the Animal Class and the involved funtions
#

import random

class animal():
    def __init__(self, name, homeX, homeY, xdim, ydim, baseArea):
        self.name = name
        self.homeX = homeX 
        self.homeY = homeY
        self.gndr = random.randint(0, 1) # 0 is female, 1 is male
        self.xdim = xdim
        self.ydim = ydim
        self.baseArea = baseArea

        self.posn = [homeX, homeY]

        # generate distances to food
        self.listdist = []
        for x in range(self.xdim):
            for y in range(self.ydim):
                if self.baseArea[x,y] == 2:
                    self.listdist.append((x-self.posn[0])**2 + (y-self.posn[1])**2)

         # find smallest distance
        for x in range(self.xdim):
            for y in range(self.ydim):
                if self.baseArea[x,y] == 2:
                    if ((x-self.posn[0])**2 + (y-self.posn[1])**2) == min(self.listdist):
                        self.foodCood = [x,y]
