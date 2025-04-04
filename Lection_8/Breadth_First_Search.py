from HW_14.t14_05 import *
from Tree import *

def BFS(tree: Tree):

    q = Queue()
    q.enqueue(tree)

    while not q.empty():
        current = q.dequeue()
        print(current.key(), end=" -> ")

        for child in current.getChildren():
            q.enqueue(child)