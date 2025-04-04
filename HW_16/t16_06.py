class GameNode:
    def __init__(self, key, outcome = None):
        self.key = key
        self.outcome = outcome
        self.children = []


def minimax(node, turn):
    if node.outcome is not None:
        return node.outcome

    child_values = [minimax(child, -turn) for child in node.children]

    if turn == 1:
        return max(child_values)
    else:
        return min(child_values)



if __name__ == '__main__':
    n = int(input().strip())

    nodes = {}

    nodes[1] = GameNode(1)

    for i in range(2, n + 1):
        parts = input().split()
        typ = parts[0]
        parent = int(parts[1])
        if typ == 'N':
            node = GameNode(i)
        else:
            outcome = int(parts[2])
            node = GameNode(i, outcome)
        nodes[i] =  node
        nodes[parent].children.append(node)

    result = minimax(nodes[1], 1)

    if result == 1:
        print('+1')
    elif result < 0:
        print('-1')
    else:
        print('0')
