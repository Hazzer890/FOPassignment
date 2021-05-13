import pygame, sys
import random
import time
from pygame.locals import *
from Wombat import *
from Animal import *
from SimulationBase import *

# Variables
numWom = 10
dimX = 700
dimY = 700
Animal1 = []
Foods = []
Waters = []

Yebble = area(dimX, dimY)
baseArea = Yebble.needs()

pygame.init()
FPS = 24
FramePerSec = pygame.time.Clock()

# colour objects
WATERC  = (42, 99, 148)
FOODC   = (238, 185, 2)
BACKGC = (62, 103, 51)
WOMBATC = (49, 42, 33)
PREDATORC = (157, 6, 26)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 1000x1000 pixel display
DISPLAYSURF = pygame.display.set_mode((dimX,dimY))
DISPLAYSURF.fill(BACKGC)
pygame.display.set_caption("Simulation")

# Init Animals
for i in range(numWom):
    yes = True
    while yes:
        randX = random.randint(0,dimX-1)
        randY = random.randint(0,dimY-1)
        if baseArea[randX,randY] != 1:
            yes = False
    Animal1.append(wombat(randX, randY, dimX, dimY, baseArea))

# Generate area
for x in range(dimX):
    for y in range(dimY):
        if baseArea[x,y] == 1:
            Waters.append((x,y))
        elif baseArea[x,y] == 2:
            Foods.append((x,y))

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Draw Area
    for i in range(len(Waters)):
        pygame.draw.rect(DISPLAYSURF, WATERC, (Waters[i][0], Waters[i][1], 10, 10), 2)
    for i in range(len(Foods)):
        pygame.draw.rect(DISPLAYSURF, FOODC, (Foods[i][0], Foods[i][1], 10, 10), 2)
    # Draw animals
    for i in range(len(Animal1)):
        lani = Animal1[i].pos()
        pygame.draw.rect(DISPLAYSURF, BACKGC, (lani[0], lani[1], 7, 7), 2)
        ani = Animal1[i].move()
        pygame.draw.rect(DISPLAYSURF, WOMBATC, (ani[0], ani[1], 7, 7), 2)

    FramePerSec.tick(FPS)