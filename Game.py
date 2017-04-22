#play game



def readInWorld(filepath):
    tempWorld = []
    World = []
    
    with open(filepath,"r") as file:
        for x in file:
            tempWorld.append(x)

    for x in range(len(tempWorld)):
        World = tempWorld.split()
            
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


world = readInWorld("C:\\tools\\test.txt")
print(world[0])
#graph(world)
