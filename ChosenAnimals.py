#
# ChosenAnimals.py -  Contains the Classes for the chosen simulated animals
#

from Animal import * 

class bird(animal):
    def __init__(self, homeX, homeY):
        super().__init__("bird", homeX, homeY)
        self.alti = 0

    def pos(self):
        return(self.posn)

    def move(self, xdim, ydim, baseArea):
        # generate distances to food
        listdist = []
        for x in range(xdim):
            for y in range(ydim):
                if baseArea[x,y] == 2:
                    listdist.append((x-self.posn[0])**2 + (y-self.posn[1])**2)
        # find smallest distance
        for x in range(xdim):
            for y in range(ydim):
                if baseArea[x,y] == 2:
                    if ((x-self.posn[0])**2 + (y-self.posn[1])**2) == min(listdist):
                        if abs((x-self.posn[0])) == 0 or abs((y-self.posn[1])) == 0:
                            break
                        else:
                            self.posn[0] = self.posn[0] + ((x-self.posn[0])/abs((x-self.posn[0])))
                            self.posn[1] = self.posn[1] + ((y-self.posn[1])/abs((y-self.posn[1])))


        # randomize movement
        self.posn[0] = self.posn[0] + random.randint(-1, 1)
        self.posn[1] = self.posn[1] + random.randint(-1, 1)
        if self.posn[0] > xdim:
            self.posn[0] = self.posn[0] - 1
        if self.posn[0] < 0:
            self.posn[0] = self.posn[0] + 1
        if self.posn[1] > ydim:
            self.posn[1] = self.posn[1] - 1
        if self.posn[1] < 0:
            self.posn[1] = self.posn[1] + 1
        
        return(self.posn)