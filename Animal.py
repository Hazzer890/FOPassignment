# 
# Animal.py - Contains the Animal Class and the involved funtions
#

import random

class animal():
    def __init__(self, name, home, population):
        self.name = name
        self.home = home #[x, y]
        self.popu = population
        self.gndr = random.randint(0, 1) # 0 is female, 1 is male

        self.posn = [home[0], home[1]]