import sys
sys.setrecursionlimit(1000000)


class BinaryTree:
    def __init__(self, item, left=None, right=None):
        self.mItem = item
        self.mLeftChild = left
        self.mRightChild = right

    def empty(self):
        return self.mItem is None

    def insert(self, key):
        if self.empty():
            self.mItem = key
        elif key < self.mItem:
            if self.mLeftChild is None:
                self.mLeftChild = BinaryTree(key)
            else:
                self.mLeftChild.insert(key)
        elif key > self.mItem:
            if self.mRightChild is None:
                self.mRightChild = BinaryTree(key)
            else:
                self.mRightChild.insert(key)
        else:
            pass

    def height(self):
        if self.empty():
            return 0

        left_height = self.mLeftChild.height() if self.mLeftChild is not None else 0
        right_height = self.mRightChild.height() if self.mRightChild is not None else 0
        return 1 + max(left_height, right_height)


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

    if tree is None:
        print(0)
    else:
        print(tree.height())
