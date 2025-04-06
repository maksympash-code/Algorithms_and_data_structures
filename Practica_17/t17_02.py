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
        elif key > self.key:
            if self.mRightChild is None:
                self.mRightChild = BinaryTree(key)
            else:
                self.mRightChild.insert(key)


    def count(self):
        if self.empty():
            return 0

        l_count = self.mLeftChild.count() if self.mLeftChild is not None else 0
        r_count = self.mRightChild.count() if self.mRightChild is not None else 0
        return 1 + r_count + l_count


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    tree = BinaryTree()
    for num in numbers:
        if num == 0:
            break
        tree.insert(num)

    print(tree.count())