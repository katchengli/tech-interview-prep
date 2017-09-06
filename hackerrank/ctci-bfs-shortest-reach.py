from collections import deque;
class Graph:
    def __init__(self, nbrNodes):
        self.nbrNodes = nbrNodes
        self.matrix = [[-1 for i in range(nbrNodes)] for j in range(nbrNodes)]

    def connect(self, x, y):
        self.matrix[x][y] = 6
        self.matrix[y][x] = 6

    def getNeighbours(self, current, unvisited):
        neighbours = list()
        for i in range(self.nbrNodes):
            if i == current:
                continue
            if self.matrix[current][i] > 0 and i in unvisited:
                neighbours.append(i)
        return neighbours

    def find_all_distances(self, startNode):
        visitingDeque = deque()
        nextDeque = deque()
        visitingDeque.append(startNode)
        unvisited = set(i for i in range(self.nbrNodes))
        currentDistance = 0

        while visitingDeque:
            current = visitingDeque.popleft()

            if current not in unvisited:
                if not visitingDeque:
                    visitingDeque = nextDeque
                    currentDistance += 6
                    nextDeque = deque()
                continue

            unvisited.remove(current)
            nextDeque.extend(self.getNeighbours(current, unvisited))

            if current != startNode:
                if currentDistance <= self.matrix[startNode][current] or self.matrix[startNode][current] < 0:
                    self.matrix[startNode][current] = currentDistance

            if not visitingDeque:
                visitingDeque = nextDeque
                currentDistance += 6
                nextDeque = deque()

        toPrint = ''
        for i in range(self.nbrNodes):
            if i != startNode:
                toPrint = toPrint + str(self.matrix[startNode][i]) + ' '

        print(toPrint)

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
