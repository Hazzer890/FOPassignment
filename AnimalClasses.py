#
# AnimalClasses.py -  Contains the Classes for our animals
#

from Animal import * 

numWom = 10
tinder4wombats = []
numkangaroo = 10
tinder4kangaroos = []
numEmu = 10
tinder4emus = []

class wombat(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("wombat", home, xdim, ydim, baseArea, fps)
        tinder4wombats.append((0,0))

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4wombats)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 3000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)
    

    def mate(self):
        super().mate()

class kangaroo(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("wombat", home, xdim, ydim, baseArea, fps)
        tinder4kangaroos.append((0,0))

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4kangaroos)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 3000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)
    

    def mate(self):
        super().mate()

class emu(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("wombat", home, xdim, ydim, baseArea, fps)
        tinder4emus.append((0,0))

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4emus)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 3000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)
    

    def mate(self):
        super().mate()