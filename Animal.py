# 
# Animal.py - Contains the Animal Class and the involved funtions
#

import sys
import math
import random
from functools import lru_cache

import numpy


class animal():
    def __init__(self, name, home, xdim, ydim, baseArea, fps):
        self.name = name
        self.home = home
        self.gndr = random.randint(0, 1) # 0 is female, 1 is male
        self.xdim = xdim
        self.ydim = ydim
        self.baseArea = baseArea
        self.isDead = False

        self.food = False
        self.looking = False
        self.closestFem = (xdim/2,ydim/2)
        self.mating = True
        self.counter = 0
        self.cantMate = True
        self.matingCooldown = 150
        self.fps = fps

        self.posn = [home[0], home[1]]
        
        if name != 'fox':
            # generate distances to food
            listdist = []
            for x in range(self.xdim):
                for y in range(self.ydim):
                    if self.baseArea[x,y] == 2:
                        listdist.append((x-abs(self.posn[0]))**2 + (y-abs(self.posn[1]))**2)

             # find smallest distance
            for x in range(self.xdim):
                for y in range(self.ydim):
                    if self.baseArea[x,y] == 2:
                        if ((x-abs(self.posn[0]))**2 + (y-abs(self.posn[1]))**2) == min(listdist):
                            self.foodCood = [x,y]
        else: self.foodCood = (-1000,-1000)

    def pos(self):
        return(self.posn) # Returns Position when called

    def periodic(self, form, tinder):
        # Pathfinding Code
        if self.food == False:
            #approach food
            if abs((self.foodCood[0]-self.posn[0])) == 0 and abs((self.foodCood[1]-self.posn[1])) == 0: self.food, self.mating = True, True
            elif abs((self.foodCood[0]-self.posn[0])) == 0: self.posn[1] = self.posn[1] + ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
            elif abs((self.foodCood[1]-self.posn[1])) == 0: self.posn[0] = self.posn[0] + ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
            else:
                if self.posn[0] < self.xdim and self.posn[1] < self.ydim:
                    if (self.baseArea[int(self.posn[0]), int(self.posn[1])] == 1):
                        self.posn[0] = self.posn[0] - ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
                        self.posn[1] = self.posn[1] - ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
                self.posn[0] = self.posn[0] + ((self.foodCood[0]-self.posn[0])/abs((self.foodCood[0]-self.posn[0])))
                self.posn[1] = self.posn[1] + ((self.foodCood[1]-self.posn[1])/abs((self.foodCood[1]-self.posn[1])))
        elif self.looking == True and self.gndr == 1:
            #find closest female
            for i in range(len(tinder)): 
                if self.closestFem[0]**2 + self.closestFem[1]**2 < tinder[i][0]**2 + tinder[i][1]**2: self.closestFem = tinder[i]
            #approach closest female
            if self.closestFem != [0,0]:
                if abs((self.closestFem[0]-self.posn[0])) == 0 and abs((self.closestFem[1]-self.posn[1])) == 0: self.food = True
                elif abs((self.closestFem[0]-self.posn[0])) == 0: self.posn[1] = self.posn[1] + ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
                elif abs((self.closestFem[1]-self.posn[1])) == 0: self.posn[0] = self.posn[0] + ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                else:
                    if (self.baseArea[int(self.posn[0]-1), int(self.posn[1]-1)] == 1):
                        self.posn[0] = self.posn[0] - ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                        self.posn[1] = self.posn[1] - ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
                    self.posn[0] = self.posn[0] + ((self.closestFem[0]-self.posn[0])/abs((self.closestFem[0]-self.posn[0])))
                    self.posn[1] = self.posn[1] + ((self.closestFem[1]-self.posn[1])/abs((self.closestFem[1]-self.posn[1])))
        else:
            if self.gndr == 0 and self.mating:
                tinder[form] = (self.posn[0], self.posn[1])
            #approach home
            if (self.home[0]-self.posn[0]) == 0 and (self.home[1]-self.posn[1]) == 0:
                self.looking = True
            elif (self.home[0]-self.posn[0]) == 0:
                self.posn[1] = self.posn[1] + ((self.home[1]-self.posn[1])/abs((self.home[1]-self.posn[1])))
            elif (self.home[1]-self.posn[1]) == 0:
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
            if self.counter > self.matingCooldown:
                self.cantMate = False

        return(self.posn)

    def mate(self):
        hX = True
        hY = True
        self.posn[0] = self.posn[0] + random.randint(-20, 20)
        self.posn[1] = self.posn[1] + random.randint(-20, 20)
        self.home[0] = self.home[0] + random.randint(-50, 50)
        while hX:
            if self.home[0] > self.xdim:
                self.home[0] = self.home[0] + random.randint(-70, -51)
            elif self.home[0] < 0:
                self.home[0] = self.home[0] + random.randint(51, 70)
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
        self.looking = False
        self.mating = False
        self.food = False
        self.cantMate = True