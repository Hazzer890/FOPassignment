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
Foxes = []
Foods = []
Waters = []
aniW = []
aniE = []
aniK = []
kangpos = []
aniF = []
time = 7.0

Yebble = area(dimX, dimY)
baseArea = Yebble.needs()

pygame.init()
FPS = fps
FramePerSec = pygame.time.Clock()

# colour obj-1ects
WATERC  = (92, 114, 170)
FOODC   = (238, 185, 2)
BACKGC = (159, 180, 112)
WOMBATC = (98, 84, 65)
EMUC = (102, 107, 120)
KANGAROOC = (130, 106, 97)
PREDATORC = (157, 6, 26)

# Setup a 1000x1000 pixel display
DISPLAY = pygame.display.set_mode((dimX,dimY))
DISPLAY.fill(BACKGC)
pygame.display.set_caption("Simulation Window")

#load images
womimg = pygame.image.load('images/wombat.png')
womimg.convert()
emuimg = pygame.image.load('images/emu.png')
emuimg.convert()
kangimg = pygame.image.load('images/kangaroo.png')
kangimg.convert()
foximg = pygame.image.load('images/fox.png')
foximg.convert()
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
    
# Init Kangaroo
for i in range(numKangaroo):
    yes = True
    while yes:
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Kangaroos.append(kangaroo(randXY, dimX, dimY, baseArea, fps))

# Init Foxes
for i in range(numFoxes):
    yes = True
    while yes:
        randXY = [random.randint(50,dimX-50),  random.randint(50,dimY-50)]
        if baseArea[randXY[0],randXY[1]] != 1:
            yes = False
    Foxes.append(fox(randXY, dimX, dimY, baseArea, fps))
    
# Generate area
for x in range(dimX):
    for y in range(dimY):
        if baseArea[x,y] == 1:
            Waters.append((x,y))
        elif baseArea[x,y] == 2:
            Foods.append((x,y))

