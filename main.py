import pygame, sys, random
from pygame.locals import *
from Wombat import *
from Animal import *
from SimulationBase import *

# Variables
fps = 10
dimX = 700
dimY = 700
Animal1 = []
Foods = []
Waters = []

ani = []

Yebble = area(dimX, dimY)
baseArea = Yebble.needs()

pygame.init()
FPS = fps
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
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Animal1.append(wombat(randXY, dimX, dimY, baseArea, fps))

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
        pygame.draw.rect(DISPLAYSURF, FOODC, (Foods[i][0], Foods[i][1], 8, 8), 2)
    # Draw Wombats
    for i in range(numWom):
        lani = Animal1[i].pos()
        pygame.draw.rect(DISPLAYSURF, BACKGC, (lani[0], lani[1], 7, 7), 2)
        ani = Animal1[i].periodic(i)
        pygame.draw.rect(DISPLAYSURF, WOMBATC, (ani[0], ani[1], 7, 7), 2)
        # Check Wombat Interaction
        for j in range(len(Animal1)):
            if Animal1[i].pos() == Animal1[j].pos() and i != j and Animal1[i].canBreed():
                numWom = numWom + 1
                Animal1.append(wombat([(Animal1[j].pos()[0]+Animal1[i].pos()[0])/2, (Animal1[j].pos()[1]+Animal1[i].pos()[1])/2], dimX, dimY, baseArea, fps))
                Animal1[i].mate()
                Animal1[j].mate()
                print("sex")
    for i in range(numWom):
        try:
            if Animal1[i].death():
                ani = Animal1[i].periodic(i)
                numWom = numWom - 1
                pygame.draw.rect(DISPLAYSURF, BACKGC, (ani[0]-5, ani[1]-5, 17, 17), 0)
                Animal1.pop(i)
                print("death")
        except:
            print('bithc')

    FramePerSec.tick(FPS)