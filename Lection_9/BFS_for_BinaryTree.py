from BinaryTree import BinaryTree
from HW_14.t14_05 import Queue


def BFS(tree: BinaryTree):

    q = Queue()
    q.enqueue(tree)

    while not q.empty():
        current = q.dequeue()
        print(current.item())

        if current.hasLeft():
            q.enqueue(current.leftChild())
        if current.hasRight():
            q.equeue(current.rightChild())
