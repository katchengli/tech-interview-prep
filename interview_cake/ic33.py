def findDuplicate(n, numbersList):
    nSet = set(numbersList)

    for n in numbersList:
        if n in nSet:
            nSet.remove(n)
        else:
            nSet.add(n)

    return nSet.pop()

print(findDuplicate(5, [1, 3, 4, 2, 5, 4]))

def findDuplicate2(n, numbersList):
    sumListWithoutDuplicates = (n*(n+1))//2

    for num in numbersList:
        sumListWithoutDuplicates -= num

    return sumListWithoutDuplicates*-1

print(findDuplicate2(5, [1, 3, 4, 2, 5, 4]))
print(findDuplicate2(6, [1, 3, 2, 2, 5, 4, 6]))
