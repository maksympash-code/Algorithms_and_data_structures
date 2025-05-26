from Practica_25.PriorityQueue import PriorityQueue

INF = float('inf')

def edge_in_mst(n, edges, p, q):
    adj = [[] for _ in range(n)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    visited = [False] * n
    dist = [INF] * n
    parent = [-1] * n

    dist[0] = 0
    pq = PriorityQueue()
    pq.insert(0, 0)

    while not pq.empty():
        u = pq.extractMinimum()
        if visited[u]:
            continue
        visited[u] = True

        for v, w in adj[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                parent[v] = u
                if v in pq:
                    pq.updatePriority(v, w)
                else:
                    pq.insert(v, w)

    return parent[p] == q or parent[q] == p

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, p, q = map(int, input().split())
        p -= 1
        q -= 1

        edges = []
        for __ in range(m):
            u, v, w = map(int, input().split())
            edges.append((w, u - 1, v - 1))

        ans = edge_in_mst(n, edges, p, q)
        print("YES" if ans else "NO")
