#
# AnimalClasses.py -  Contains the Classes for our animals
#
from Animal import * 

tinder4wombats = []
tinder4emus = []
tinder4possums = []
tinder4kangaroos = []
tinder4foxes = []


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
        if self.isDead > 1000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)


class emu(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("emu", home, xdim, ydim, baseArea, fps)
        tinder4emus.append((0,0))

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4emus)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 1000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)

class possum(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("possum", home, xdim, ydim, baseArea, fps)
        tinder4possums.append((0,0))

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4possums)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 1400:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)


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
        if self.isDead > 1000:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)


class fox(animal):
    def __init__(self, home, xdim, ydim, baseArea, fps):
        super().__init__("fox", home, xdim, ydim, baseArea, fps)
        tinder4foxes.append((0,0))
        self.matingCooldown = 500
    
    def sniff(self, ani):
        if math.sqrt((abs(ani[0])-abs(self.posn[0]))**2 + (abs(ani[1])-abs(self.posn[1]))**2) <= math.sqrt((abs(self.foodCood[0])-abs(self.posn[0]))**2 + (abs(self.foodCood[1])-abs(self.posn[1]))**2):
                    self.foodCood = [ani[0],ani[1]]

    @lru_cache(maxsize=3)
    def periodic(self, form):
        super().periodic(form, tinder4foxes)
        return(self.posn)
        

    def death(self):
        self.isDead = self.isDead + random.randint(0,3)
        if self.isDead > 1800:
            return(True)


    def canBreed(self):
        if self.mating and self.cantMate == False:
            return(True)