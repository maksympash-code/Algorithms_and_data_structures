from Tree import *

def DFS(tree: Tree):
    for child in tree.getChildren():
        DFS(child)

    print(tree.key(), end=" -> ")