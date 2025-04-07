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

    def find_max(self):
        node = self

        while node.right is not None:
            node = node.right

        return node

    def second_maximum(self):
        max_node = self.find_max()
        if max_node.left is not None:
            node = max_node.left
            while node.right is not None:
                node = node.right
            return node.key
        node = self
        parent = None
        while node.right is not None:
            parent = node
            node = node.right
        return parent.key



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
    print(tree.second_maximum())