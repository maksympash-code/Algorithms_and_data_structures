from Practica_25.PriorityQueue import PriorityQueue

INF = float('inf')

def algo_Prima(n, edges):
    adj = [[] for _ in range(n)]
    for w, u, v in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    visited = [False] * n
    dist = [INF] * n
    dist[0] = 0

    pq = PriorityQueue()
    pq.insert(0, 0)

    total_weight = 0

    while not pq.empty():
        u = pq.extractMinimum()
        if visited[u]:
            continue

        visited[u] = True
        total_weight += dist[u]

        for v, w in adj[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                if v in pq:
                    pq.updatePriority(v, w)
                else:
                    pq.insert(v, w)

    return total_weight





if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a - 1, b - 1))


    print(algo_Prima(n, edges))

