from structures.tree import Tree

class BFS(object):
    def __init__(self):
        self.tree = Tree()


if __name__ == "__main__":
    bfs = BFS()
    bfs.tree.populateTree([5,4,5,6,7,8,1,2,9])
    print(bfs.tree)
