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

    def move(self):
        self.posn[0] = self.posn[0] + 1
        self.posn[1] = self.posn[1] + 1
        return(self.posn)