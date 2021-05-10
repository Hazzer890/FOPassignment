import pygame, sys
from pygame.locals import *
from ChosenAnimals import *
from Animal import *
from SimulationBase import *

Yebble = area(1000, 1000)
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
DISPLAYSURF = pygame.display.set_mode((1000,1000))
DISPLAYSURF.fill(BACKGC)
pygame.display.set_caption("Simulation")

for x in range(1000):
    for y in range(1000):
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