from collections import deque

def findNeighbours(current, columnHeight, rowLength):
    firstRow = (current[0] == 0)
    lastRow = (current[0] == (columnHeight-1))
    firstColumn = (current[1] == 0)
    lastColumn = (current[1] == (rowLength-1))

    neighbours = list()

    # Adding the top neighbours
    if not firstRow:
        neighbours.append((current[0]-1, current[1]))
        if not firstColumn:
            neighbours.append((current[0]-1, current[1]-1))
        if not lastColumn:
            neighbours.append((current[0]-1, current[1]+1))
    #Adding the bottom neighbours
    if not lastRow:
        neighbours.append((current[0]+1, current[1]))
        if not firstColumn:
            neighbours.append((current[0]+1, current[1]-1))
        if not lastColumn:
            neighbours.append((current[0]+1, current[1]+1))
    #Adding the side neighbours
    if not firstColumn:
        neighbours.append((current[0], current[1]-1))
    if not lastColumn:
        neighbours.append((current[0], current[1]+1))

    return neighbours

def visitIsland(grid, current, visited):
    islandSet = 1
    visitingList = findNeighbours(current, len(grid), len(grid[0]))

    while visitingList:
        current = visitingList.pop()
        if current not in visited:
            visited.add(current)
            if grid[current[0]][current[1]] == 1:
                islandSet += 1
                visitingList = visitingList + findNeighbours(current, len(grid), len(grid[0]))

    return islandSet, visited

def getBiggestRegion(grid):
    largestSet = 0
    visited = set()
    nbRows = len(grid)
    nbCols = len(grid[0])

    for i in range(nbRows):
        for j in range(nbCols):
            current = (i, j)
            if current not in visited:
                visited.add(current)
                if grid[current[0]][current[1]] == 1:
                    islandSet, visited = visitIsland(grid, current, visited)
                    if islandSet > largestSet:
                        largestSet = islandSet

    return largestSet

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))




#
# 8
# 9
# 0 1 0 0 0 0 1 1 0
# 1 1 0 0 1 0 0 0 1
# 0 0 0 0 1 0 1 0 0
# 0 1 1 1 0 1 0 1 1
# 0 1 1 1 0 0 1 1 0
# 0 1 0 1 1 0 1 1 0
# 0 1 0 0 1 1 0 1 1
# 1 0 1 1 1 1 0 0 0
#
# 29
