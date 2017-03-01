from structures.node import Node

class AVLNode(Node):
    def __init__(self):
        super().__init__()
        self.balanceFactor = 0
        self.parent = None

    def __init__(self, parent, value):
        super().__init__(value)
        self.balanceFactor = 0
        self.parent = parent

    def isLeftChild(self):
        if self.parent != None and self.parent.leftChild == self:
            return True
        else:
            return False

    def isRightChild(self):
        if self.parent != None and self.parent.rightChild == self:
            return True
        else:
            return False

    def __str__(self):
        strrep = '[' + str(self.value) + '(bf: '+ str(self.balanceFactor) + '), (' + str(self.leftChild) + ', ' + str(self.rightChild) + ')]'
        return strrep
