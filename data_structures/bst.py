from structures.binary_search_tree import BinarySearchTree

class BST(object):
    def __init__(self):
        pass

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.populateTree([5,4,5,7,9,10,3,7,8,11,2,1])
    print(tree)
    print(tree.findValue(4))
    print(tree.findValue(10))
    print(tree.findValue(13))
