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

    def find_max(self):
        node = self

        while node.mRightChild is not None:
            node = node.mRightChild
        return node


def reverse_inorder(node, result, limit = 2):
    if node is None or len(result) >= limit:
        return
    reverse_inorder(node.mRightChild, result, limit)
    if len(result) < limit:
        result.append(node.key)
    reverse_inorder(node.mLeftChild, result, limit)



def second_max(tree: BinaryTree):
    max_node = tree.find_max()
    if max_node.mLeftChild is not None:
        return max_node.mLeftChild.find_max().key
    res = []
    reverse_inorder(tree, res)
    return res[1]

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    tree = BinaryTree()

    for num in numbers:
        if num == 0:
            break
        tree.insert(num)
    print(second_max(tree))