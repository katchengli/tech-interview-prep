class IntervalTreeNode(object):
    def __init__(self, valuesTuple, maxHigh):
        self.interval = valuesTuple
        self.leftChild = None
        self.rightChild = None
        self.maxHigh = maxHigh

class IntervalTree(object):
    def __init__(self, tuplesList):
        self.root = None
        if tuplesList:
            for interval in tuplesList:
                self.insertInterval(self.root, interval)

    def insertInterval(self, currentNode, interval):
        if self.root is None:
            self.root = IntervalTreeNode(interval, interval[1])
            return

        low = currentNode.interval[0]

        if interval[0] < low:
            if currentNode.leftChild is None:
                currentNode.leftChild = IntervalTreeNode(interval, interval[1])
            else:
                self.insertInterval(currentNode.leftChild, interval)
        else:
            if currentNode.rightChild is None:
                currentNode.rightChild = IntervalTreeNode(interval, interval[1])
            else:
                self.insertInterval(currentNode.rightChild, interval)

        if currentNode.maxHigh < interval[1]:
            currentNode.maxHigh = interval[1]

    def getOverlappingIntervals(self):
        overlapIntervals = list()

        if self.root is None:
            return None

        inorderStack = list()
        node = self.root

        while inorderStack or node is not None:
            if node is not None:
                inorderStack.append(node)
                node = node.leftChild
            else:
                node = inorderStack.pop()
                overlapIntervals = self.updateIntervals(node, overlapIntervals)
                node = node.rightChild

        return overlapIntervals

    def updateIntervals(self, node, intervalList):
        if not intervalList:
            intervalList.append(node.interval)
            return intervalList

        interval = intervalList[len(intervalList)-1]
        if node.interval[0] > interval[1]:
            intervalList.append(node.interval)
            return intervalList
        else:
            if node.interval[1] > interval[1]:
                interval = (interval[0], node.interval[1])
                intervalList[len(intervalList)-1] = interval
            #else nothing to update
        return intervalList

class HiCal(object):
    def __init__(self, meetings):
        self.meetings = meetings

    def createMeetingsTree(self):
        self.meetingsTree = IntervalTree(self.meetings)

    def merge_ranges(self):
        ranges = self.meetingsTree.getOverlappingIntervals()
        return ranges


if __name__ == "__main__":
    hiCal = HiCal([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

    print([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

    hiCal = HiCal([(1,2), (2,3)])
    hiCal = HiCal([(1,5), (2, 3)])
    hiCal = HiCal([(1, 10), (2, 6), (3, 5), (7, 9)])
    hiCal.createMeetingsTree()
    print(hiCal.merge_ranges())
