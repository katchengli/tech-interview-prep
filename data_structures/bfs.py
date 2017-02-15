from structures.tree import Tree
from queue import Queue

class BFS(object):
    def __init__(self):
        self.tree = Tree()

    def breadth_first_search(self, val):
        scanQueue = Queue()

        scanQueue.put(self.tree.root)

        while not scanQueue.empty():
            currentNode = scanQueue.get()
            if currentNode.value == val:
                return True
            else:
                if currentNode.leftChild is not None:
                    scanQueue.put(currentNode.leftChild)
                if currentNode.rightChild is not None:
                    scanQueue.put(currentNode.rightChild)

        return False


if __name__ == "__main__":
    bfs = BFS()
    bfs.tree.populateTree([5,4,5,6,7,8,1,2,9])
    print(bfs.tree)
    print(bfs.breadth_first_search(45))
    print(bfs.breadth_first_search(4))
    print(bfs.breadth_first_search(7))
    print(bfs.breadth_first_search(5))
    print(bfs.breadth_first_search(-3))
