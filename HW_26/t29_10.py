from Practica_25.PriorityQueue import PriorityQueue

INF = float('inf')

def prim(n, adj):
    visited = [False] * n
    dist = [INF] * n
    parent = [-1] * n
    dist[0] = 0
    pq = PriorityQueue()
    pq.insert(0, 0)
    total = 0
    mst_edges = []
    while not pq.empty():
        u = pq.extractMinimum()
        if visited[u]:
            continue
        visited[u] = True
        total += dist[u]
        if parent[u] != -1:
            mst_edges.append((parent[u], u, dist[u]))
        for v, w in adj[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                parent[v] = u
                if v in pq:
                    pq.updatePriority(v, w)
                else:
                    pq.insert(v, w)
    if not all(visited):
        return None, None
    return total, mst_edges

def max_edge_on_path(n, tree_adj, u, target):
    visited = [False] * n
    def dfs(x, mx):
        visited[x] = True
        if x == target:
            return mx
        for y, w in tree_adj[x]:
            if not visited[y]:
                res = dfs(y, mx if mx > w else w)
                if res is not None:
                    return res
        return None
    return dfs(u, 0)

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))

    mst_weight, mst_edges = prim(n, adj)
    tree_adj = [[] for _ in range(n)]
    mst_set = set()
    for u, v, w in mst_edges:
        tree_adj[u].append((v, w))
        tree_adj[v].append((u, w))
        mst_set.add(frozenset((u, v)))

    second = INF
    for u, v, w in edges:
        if frozenset((u, v)) not in mst_set:
            mx = max_edge_on_path(n, tree_adj, u, v)
            if mx is not None:
                cand = mst_weight + w - mx
                if cand < second:
                    second = cand

    print(mst_weight, second)
