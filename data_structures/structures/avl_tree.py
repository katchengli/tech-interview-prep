from structures.avl_node import AVLNode

class AVLTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = AVLNode(value)
            return self.root

    def __str__(self):
        return str(self.root)
