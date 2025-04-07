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


    def height(self):
        stack =[(self, 1)]
        max_height = 0
        while stack:
            node, height = stack.pop()
            if height > max_height:
                max_height = height
            if node.left is not None:
                stack.append((node.left, height + 1))
            if node.right is not None:
                stack.append((node.right, height + 1))
        return max_height

    def __str__(self):
        res = ""
        if self.left is not None:
            res += str(self.left)
        res += str(self.key)
        if self.right is not None:
            res += str(self.right)
        return res


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
        print(tree.height())