from collections import deque

class Tree:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []

    def BFS(self, key, came_from=None):
        queue = deque()
        queue.append(self)
        while queue:
            current = queue.popleft()
            if current is came_from:
                continue
            if current.key == key:
                return current
            for child in current.children:
                queue.append(child)
        return None

    def add_child(self, parent_key, key):
        parent = self.BFS(parent_key)
        if parent is None:
            return
        node = Tree(key, parent)
        parent.children.append(node)

    def lca(self, i, j):
        node = self.BFS(i)
        came_from = None
        while True:
            if node.BFS(j, came_from) is not None:
                return node.key
            came_from = node
            node = node.parent

        # node_i = self.BFS(i)
        # node_j = self.BFS(j)
        #
        # def get_depth(node):
        #     d = 0
        #     while node is not None:
        #         d += 1
        #         node = node.parent
        #     return d
        #
        # depth_i = get_depth(node_i)
        # depth_j = get_depth(node_j)
        #
        # while depth_i > depth_j:
        #     node_i = node_i.parent
        #     depth_i -= 1
        # while depth_j > depth_i:
        #     node_j = node_j.parent
        #     depth_j -= 1
        # while node_i != node_j:
        #     node_i = node_i.parent
        #     node_j = node_j.parent
        # return node_i

if __name__ == '__main__':
    f = open("input.txt")
    k = int(f.readline())
    tree = Tree(1)
    for _ in range(k):
        cmd, *args = f.readline().split()
        a, b = map(int, args)
        if cmd == "ADD":
            tree.add_child(a, b)
        elif cmd == "GET":
            print(tree.lca(a, b))
    f.close()