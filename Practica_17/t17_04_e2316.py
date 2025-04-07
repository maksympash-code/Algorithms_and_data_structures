class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key == node.key:
                break
            elif key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right

    def in_order_leaves(self, leaves):
        stack = []
        current = self
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.left is None and current.right is None:
                leaves.append(current.key)
            current = current.right


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    tree = None

    for num in numbers:
        if num == 0:
            break
        if tree is None:
            tree = SearchTree(num)
        else:
            tree.insert(num)

    leaves = []
    if tree is not None:
        tree.in_order_leaves(leaves)

    print(" ".join(map(str, leaves)))