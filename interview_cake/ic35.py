def in_place_shuffle(shuffleList):
    listLength = len(shuffleList)

    for i in range(0, listLength):
        ix = get_random(0, listLength)


    return shuffleList

# Gives a random integer that is >= floor and <= ceiling.
def get_random(floor, ceiling):
    pass

def shuffling(shuffleList):
    listLength = len(shuffleList)
    newList = [0]*listLength
    for i in range(0, len(shuffleList)):
        ix = get_random(0, listLength)
        newList[i] = shuffleList[ix]
        del(shuffleList[ix])
        listLength -= 1

    return shuffleList

def in_place_shuffling(shuffleList):

    for i in range(0, len(shuffleList)):
        ix = get_random(i, len(shuffleList))

        if ix != i:
            shuffleList[i], shuffleList[ix] = shuffleList[ix], shuffleList[i]

    return shuffleList
