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

def validBST(root):
    s = list()
    node = root
    lastVisited = None
    while s or node != None:
        if node != None:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            if lastVisited == None or lastVisited.value < node.value:
                lastVisited = node
            else:
                return False
            node = node.right
    return True

root = BinaryTreeNode(50)
node1 = root.insert_left(30)
node2 = root.insert_right(80)
node3 = node1.insert_left(20)
node4 = node1.insert_right(60)
node5 = node2.insert_left(70)
node6 = node2.insert_right(90)

print(validBST(root))
