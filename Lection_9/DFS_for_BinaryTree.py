from BinaryTree import BinaryTree

def DFS(tree: BinaryTree):
    print(tree.item)

    if tree.hasLeft():
        DFS(tree.leftChild())

    if tree.hasRight():
        DFS(tree.rightChild())