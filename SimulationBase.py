import random
import numpy as np

#  0 = nothing
#  1 = water
#  2 = food

class area():
    def __init__(self, xDim, yDim):
        self.xDim = xDim
        self.yDim = yDim
        self.numF = 5   # 5 food sources per 500^2
        
        self.baseArea = np.zeros((self.xDim, self.yDim), dtype=int)

    def needs(self):
        # water generation
        waterRad = random.randint(70, 100)
        EPSILON = 10
        water = [0,0]
        water[0] = random.randint(0, self.xDim-1)
        water[1] = random.randint(0, self.yDim-1)
        print("water @", water)

        for y in range(self.yDim):
            for x in range(self.xDim):
                if abs((x-water[0])**2 + (y-water[1])**2 < waterRad**2): # < EPSILON**2
                    self.baseArea[x, y] = 1

        # food generation 
        for i in range(int(((self.xDim * self.yDim)/250000)*self.numF)):
            x, y = random.randint(0, self.xDim-1), random.randint(0, self.yDim-1)
            if self.baseArea[x,y] == 1:
                i = i-1
            else: self.baseArea[x,y] = 2 
        return(self.baseArea)