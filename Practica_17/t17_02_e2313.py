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

    def count(self):
        cnt = 0
        stack = [self]
        while stack:
            node = stack.pop()
            cnt += 1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return cnt


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        print(0)
    else:
        tree = SearchTree(numbers[0])
        for num in numbers[1:]:
            if num == 0:
                break
            tree.insert(num)
        print(tree.count())