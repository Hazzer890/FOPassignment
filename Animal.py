# 
# Animal.py - Contains the Animal Class and the involved funtions
#

import random

class animal():
    def __init__(self, name, homeX, homeY):
        self.name = name
        self.homeX = homeX 
        self.homeY = homeY
        self.gndr = random.randint(0, 1) # 0 is female, 1 is male

        self.posn = [homeX, homeY]
