from structures.tree import Tree

class BinarySearchTree(Tree):
    def __init__(self):
        super().__init__()

    def populateTree(self, valuesList):
        #check empty list
        valuesList = list(set(valuesList))
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

        def findValue(self, value):
            continue
