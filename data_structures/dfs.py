from structures.tree import Tree

class DFS(object):
    def __init__(self):
        self.tree = Tree()

    def depth_first_search(self, val):
        scanStack = list()

        scanStack.append(self.tree.root)

        while scanStack:
            currentNode = scanStack.pop()
            if currentNode.value == val:
                return True
            else:
                if currentNode.leftChild is not None:
                    scanStack.append(currentNode.leftChild)
                if currentNode.rightChild is not None:
                    scanStack.append(currentNode.rightChild)

        return False


if __name__ == "__main__":
    dfs = DFS()
    dfs.tree.populateTree([5,4,5,6,7,8,1,2,9])
    print(dfs.tree)
    print(dfs.depth_first_search(45))
    print(dfs.depth_first_search(4))
    print(dfs.depth_first_search(7))
    print(dfs.depth_first_search(5))
    print(dfs.depth_first_search(-3))
