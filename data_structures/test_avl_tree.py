from structures.avl_tree import AVLTree

tree = AVLTree()
tree.insert(5)
tree.insert(6)
tree.insert(9)
tree.insert(11)
tree.insert(19)
tree.insert(10)
tree.delete(11)
print(tree)
