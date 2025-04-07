class SearchTree:
    def __init__(self,  key):
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


    def search_path(self, key):
        path = []
        node = self

        while node is not None:
            path.append(node.key)

            if key == node.key:
                break
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return path


if __name__ == '__main__':
    numbers = input().split()

    while len(numbers) < 1:
        numbers = input().split()

    seq = list(map(int, numbers))
    inserted = []

    for num in seq:
        if num == 0:
            break
        inserted.append(num)

    if not inserted:
        print('NO')
    else:
        tree = SearchTree(inserted[0])
        for num in inserted[1:]:
            tree.insert(num)

        path = tree.search_path(inserted[-1])
        print("YES" if path == inserted else 'NO')