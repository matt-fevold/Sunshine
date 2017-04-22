import random
#generate 1d world

def generateWorld(X,World,TurnCount,Age):
    for x in range(X):
        #flatten the world
        world.append(generateZero(0))
        #add life to the world
    for y in range(TurnCount):
        for x in range(X):
            World[x] = randomize(World[x])
    for x in range(len(World)):
            print(World[x],end="")

    graph(World)

    for x in range(Age):        
        levelOut(World,1)

    print("\n\n")
    graph(World)

def randomize(val):    
    return random.choice([staySame(val),staySame(val),staySame(val),
                          generateUpOne(val),generateUpOne(val),
                          generateUpTwo(val),
                          generateDownOne(val),generateDownTwo(val)])

def debug(World,simple):
    print("Randomness Checker")
    Counter = checkRandomness(World)
    print("\nPrint out of world")
    if(simple):
        printWorld(World,True)
    else:
        printWorld(World,False)
    #graph(World)


def printWorld(World,simple):
    if(simple):
        for x in range(len(World)):
            print(World[x],end="")

    else:
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


def levelOut(World,Amount):
    for x in range(len(World)):
        if(x<len(World)-1):            
            if(World[x+1]>World[x]):
                World[x]+=Amount
                World[x+1]-=Amount
        

def staySame(val):
    return val

def generateZero(val):
    return 0

def generateDownOne(val):
    if(val >= 1):
        return val-1
    else:
        return val

def generateDownTwo(val):
    if(val >=2):
        return val-2
    else:
        return val
        
def generateUpOne(val):
    return val+1

def generateUpTwo(val):
    return val+2

def outputWorld(World,filePath):
    print("\nwriting to : " , filePath)
    f = open(filePath,'w')
    for x in range(len(World)):
        f.write(str(World[x]))

    f.close()    
    return 0

def checkRandomness(World):
    counter = [0 for x in range(max(World)+1)]

    for x in range(len(World)):
        counter[World[x]] +=1
    for x in range(len(counter)):
        print (x, " : ", counter[x])
    return counter


def graph(World):
    print(" \n=" , len(World))
    for y in range(max(World)):
        for x in range(len(World)):
            if(World[x]>y):
                print("X",end="")
            else:
                print(" ",end="")
        print()
            

import timeit
start = timeit.default_timer()
         
x_size = 150
world = []

generateWorld(x_size,world,20,20)
debug(world,True)
outputWorld(world,"C:\\tools\\test.txt")

stop = timeit.default_timer()

print("World generation execution time: " , stop - start) 


