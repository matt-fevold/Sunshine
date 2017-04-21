import random
#generate 1d world




def generateWorld(X,World):
    for x in range(X):
        #flatten the world
        world.append(generateZero())
        #add life to the world
    for x in range(X):
        World[x] = randomize()
        

def randomize():
    #random.randInt(0,3)
    
    return random.choice([generateZero(),generateZero(),generateOne(),generateTwo()])

def debug(World):
    print("Randomness Checker")
    checkRandomness(World)
    print("\nPrint out of world")
    printWorld(World)

def printWorld(World):
    for x in range(len(World)+10): 
        print("_", end="")

    print()

    #display content    
    for x in range(1):    
        print(x, "||", end=" ")
        for y in range(len(world)):
            print(world[y], end='')
        print(" ||", end=" ")
        print()

def generateZero():
    return 0

def generateOne():
    return 1

def generateTwo():
    return 2

def outputWorld(World,filePath):
    print("\nwriting to : " , filePath)
    f = open(filePath,'w')
    for x in range(len(World)):
        f.write(str(World[x]))

    f.close()    
    return 0

def checkRandomness(World):
    zero = 0
    one  = 0
    two  = 0

    for x in range(len(World)):
        if(World[x]==0):
            zero+=1
        if(World[x]==1):
            one+=1
        if(World[x]==2):
            two+=2
    print("0: " , zero)
    print("1: " , one)
    print("2: " , two)

import timeit
start = timeit.default_timer()
         
x_size = 1500
world = []

generateWorld(x_size,world)
#debug(world)
outputWorld(world,"C:\\tools\\test.txt")

stop = timeit.default_timer()

print("World generation execution time: " , stop - start) 
