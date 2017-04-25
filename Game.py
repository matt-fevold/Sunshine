#play game
import sys

import pygame


from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
surface = pygame.Surface((100, 100))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue


        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            done = True
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        else:
            

            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_LEFT]: x -= 3
            if pressed[pygame.K_RIGHT]: x += 3
            
            
            screen.fill((0, 0, 0))
            if is_blue: color = (0, 128, 255)
            else: color = (255, 100, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
            
            pygame.display.flip()
            clock.tick(60)


def readInWorld(filepath):
    tempWorld = []
    World = []
    
    with open(filepath,"r") as file:
        for x in file.readline():
            tempWorld.append(file)

    #print (tempWorld[0])
            
    return World
        



def graph(World):
    print(" \n=" , len(World))
    for y in reversed(range(max(World))):
        for x in range(len(World)):
            if(World[x]>y):
                print("X",end="")
            else:
                print(" ",end="")
        print()


#world = readInWorld("C:\\tools\\test.txt")
#print(world[0])
#graph(world)