# Game Loop
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
    for i in range(len(Wombats)):
        if time > 6 and time < 22: Wombats[i].periodic(i)
        aniW = Wombats[i].posn
        DISPLAY.blit(womimg, (aniW[0], aniW[1]))
        for i in range(numFoxes):
            Foxes[i].sniff(aniW)
        # Check Wombat Interaction
        for j in range(numWom):
            if i < len(Wombats) and j < len(Wombats):
                if Wombats[i].posn == Wombats[j-1].posn and i != j-1 and Wombats[i].canBreed():
                    Wombats.append(wombat([(Wombats[j-1].posn[0]+Wombats[i].posn[0])/2, (Wombats[j-1].posn[1]+Wombats[i].posn[1])/2], dimX, dimY, baseArea, fps))
                    Wombats[i].mate()
                    Wombats[j-1].mate()
                    numWom = numWom + 1
                    break
    #Draw Emus
    for i in range(numEmu-1):
        if time > 5 and time < 20: Emus[i].periodic(i)
        aniE = Emus[i].posn
        DISPLAY.blit(emuimg, (aniE[0], aniE[1]))
        for i in range(numFoxes):
            Foxes[i].sniff(aniE)
        # Check Wombat Interaction
        for j in range(numEmu):
            if i < len(Emus) and j < len(Emus):
                if Emus[i].posn == Emus[j-1].posn and i != j-1 and Emus[i].canBreed():
                    Emus.append(emu([(Emus[j-1].posn[0]+Emus[i].posn[0])/2, (Emus[j-1].posn[1]+Emus[i].posn[1])/2], dimX, dimY, baseArea, fps))
                    Emus[i].mate()
                    Emus[j-1].mate()
                    numEmu = numEmu + 1
                    break
    #Draw kangaroos
    for i in range(numKangaroo):
        if time > 3 and time < 19:  Kangaroos[i].periodic(i)
        aniK = Kangaroos[i].posn
        DISPLAY.blit(kangimg, (aniK[0], aniK[1]))
        for i in range(numFoxes):
            Foxes[i].sniff(aniK)
        # Check Kangaroo Interaction
        for j in range(numKangaroo):
            if i < len(Kangaroos) and j < len(Kangaroos):
                if Kangaroos[i].posn == Kangaroos[j-1].posn and i != j-1 and Kangaroos[i].canBreed():
                    Kangaroos.append(kangaroo([(Kangaroos[j-1].posn[0]+Kangaroos[i].posn[0])/2, (Kangaroos[j-1].posn[1]+Kangaroos[i].posn[1])/2], dimX, dimY, baseArea, fps))
                    Kangaroos[i].mate()
                    Kangaroos[j-1].mate()
                    numKangaroo = numKangaroo + 1
                    break
    #Draw Foxes
    for i in range(numFoxes):
        if time > 5 and time < 20: 
            Foxes[i].periodic(i)
        aniF = Foxes[i].posn
        DISPLAY.blit(foximg, (aniF[0], aniF[1]))
        # Check Wombat Interaction
        for j in range(len(Foxes)):
            if Foxes[i].posn == Foxes[j-1].posn and i != j-1 and Foxes[i].canBreed():
                numFoxes = numFoxes + 1
                Foxes.append(fox([(Foxes[j-1].posn[0]+Foxes[i].posn[0])/2, (Foxes[j-1].posn[1]+Foxes[i].posn[1])/2], dimX, dimY, baseArea, fps))
                Foxes[i].mate()
                Foxes[j].mate()
                break
        for j in range(numWom-1):
            if Foxes[i].posn == Wombats[j].posn:
                for z in range(numFoxes):
                    Foxes[z].foodCood = (-1000,-1000)
                Wombats.pop(j)
                numWom = numWom - 1
                break
        for j in range(numEmu):
            if Foxes[i].posn == Emus[j].posn:
                for z in range(numFoxes):
                    Foxes[z].foodCood = (-1000,-1000)
                Emus.pop(j)
                numEmu = numEmu - 1
                break
        for j in range(numKangaroo-1):
            if Foxes[i].posn == Kangaroos[j].posn:
                for z in range(numFoxes):
                    Foxes[z].foodCood = (-1000,-1000)
                Kangaroos.pop(j)
                numKangaroo = numKangaroo - 1
                break
    #Kill Wombats
    for i in range(numWom):
        try:
            if Wombats[i].death():
                aniW = Wombats.pop(i).periodic(i)
                numWom = numWom - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniW[0]-5, aniW[1]-5, 17, 17), 0)
                print("Wdeath")
        except:
            pass
    #Kill Emus
    for i in range(numEmu):
        try:
            if Emus[i].death():
                aniE = Emus.pop(i).periodic(i)
                numEmu = numEmu - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniE[0]-5, aniE[1]-5, 17, 17), 0)
                print("Edeath")
        except:
            pass
    #Kill Kangaroos
    for i in range(numKangaroo):
        try:
            if Kangaroos[i].death():
                aniK = Kangaroos.pop(i).periodic(i)
                numKangaroo = numKangaroo - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniK[0]-5, aniK[1]-5, 17, 17), 0)
                print("Kdeath")
        except:
            pass
    #Kill Foxes   
    for i in range(numFoxes):
        try:
            if Foxes[i].death():
                aniF = Foxes.pop(i).periodic(i)
                numFoxes = numFoxes - 1
                pygame.draw.rect(DISPLAY, BACKGC, (aniF[0]-5, aniF[1]-5, 17, 17), 0)
                print("Fdeath")
        except:
            pass
    
    #Day/Night Cycle 
    # if time >= 24: time = 0.0
    # else: time += 0.05
    # #Day/Night Visualisation
    # if time > 19: BACKGC, WATERC, night = (159 * night, 180 * night, 112 * night), (92 * night, 114 * night, 170 * night), night - 0.009
    # elif time < 5: BACKGC, WATERC, night = (159 * night, 180 * night, 112 * night), (92 * night, 114 * night, 170 * night), night + 0.009
    # else: BACKGC, night = (159, 180, 112), 1.0

    FramePerSec.tick(FPS)