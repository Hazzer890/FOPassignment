import pygame, sys
import random
from pygame.locals import *
from ChosenAnimals import *
from Animal import *
from SimulationBase import *

# Variables
dimX = 1000
dimY = 1000
Animal1 = []

Yebble = area(dimX, dimY)
baseArea = Yebble.needs()

pygame.init()
FPS = 30
FramePerSec = pygame.time.Clock()

# colour objects
WATERC  = (42, 68, 148)
FOODC   = (238, 185, 2)
BACKGC = (62, 86, 65)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 1000x1000 pixel display
DISPLAYSURF = pygame.display.set_mode((dimX,dimY))
DISPLAYSURF.fill(BACKGC)
pygame.display.set_caption("Simulation")

# Init Animals
for i in range(20):
    randX = random.randint(0,dimX-1)
    randY = random.randint(0,dimY-1)
    Animal1.append(bird(randX, randY))

# Draw area
for i in range(20):
    ani = Animal1[i].pos()
    pygame.draw.rect(DISPLAYSURF, BLACK, (ani[0], ani[1], 2, 2), 2)
for x in range(dimX):
    for y in range(dimY):
        if baseArea[x,y] == 1:
            pygame.draw.rect(DISPLAYSURF, WATERC, (x, y, 2, 2), 2)
        elif baseArea[x,y] == 2:
            pygame.draw.rect(DISPLAYSURF, FOODC, (x, y, 10, 10), 2)

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)