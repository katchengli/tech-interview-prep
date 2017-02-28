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
