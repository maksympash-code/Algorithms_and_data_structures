class TrieNode:
    def __init__(self):
        self.mChildren = {}
        self.is_end = False


def insert(root, number):
    node = root

    for digit in number:
        if node.is_end:
            return False
        if digit not in node.mChildren:
            node.mChildren[digit] = TrieNode()
        node = node.mChildren[digit]

    if node.is_end or node.mChildren:
        return False
    node.is_end = True
    return True

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        consistent = True
        root = TrieNode()
        for _ in range(n):
            number = input().strip()
            if not insert(root, number):
                consistent = False
        print("YES" if consistent else "NO")

if __name__ == "__main__":
    solve()
