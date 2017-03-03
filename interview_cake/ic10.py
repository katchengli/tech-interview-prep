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

def findSecondLargestElem(root):
    if root.left == None and root.right == None:
        return None

    first = root
    second = None

    while first.right != None :
        second = first
        first = first.right

    if first.left != None:
        second = first.left
        while second.right != None:
            second = second.right

    return second

root = BinaryTreeNode(50)
node1 = root.insert_left(30)
node2 = root.insert_right(80)
node3 = node1.insert_left(20)
node4 = node1.insert_right(40)
node5 = node2.insert_left(70)
node6 = node2.insert_right(90)

print(findSecondLargestElem(root).value)
