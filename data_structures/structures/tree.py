from structures.node import Node

class Tree(object):
    def __init__(self):
        self.root = Node()

    def populateTree(self, valuesList):
        # Assumes a binary tree and populates it like a binary search tree without removing duplicates
        #check empty list
        self.root.value = valuesList[0]
        for i in range(1, len(valuesList)):
            currentNode = self.root
            inserted = False
            while not inserted:
                if currentNode.value >= valuesList[i]:
                    if currentNode.leftChild == None:
                        currentNode.leftChild = Node()
                        currentNode.leftChild.value = valuesList[i]
                        inserted = True
                    else:
                        currentNode = currentNode.leftChild
                else:
                    if currentNode.rightChild == None:
                        currentNode.rightChild = Node()
                        currentNode.rightChild.value = valuesList[i]
                        inserted = True
                    else:
                        currentNode = currentNode.rightChild

    def __str__(self):
        return str(self.root)
