import pygame, sys, random
from pygame.locals import *
from Animal import *
from AnimalClasses import *
from SimulationBase import *

# Variables
fps = 30
dimX, dimY = 700, 700
Wombats = []
Emus = []
Kangaroos = []
Foods = []
Waters = []
aniW = []
aniE = []
aniK = []
time = 7.0

Yebble = area(dimX, dimY)
baseArea = Yebble.needs()

pygame.init()
FPS = fps
FramePerSec = pygame.time.Clock()

# colour objects
WATERC  = (92, 114, 170)
FOODC   = (238, 185, 2)
BACKGC = (159, 180, 112)
WOMBATC = (98, 84, 65)
EMUC = (102, 107, 120)
KANGAROOC = (14, 6, 8)
PREDATORC = (157, 6, 26)

# Setup a 1000x1000 pixel display
DISPLAY = pygame.display.set_mode((dimX,dimY))
DISPLAY.fill(BACKGC)
pygame.display.set_caption("Simulation")

#load images
womimg = pygame.image.load('images/wombat.png')
womimg.convert()
emuimg = pygame.image.load('images/emu.png')
emuimg.convert()
kangimg = pygame.image.load('images/kangaroo.png')
kangimg.convert()
treeimg = pygame.image.load('images/tree.png')
treeimg.convert()

# Init Wombat
for i in range(numWom):
    yes = True
    while yes:
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Wombats.append(wombat(randXY, dimX, dimY, baseArea, fps))

# Init Emu
for i in range(numEmu):
    yes = True
    while yes:
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Emus.append(emu(randXY, dimX, dimY, baseArea, fps))

# Init kangaroo
for i in range(numkangaroo):
    yes = True
    while yes:
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Kangaroos.append(kangaroo(randXY, dimX, dimY, baseArea, fps))

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
    DISPLAY.fill(BACKGC)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Draw Area
    for i in range(len(Waters)):
        pygame.draw.rect(DISPLAY, WATERC, (Waters[i][0], Waters[i][1], 10, 10), 2)
    for i in range(len(Foods)):
        DISPLAY.blit(treeimg, (Foods[i][0], Foods[i][1]))
   
    # Draw Wombats
    for i in range(numWom):
        if time > 6 and time < 22: Wombats[i].periodic(i)
        aniW = Wombats[i].posn
        DISPLAY.blit(womimg, (aniW[0], aniW[1]))
        # Check Wombat Interaction
        for j in range(len(Wombats)):
            if Wombats[i].posn == Wombats[j].posn and i != j and Wombats[i].canBreed():
                numWom = numWom + 1
                Wombats.append(wombat([(Wombats[j].posn[0]+Wombats[i].posn[0])/2, (Wombats[j].posn[1]+Wombats[i].posn[1])/2], dimX, dimY, baseArea, fps))
                Wombats[i].mate()
                Wombats[j].mate()
    #Draw Emus
    for i in range(numEmu):
        if time > 5 and time < 20: Emus[i].periodic(i)
        aniE = Emus[i].posn
        DISPLAY.blit(emuimg, (aniE[0], aniE[1]))
        # Check Wombat Interaction
        for j in range(len(Emus)):
            if Emus[i].posn == Emus[j].posn and i != j and Emus[i].canBreed():
                numEmu = numEmu + 1
                Emus.append(emu([(Emus[j].posn[0]+Emus[i].posn[0])/2, (Emus[j].posn[1]+Emus[i].posn[1])/2], dimX, dimY, baseArea, fps))
                Emus[i].mate()
                Emus[j].mate()
    #Draw kangaroos
    for i in range(numkangaroo):
        if time > 3 and time < 19:  Kangaroos[i].periodic(i)
        aniK = Kangaroos[i].posn
        DISPLAY.blit(kangimg, (aniK[0], aniK[1]))
        # Check Kangaroo Interaction
        for j in range(len(Kangaroos)):
            if Kangaroos[i].posn == Kangaroos[j].posn and i != j and Kangaroos[i].canBreed():
                numkangaroo = numkangaroo + 1
                Kangaroos.append(kangaroo([(Kangaroos[j].posn[0]+Kangaroos[i].posn[0])/2, (Kangaroos[j].posn[1]+Kangaroos[i].posn[1])/2], dimX, dimY, baseArea, fps))
                Kangaroos[i].mate()
                Kangaroos[j].mate()
    #Kill Wombats
    for i in range(numWom):
        try:
            if Wombats[i].death():
                aniW = Wombats[i].periodic(i)
                numWom = numWom - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniW[0]-5, aniW[1]-5, 17, 17), 0)
                Wombats.pop(i)
                print("death")
        except:
            pass
    #Kill Emus
    for i in range(numEmu):
        try:
            if Emus[i].death():
                aniE = Emus[i].periodic(i)
                numEmu = numEmu - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniE[0]-5, aniE[1]-5, 17, 17), 0)
                Emus.pop(i)
                print("Edeath")
        except:
            pass
    #Kill Kangaroos
    for i in range(numkangaroo):
        try:
            if Kangaroos[i].death():
                aniK = Kangaroos[i].periodic(i)
                numkangaroo = numkangaroo - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniK[0]-5, aniK[1]-5, 17, 17), 0)
                Kangaroos.pop(i)
                print("Edeath")
        except:
            pass
    
    #Day/Night Cycle 
    if time >= 24: time = 0.0
    else: time += 0.05
    #Visualisation
    if time > 19: BACKGC, WATERC, night = (159 * night, 180 * night, 112 * night), (92 * night, 114 * night, 170 * night), night - 0.009
    elif time < 5: BACKGC, WATERC, night = (159 * night, 180 * night, 112 * night), (92 * night, 114 * night, 170 * night), night + 0.009
    else: BACKGC, night = (159, 180, 112), 1.0

    FramePerSec.tick(FPS)