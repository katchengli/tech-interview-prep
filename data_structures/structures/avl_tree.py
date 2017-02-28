from structures.avl_node import AVLNode

class AVLTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = AVLNode(None, value)
            return self.root

        currentNode = self.root
        while True:
            if value < currentNode.value:
                if currentNode.leftChild == None:
                    currentNode.leftChild = AVLNode(currentNode, value)
                    self.balanceTree(currentNode.leftChild)
                else:
                    currentNode = currentNode.leftChild
            else:
                if currentNode.rightChild == None:
                    currentNode.rightChild = AVLNode(currentNode, value)
                    self.balanceTree(currentNode.rightChild)
                else:
                    currentNode = currentNode.rightChild

    def balanceTree(self, child):
        parent = child.parent
        if child.balanceFactor > 1 or child.balanceFactor < -1:
            self.rebalanceTree(child)
            return

        if parent != None:
            if child == parent.leftChild:
                parent.balanceFactor += 1
            elif child == parent.rightChild:
                parent.balanceFactor -= 1

            if parent.parent.balanceFactor != 0:
                self.updateBalance(parent)

    def updateBalance(self, node):



    def __str__(self):
        return str(self.root)
