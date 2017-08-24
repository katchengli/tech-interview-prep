def highestFloor(floor):
    totalNumberOfFloors = 100
    drops = 0
    if floor >= totalNumberOfFloors:
        try:
            raise Exception('Floor given greater than the total number of floors available!')
        except Exception as inst:
            return inst

    secondEgg = totalNumberOfFloors // 2
    broken = False
    firstEgg = 0

    while not broken and firstEgg+1 < totalNumberOfFloors:
        # dropping second egg!
        drops += 1
        if secondEgg > floor:
            broken = True
        else:
            firstEgg = secondEgg
            secondEgg = (totalNumberOfFloors - secondEgg)//2 + secondEgg

    if broken == False:
        print('drops: ' + str(drops))
        return firstEgg

    for i in range(firstEgg, totalNumberOfFloors):
        drops += 1
        firstEgg = i
        if firstEgg > floor:
            print('drops: ' + str(drops))
            return firstEgg-1



print(highestFloor(7))
print(highestFloor(100))
print(highestFloor(99))
print(highestFloor(49))

import math

def highestFloor2(floor):
    skip = math.floor(math.sqrt(floor))

    totalNumberOfFloors = 100
    drops = 0
    if floor >= totalNumberOfFloors:
        try:
            raise Exception('Floor given greater than the total number of floors available!')
        except Exception as inst:
            return inst

    secondEgg = skip
    broken = False
    firstEgg = 0

    while not broken and firstEgg+1 < totalNumberOfFloors:
        # dropping second egg!
        drops += 1
        if secondEgg > floor:
            broken = True
        else:
            firstEgg = secondEgg
            secondEgg = skip + secondEgg

    if broken == False:
        print('drops: ' + str(drops))
        return firstEgg

    for i in range(firstEgg, totalNumberOfFloors):
        drops += 1
        firstEgg = i
        if firstEgg > floor:
            print('drops: ' + str(drops))
            return firstEgg-1

print(highestFloor2(7))
print(highestFloor2(100))
print(highestFloor2(99))
print(highestFloor2(49))

def highestFloor3(floor):
    
