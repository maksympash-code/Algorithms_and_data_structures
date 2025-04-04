INF = float('inf')
P = 1000000007
q = 127

class TreeNode:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []

def merge_sorted(A, B):
    merged = []
    i, j = 0, 0
    local_min = INF
    prev = None
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            val = A[i]
            i += 1
        else:
            val = B[j]
            j += 1
        merged.append(val)
        if prev is not None:
            local_min = min(local_min, val - prev)
        prev = val
    while i < len(A):
        val = A[i]
        merged.append(val)
        if prev is not None:
            local_min = min(local_min, val - prev)
        prev = val
        i += 1
    while j < len(B):
        val = B[j]
        merged.append(val)
        if prev is not None:
            local_min = min(local_min, val - prev)
        prev = val
        j += 1
    return merged, local_min

def dfs(node):
    current_list = [node.value]
    current_min = INF
    for child in node.children:
        child_list, child_min = dfs(child)
        merged, merge_min = merge_sorted(current_list, child_list)
        current_list = merged
        current_min = min(current_min, child_min, merge_min)
    return current_list, current_min

def dfs_internal(node, internal_ans):
    if node.children:
        _, diff = dfs(node)
        if diff == INF:
            diff = 0
        internal_ans[node.index] = diff
    for child in node.children:
        dfs_internal(child, internal_ans)

def solve():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n = int(data[0])
    nodes = [None] * n
    root = None
    for i in range(n):
        parts = data[i+1].split()
        p = int(parts[0])
        v = int(parts[1])
        nodes[i] = TreeNode(i, v)
        if p == -1:
            root = nodes[i]
    for i in range(n):
        parts = data[i+1].split()
        p = int(parts[0])
        if p != -1:
            nodes[p].children.append(nodes[i])
    internal_ans = {}
    dfs_internal(root, internal_ans)
    result = 0
    q_powers = [1] * (n + 1)
    for i in range(1, n+1):
        q_powers[i] = (q_powers[i-1] * q) % P
    for idx, diff in internal_ans.items():
        result = (result + diff * q_powers[idx]) % P
    print(result)

if __name__ == '__main__':
    solve()
