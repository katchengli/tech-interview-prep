class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if value == None:
            return

        if self.root == None:
            self.root = BinaryTreeNode(value)
            return self.root

        currentNode = self.root
        while True:
            if currentNode.value == value:
                return
            elif value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = BinaryTreeNode(value)
                    return currentNode.left
                else:
                    currentNode = currentNode.left
            elif value > currentNode.value:
                if currentNode.right == None:
                    currentNode.right = BinaryTreeNode(value)
                    return currentNode.right
                else:
                    currentNode = currentNode.right



    def isSuperbalanced(self):
        superBalancedLeafSet = self.preOrder(self.root, 0)

        if len(superBalancedLeafSet) == 1 or len(superBalancedLeafSet) == 0:
            return True
        elif len(superBalancedLeafSet) > 2:
            return False

        elem1 = superBalancedLeafSet.pop()
        elem2 = superBalancedLeafSet.pop()

        diff = elem1 - elem2

        if diff > 1 or diff < -1:
            return False
        else:
            return True

    def preOrder(self, node, count):
        countSet = set()
        if node == None:
            return set()
        elif node.left == None and node.right == None:
            countSet.add(count+1)
        else:
            countSet |= self.preOrder(node.left, count+1)
            countSet |= self.preOrder(node.right, count+1)

        return countSet

t = BinaryTree()
t.insert(10)
t.insert(9)
t.insert(11)
print(t.isSuperbalanced())
t.insert(8)
t.insert(7)
print(t.isSuperbalanced())
t.insert(12)
t.insert(7)
print(t.isSuperbalanced())
