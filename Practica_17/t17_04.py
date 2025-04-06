import sys
sys.setrecursionlimit(1000000)

class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.mLeftChild = None
        self.mRightChild = None

    def empty(self):
        return self.key is None

    def insert(self, key):
        if self.empty():
            self.key = key
        elif key == self.key:
            return
        elif key < self.key:
            if self.mLeftChild is None:
                self.mLeftChild = BinaryTree(key)
            else:
                self.mLeftChild.insert(key)
        else:
            if self.mRightChild is None:
                self.mRightChild = BinaryTree(key)
            else:
                self.mRightChild.insert(key)

    def in_order_leaves(self, leaves):
        if self.mLeftChild is not None:
            self.mLeftChild.in_order_leaves(leaves)
        if self.mLeftChild is None and self.mRightChild is None:
            leaves.append(self.key)
        if self.mRightChild is not None:
            self.mRightChild.in_order_leaves(leaves)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    tree = None

    for num in numbers:
        if num == 0:
            break
        if tree is None:
            tree = BinaryTree(num)
        else:
            tree.insert(num)

    leaves = []
    if tree is not None:
        tree.in_order_leaves(leaves)

    print(" ".join(map(str, leaves)))


