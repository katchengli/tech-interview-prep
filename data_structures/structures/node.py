# Currently creates a binary tree node...
class Node(object):
    def __init__(self):
        self.value = None
        self.rightChild = None
        self.leftChild = None

    def __str__(self):
        strrep = '[' + str(self.value) + ', (' + str(self.leftChild) + ', ' + str(self.rightChild) + ')]'
        return strrep
