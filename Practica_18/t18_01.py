class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_left(self, node):
        y = node.right
        T2 = y.left
        y.left = node
        node.right = T2
        self._update_height(node)
        self._update_height(y)
        return y

    def _rotate_right(self, node):
        y = node.left
        T3 = y.right
        y.right = node
        node.left = T3
        self._update_height(node)
        self._update_height(y)
        return y

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self._update_height(node)
        balance = self._get_balance(node)

        # Ліва-ліва
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Право - право
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Ліво - право
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Право - ліво
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        self._update_height(node)
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._exists(node.left, key)
        else:
            return self._exists(node.right, key)

    def exists(self, key):
        return self._exists(self.root, key)

if __name__ == '__main__':
    tree = AVLTree()
    output_lines = []

    try:
        while True:
            line = input().strip()
            if not line:
                continue

            parts = line.split()
            op = parts[0]
            x = int(parts[1])

            if op == 'insert':
                tree.insert(x)
            elif op == 'delete':
                tree.delete(x)
            elif op == 'exists':
                output_lines.append('true' if tree.exists(x) else 'false')
    except EOFError:
        pass

    for res in output_lines:
        print(res)
