
INF = float('inf')

def hamming(a, b):
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1

    return count

def algo_Prima(mat):
    n = len(mat)

    dist = [INF] * n
    parent = [-1] * n
    visited = [False] * n

    dist[0] = 0
    pq = PriorityQueue()
    pq.insert(0, 0)

    total_weight = 0
    edges = []

    while not pq.empty():
        u = pq.extractMinimum()
        if visited[u]:
            continue

        visited[u] = True
        total_weight += dist[u]
        if parent[u] != -1:
            edges.append((parent[u], u))

        for v in range(n):
            if not visited[v]:
                w = hamming(mat[u], mat[v])
                if w < dist[v]:
                    dist[v] = w
                    parent[v] = u
                    if v in pq:
                        pq.updatePriority(v, w)
                    else:
                        pq.insert(v, w)

    return total_weight, edges




if __name__ == '__main__':
    n, k = map(int, input().split())
    mat = [input().rstrip() for _ in range(n)]

    total, edges = algo_Prima(mat)
    print(total)
    for u, v in edges:
        print(u, v)