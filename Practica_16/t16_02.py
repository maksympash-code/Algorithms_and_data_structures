class TreeNode:
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.children = []
        self.depth = 0 if parent is None else parent.depth + 1

    def addChild(self, child):
        self.children.append(child)

def lca(node_a, node_b):
    while node_a.depth > node_b.depth:
        node_a = node_a.parent
    while node_b.depth > node_a.depth:
        node_b = node_b.parent
    while node_a != node_b:
        node_a = node_a.parent
        node_b = node_b.parent
    return node_a

if __name__ == '__main__':
    t = int(input())
    nodes = {1: TreeNode(1)}
    result = []

    for _ in range(t):
        parts = input().split()
        if parts[0] == 'ADD':
            a = int(parts[1])
            b = int(parts[2])
            parent_node = nodes[a]
            new_node = TreeNode(b, parent_node)
            parent_node.addChild(new_node)
            nodes[b] = new_node
        elif parts[0] == 'GET':
            a = int(parts[1])
            b = int(parts[2])
            lca_node = lca(nodes[a], nodes[b])
            result.append(str(lca_node.key))

    for res in result:
        print(res)