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
                    self.updateBalanceInsert(currentNode.leftChild)
                    return True
                else:
                    currentNode = currentNode.leftChild
            else:
                if currentNode.rightChild == None:
                    currentNode.rightChild = AVLNode(currentNode, value)
                    self.updateBalanceInsert(currentNode.rightChild)
                    return True
                else:
                    currentNode = currentNode.rightChild

    def delete(self, value):
        found = False
        currentNode = self.root
        while not found:
            if currentNode.value == value:
                found = True
                successor = self.findSuccessor(currentNode)
                if successor == None:
                    self.updateBalanceDelete(currentNode)
                else:
                    self.updateBalanceDelete(successor)
                    currentNode.value = successor.value
            elif value < currentNode.value:
                currentNode = currentNode.leftChild
            elif value > currentNode.value:
                currentNode = currentNode.rightChild
            else:
                return False

        return True


    def findSuccessor(self, node):
        if node.leftChild == None and node.rightChild == None:
            return None
        inorderStack = list()
        currentNode = node
        seen = False
        latestPopped = None
        while inorderStack or currentNode is not None:
            if currentNode is not None:
                inorderStack.append(currentNode)
                currentNode = currentNode.leftChild
            else:
                currentNode = inorderStack.pop()
                if currentNode == node and latestPopped is not None:
                    return latestPopped
                latestPopped = currentNode
                if seen:
                    return currentNode
                if currentNode == node:
                    seen = True
                currentNode = currentNode.rightChild

    def updateBalanceInsert(self, child):
        parent = child.parent
        if child.balanceFactor > 1 or child.balanceFactor < -1:
            self.rebalance(child)
            return

        if parent != None:
            if child == parent.leftChild:
                parent.balanceFactor += 1
            elif child == parent.rightChild:
                parent.balanceFactor -= 1

            if parent.balanceFactor != 0:
                self.updateBalanceInsert(parent)

    def updateBalanceDelete(self, child):
        parent = child.parent

        if parent != None:
            updateParent = False
            diffFactor = 0
            if child == parent.leftChild:
                parent.balanceFactor -= 1
                diffFactor = -1
                parent.leftChild = None
                if parent.rightChild == None:
                    updateParent = True
            elif child == parent.rightChild:
                parent.balanceFactor += 1
                diffFactor = 1
                parent.rightChild = None
                if parent.leftChild == None:
                    updateParent = True

            # propagate the height change/balance factor change upwards
            if updateParent:
                while parent != None:
                    if parent.balanceFactor > 1 or parent.balanceFactor < -1:
                        self.rebalance(parent)
                        return

                    parent = parent.parent
                    if parent != None:
                        parent.balanceFactor += diffFactor

    def rotateLeft(self, oldRoot):
        #promote right child in this left rotation
        newRoot = oldRoot.rightChild
        #moving the new root's old left child to the oldRoot
        oldRoot.rightChild = newRoot.leftChild
        #if it wasn't None, change its parent
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = oldRoot
        #change the newRoot's parent
        newRoot.parent = oldRoot.parent
        #if the old root was the tree's root, set the new tree root
        if oldRoot == self.root:
            self.root = newRoot
        else: #Otherwise, set the newRoot as the right or left child of the old parent
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        #set the oldRoot as the left child of the new root
        newRoot.leftChild = oldRoot
        #the parent of the old root is the new root
        oldRoot.parent = newRoot

        #update the balance factors
        oldRoot.balanceFactor = oldRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(oldRoot.balanceFactor, 0)

    def rotateRight(self, oldRoot):
        #promote left child in this right rotation
        newRoot = oldRoot.leftChild
        #moving the new root's old right child to the oldRoot
        oldRoot.leftChild = newRoot.rightChild
        #if it wasn't None, change its parent
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = oldRoot
        ##change the newRoot's parent
        newRoot.parent = oldRoot.parent
        #if the old root was the tree's root, set the new tree root
        if oldRoot == self.root:
            self.root = newRoot
        else: #Otherwise, set the newRoot as the right or left child of the old parent
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        #set the oldRoot as the left child of the new root
        newRoot.rightChild = oldRoot
        #the parent of the old root is the new root
        oldRoot.parent = newRoot

        #update the balance factors
        oldRoot.balanceFactor = oldRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 - min(oldRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


    def __str__(self):
        return str(self.root)
