#
# ChosenAnimals.py -  Contains the Classes for the chosen simulated animals
#

from Animal import * 

class bird(animal):
    def __init__(self, home):
        super().__init__(self, home)
        self.alti = 0