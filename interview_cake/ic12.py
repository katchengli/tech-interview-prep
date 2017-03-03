# Guess -> implement binary search -> O(log n)
# update: Guess was right!
# will implement for the exercise

def checkInList(numberList, num):
    # these need to be outside indexes
    firstIx = -1
    lastIx = len(numberList)


    while firstIx+1 < lastIx:
        midDist = (lastIx - firstIx) // 2
        midIx = firstIx + midDist

        if num == numberList[midIx]:
            return True
        elif num < numberList[midIx]:
            lastIx = midIx
        elif num > numberList:
            firstIx = midIx

    return False
